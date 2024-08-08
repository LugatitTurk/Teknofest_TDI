# Teknofest_TDI
Teknofest 2024 NLP (Türkçe Doğal Dil İşleme) Yarışması Github Projesi


## Model Kullanımı
Modeli kullanmak için iki yol izleyebilirsiniz:

### 1) Hugging Face Aracılığıyla
Tüm denediğimiz modeller arasından en iyi 5 modeli HuggingFace sayfamıza (https://huggingface.co/LugatitTurk) yüklemiş bulunmaktayız. Bu sayede modelimizi denemek veya kullanmak için githubdan modeli indirmeniz gerekmemektedir. 
HuggingFace aracılığıyla modeli kullanmak için,

```
# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

tokenizer = AutoTokenizer.from_pretrained("LugatitTurk/LugatitBert")
model = AutoModelForSequenceClassification.from_pretrained("LugatitTurk/LugatitBert")
```
```
def ModelTahmini(metin):
  inputs = tokenizer(metin, return_tensors="pt")
  outputs = model(**inputs)
  first_three_probs = outputs[0][0][:3]
  probabilities = F.softmax(first_three_probs, dim=0)
  percentages = probabilities * 100
  result = percentages.detach().numpy()
  return result

result = ModelTahmini('metniniz')
print(f"Diğer: %{result[0]}, Şiddet İçerikli: %{result[1]}, Yönlendirici: %{result[2]}")
```
veya 
```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="LugatitTurk/LugatitBert")
```
yöntemlerini kullanabilirsiniz.

### 2) Github'daki modelin dosyalarıyla
Github'da bulunan modelin boyutu 100mb'dan büyük olduğundan ötürü model git-lfs yönetemiyle yüklenmiştir. Modeli kullanmak için;

1. Git LFS'i Kur:
Eğer bilgisayarında Git LFS yüklü değilse, öncelikle Git LFS'i kurman gerekir. Terminale şu komutu yazarak kurabilirsin:
```
git lfs install
```

2. Depoyu Klonla:
Depoyu klonladığında, Git LFS tarafından izlenen büyük dosyalar otomatik olarak indirilecektir. Depoyu klonlamak için;
```
git clone https://github.com/LugatitTurk/Teknofest_TDI.git
```

3. Modeli Kullanma
Modeli clone'ladıktan sonra modeli kullanabilirsiniz. Modeli kullanmak için;
```
# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

tokenizer = AutoTokenizer.from_pretrained("modelin_konumu")
model = AutoModelForSequenceClassification.from_pretrained("modelin_konumu")
```
```
def ModelTahmini(metin):
  inputs = tokenizer(metin, return_tensors="pt")
  outputs = model(**inputs)
  first_three_probs = outputs[0][0][:3]
  probabilities = F.softmax(first_three_probs, dim=0)
  percentages = probabilities * 100
  result = percentages.detach().numpy()
  return result

result = ModelTahmini('metniniz')
print(f"Diğer: %{result[0]}, Şiddet İçerikli: %{result[1]}, Yönlendirici: %{result[2]}")
```
veya 
```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="LugatitTurk/LugatitBert")
```


## Datasetleri 
Projemiz 2 model içermektedir. Bu modellerin eğitimi için kullanılan datasetleri data klasörünün içindeki datasets klasöründe bulunmaktadır.

#### LügatiBert'in Datasetleri
LugatiBert modelimizi eğitmek için;
  - data klasöründe bulunan data scraper kodu aracılığıyla Twitter'dan elde edilen veriler,
    
  - Hazır datasetleri
    - https://huggingface.co/datasets/Overfit-GM/turkish-toxic-language
    - https://huggingface.co/datasets/nanelimon/insult-dataset
      
  - Sentetik veriler

kullanılmıştır.

#### LugatiHaber'in Datasetleri
LugatiHaber modelimizi eğitmek için;
  - Hazır dataseti
      - https://www.kaggle.com/datasets/anil1055/turkish-headlines-dataset

kullanılmıştır.



![Interactive-Neural-Network-Opera-2024-08-07-01-03-28-_online-video-cutter com_](https://github.com/user-attachments/assets/cf4772c9-90a8-4251-8106-092f19cf472f)





