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

tokenizer = AutoTokenizer.from_pretrained("LugatitTurk/LugatitBert")
model = AutoModelForSequenceClassification.from_pretrained("LugatitTurk/LugatitBert")
```
veya 
```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="LugatitTurk/LugatitBert")
```
yöntemlerini kullanabilirsiniz.

### 2) Github'daki modelin dosyalarıyla
Github'da bulunan modelin dosyalarıyla modeli denemek veya kullanmak için,

```
# Load the tokenizer and model for inference
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("LugatitTurk/LugatitBert")
model = AutoModelForSequenceClassification.from_pretrained("modelin_konumu") #İndirilen modelin konumu

# Create a pipeline for sentiment analysis
nlp = pipeline("text-classification", model=model, tokenizer=tokenizer)
```
yöntemini kullanabilirsiniz.


## Datasetleri 
Projemiz 2 model içermektedir. Bu modellerin eğitimi için kullanılan datasetleri **data klasörünün içindeki **datasets klasöründe bulunmaktadır.
#### LügatiBert 


![Interactive-Neural-Network-Opera-2024-08-07-01-03-28-_online-video-cutter com_](https://github.com/user-attachments/assets/cf4772c9-90a8-4251-8106-092f19cf472f)





