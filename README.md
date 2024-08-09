
![lugatitturk-high-resolution-logo (3)](https://github.com/user-attachments/assets/dba710a6-e246-44fb-872d-78ead64bd9ac)

# Teknofest 2024 NLP (Türkçe Doğal Dil İşleme) Yarışması Github Projesi

**Not: Github klasör ve dosyalaımızın içerikleritle ilgili bilgi edinmek için README dosyasının en altına inebilirsiniz**

Projemizde 2 modeli birleştirerek tek bir model oluşturduk. Bu alt modellerden LügatitBert girdiyi(leri) sınıflandırma görevini yerine getirirken LugatitHaberler girdinin temasını belirlemektedir. LügatitBert girdiyi üç sınıfa ayırıyor, bunlar şiddet içerikli (zorbalık, küfür, hakaret vb.), yönlendirici (toplumu eylem, toplumsal hareket, galeyan gibi herhangi bir aksiyon almaya yönlendiren/ teşvik eden) ve diğer. LugatitHaberler girdiyi yedi temaya ayırıyor, bunlar Dünya, Ekonomi, Kültür, Sağlık, Siyaset, Spor, Diğer. Oluşturduğumuz bu model iki çeşit girdi alabiliyor ve bu girdinin tipine göre çıktı veriyor. 

![modelimiz](https://github.com/user-attachments/assets/6e1eef4f-2dc0-43c5-bbef-c3b044098b84)

**Kullanım seneryosu 1:** Tekil girdi
Modelimize tek bir tweet/cümle/metin girdi olarak verildiğinde öncelikle LügatitBert bu tekil girdinin sınflandırmasını yapıyor. Eğer sınıflandırma sonucu ana odağımız olan 'yönlendirici' kategorisi olursa bu girdi hakkında daha fazla bilgi edinmek amacıyla LugatitHaberler girdinin temasını belirliyor. Bu durumda LügatitBert her sınıf için bir aidiyet olasılığı çıktı veriyor ve girdi, aidiyet olasılığının en yüksek olduğu sınıfa atanıyor. LugatitHaberler de aynı şekilde her tema için bir aidiyet olasılığı çıktı veriyor ve girdi, aidiyet olasılığının en yüksek olduğu temaya atanıyor. 

**Kullanım seneryosu 2:** Çoklu girdi
Modelimize birden fazla tweet/cümle/metin excel dosyası formatında girdi olarak verildiğinde öncelikle LügatitBert sınıfların exceldeki dağılımını çıktı veriyor. Eğer girilen excel 'yönlendirici' sınıfında veri içeriyosa LugatitHaberler ile bu sınıfta olduğu belirlenen verilerin tema dağılımı çıktı veriliyor. Sınıflar ve temalar belirlenirken yine aidiyet olasılıklarından en yükseği kullanılıyor.

## Modellerin Kullanımı

Denediğimiz tüm modeller arasından **en iyi 5 modeli** [HuggingFace sayfamıza](https://huggingface.co/LugatitTurk) yüklemiş bulunmaktayız. Bu sayede modelimizi denemek veya kullanmak için githubdan modeli indirmenize gerek yok. Peki modellerimizi nasıl kullanacaksınız?

### 1) Hugging Face Aracılığıyla
HuggingFace aracılığıyla modeli kullanmak için öncelikle transformers, torch ve torch.nn.functional kütüphanelerini indirmelisiniz. Daha sonra aşağıdaki şekilde modellerimizi kullanabilirsiniz. 

```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

egilimTokenizer = AutoTokenizer.from_pretrained("LugatitTurk/LugatitBert")
egilimModel = AutoModelForSequenceClassification.from_pretrained("LugatitTurk/LugatitBert")

haberTokenizer = AutoTokenizer.from_pretrained("LugatitTurk/LugatitHaberler")
haberModel = AutoModelForSequenceClassification.from_pretrained("LugatitTurk/LugatitHaberler")


```
Modelimizin çıktılarını düzenlemek ve daha anlaşlır kılmak amacıyla bizler aşağıdaki MetinTahmini fonksiyonunu kullandık, sizlere de bu methodu kullanmanızı öneriyoruz.
```
def MetinTahmini(metin):
  inputs = egilimTokenizer(metin, return_tensors="pt")
  logits = egilimModel(**inputs)
  outputs = logits[0][0][:3]
  probabilities = F.softmax(outputs, dim=0)
  percentages = probabilities * 100
  result = percentages.detach().numpy()

  if( result[0] < result[2] and result[1] < result[2] ):
    inputs = haberTokenizer(metin, return_tensors="pt")
    logits = haberModel(**inputs)
    outputs = logits[0][0]
    probabilities = F.softmax(outputs, dim=0)
    percentages = probabilities * 100
    result2 = percentages.detach().numpy()
    return [result,result2]
  else :
     return result

```

### 2) Github Aracılığıyla
Modelimizin boyutu 100mb'dan büyük olduğundan ötürü model Github'a [**Git LFS**](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) yönetemiyle yüklenmiştir. Modeli kullanmak için izlemeniz gereken adımları aşağıda bulabilirsiniz.

**1. Git LFS'i Kur:**
Eğer bilgisayarında Git LFS yüklü değilse, öncelikle Git LFS'i kurman gerekir. Terminale şu komutu yazarak kurabilirsin:
```
git lfs install
```

**2. Depoyu Klonla:**
Depoyu klonladığında, Git LFS tarafından izlenen büyük dosyalar otomatik olarak indirilecektir. Terminale şu komutu yazarak klonlayabilirsin:
```
git clone https://github.com/LugatitTurk/Teknofest_TDI.git
```

**3. Modeli Kullanma**
Modeli clone'ladıktan sonra modeli kullanabilirsiniz. Modeli nasıl kullanacağını öğrenmik için bu partın en başına dönebilirsin.


## Datasetleri 

Projemiz 2 model içermektedir. Bu modellerin eğitimi için kullanılan datasetleri data klasörünün içindeki datasets klasöründe bulunmaktadır.

#### *LügatitBert'in Veri Setleri*
LugatiBert modelimizi eğitmek için üç temel yüntem kullandık.
  **1- veri toplama:**
  Data klasöründe bulunan data scraper kodu aracılığıyla Twitter'dan veri topladık,
    
  **2- Hazır datasetleri**
  İncelediğimiz iki veri setinden modelimiz için uygun olan birkaç veri kullandık, bunlar;
  -  [Overfit'in veriseti](https://huggingface.co/datasets/Overfit-GM/turkish-toxic-language)
  -  [NaneLimon'un veri seti](https://huggingface.co/datasets/nanelimon/insult-dataset)
      
  **3- Sentetik veri üretimi**
  Modelin başarısını arttırmak ve veri kapsamımızı genişletmek için sentetik veri ürettik.
  
Kullandığımız bu yöntemlerle toplam **100 bin** veriye ulaştık.

#### *LugatitHaberler'in Datasetleri*
LugatiHaber modelimizi eğitmek için [Anıl Güven'in veri seti](https://www.kaggle.com/datasets/anil1055/turkish-headlines-dataset)'ni kullandık.

## Github klasör ve dosyalarımız

### 1- data
Bu klasör veri ile ilgili yaptığımız işlemleri içermektedir. İçerisinde data scraper, datasets ve promptlar bulunmaktadır.
#### *data scraper:*
Bu klasör veri toplamak için hazırladığımız kod ve yöntemi içerir.
#### *datasets:*
Bu klasör kullandığımız hazır verisetlerini içerir.
#### *promptlar:*
---
Bu klasör veri etiketleme aşamasında GPT üzerinde kullandığımız promptları içerir.

### 2- models
Bu klasör projemiz için oluşturduğumuz modellerini içermektedir.

### 3- resources
Bu klasör ara işlemler için kullandığımız kod ve yöntemleri içermektedir.
#### *fotoğraflar*
---
README'de kullandığımız fotoğrafları içerir.
#### *kendi stopwords*
---
topladığımız veriye göre oluşturduğumuz stopwordleri içerir.
#### *stopwordTemizleyici*
---
Başarı oranı en yüksek model için kullandığımız stopword temizleme kodumuzu içerir.
#### *trainer*
---
Oluşturduğumuz modeli eğitme kodumuzu içerir.

### 4- TDDİ Final Sunum Şablonu
Teknofest TDDİ serbest kategori final sunumumuz.


![Interactive-Neural-Network-Opera-2024-08-07-01-03-28-_online-video-cutter com_](https://github.com/user-attachments/assets/cf4772c9-90a8-4251-8106-092f19cf472f)





