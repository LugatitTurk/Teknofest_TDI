#Bu kodlar anvilin arayüzünde çalıştırılan kodlardır bunu kendiniz çalıştırmanız için 
#anvil hesabı oluşturup ardından gerekli bileşenleri ekleyerek bu kodu doğru bir şekilde çalıştırmalısınız
#Bu konuyla ilgili video Youtube sayfamızda bulunmaktadır göz atabilirsiniz.
#Ayrıca bu kodların backendle iletişime geçebilmesi için google colabda yazmış olduğumuz kodu da çalıştırmalısını gene youtubeden buna ulaşabilirsiniz. 







from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import anvil.server



class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    kategory = anvil.server.call('predict_tweet', self.tweet_metin.text)
    print(kategory)
    if kategory:
      layout = go.Layout(
      title='GÜVENLİK EĞİLİMİ'
      )

      layout2 = go.Layout(
      title='İÇERİK TEMASI'
      )

      if(len(kategory)  == 3):
        self.label_1.visible = True
        metin1 =  "Şiddete Yönlendirici: %" + (str(kategory[2])) [:5] +  "\n Şiddet İçerikli/Zorbalık: %"+ (str(kategory[1]))[:5] + "\n Diğer : %" + (str(kategory[0]))[:5]
        self.label_1.text = "Güvenlik Eğilimi: \n" + metin1
      
        
      
        data = [kategory[0], kategory[1], kategory[2]]  # Örnek yüzdelik veriler     
        labels = ['Diğer', 'Şiddet İçerikli Zorbalık', 'Şiddete Yönlendirici']  # Sınıf etiketleri
        pie = go.Pie(labels=labels, values=data)
        self.plot_1.data = [pie]
        self.plot_1.layout = layout
        self.plot_2.visible = False

      elif(len(kategory) == 2):
        data = [kategory[0][0], kategory[0][1], kategory[0][2]]  # Örnek yüzdelik veriler     
        labels = ['Diğer', 'Şiddet İçerikli Zorbalık', 'Şiddete Yönlendirici']  # Sınıf etiketleri
        pie = go.Pie(labels=labels, values=data)
        self.plot_1.data = [pie]
        self.plot_1.layout = layout

        
        metin2 = "Dünya : % " + str(kategory[1][0])[:5] + "\n Ekonomi : % "+ str(kategory[1][1])[:5] + "\n Kültür : %" + str(kategory[1][2])[:5] + "\n Sağlık : %" + str(kategory[1][3])[:5] + "\n Siyaset : %" + str(kategory[1][4])[:5]+ "\n Spor : %" + str(kategory[1][5])[:5]+ "\n Diğer: %" + str(kategory[1][6])[:5] 
        metin1 =  "Şiddete Yönlendirici: %" + (str(kategory[0][2])) [:5] +  "\n Şiddet İçerikli/Zorbalık: %"+ (str(kategory[0][1]))[:5] + "\n Diğer : %" + (str(kategory[0][0]))[:5]
        self.label_1.text = "Güvenlik Eğilimi: \n" + metin1 + "\n \n Tema: \n " + metin2 
        data2 = [kategory[1][0], kategory[1][1], kategory[1][2],kategory[1][3], kategory[1][4], kategory[1][5], kategory[1][6]]  # Örnek yüzdelik veriler
        labels2 = ['Dünya', 'Ekonomi', 'Kültür','Sağlık','Siyaset','Spor','Diğer' ]  # Sınıf etiketleri
        pie2 = go.Pie(labels=labels2, values=data2)
        self.plot_2.data = [pie2]
        self.plot_2.layout = layout2
        self.plot_2.visible = True

  

   
  


  def file_loader_1_change(self, file, **event_args):
    file = self.file_loader_1.file
    kategory  = anvil.server.call('process_uploaded_file', file)
    print(kategory)
    if kategory:
          self.label_1.visible = True
          metin1 =  "Şiddete Yönlendirici: " + str(kategory[0][2])[:5] +"\n Şiddet İçerikli/Zorbalık: "+ str(kategory[0][1])[:5] + "\n Diğer : " + str(kategory[0][0])[:5]
          metin2 = "Dünya : " + str(kategory[1][0])[:5] + "\n Ekonomi : "+ str(kategory[1][1])[:5] + "\n Kültür : " + str(kategory[1][2])[:5] + "\n Sağlık : " + str(kategory[1][3])[:5] + "\n Siyaset : " + str(kategory[1][4])[:5]+ "\n Spor : " + str(kategory[1][5])[:5]+ "\n Diğer: " + str(kategory[1][6])[:5] 
          self.label_1.text = "Güvenlik Eğilimi: \n" + metin1 + "\n \n Tema: \n " + metin2

          layout = go.Layout(
          title='ORTALAMA GÜVENLİK EĞİLİMLERİ'
          )

          layout2 = go.Layout(
          title='ŞİDDETE YÖNLENDİRİCİ KATEGORİSİNİN TEMANIN DAĞILIMI'
          )
      
          data = [kategory[0][0], kategory[0][1], kategory[0][2]]  # Örnek yüzdelik veriler
          labels = ['Diğer', 'Şiddet İçerikli Zorbalık', 'Şiddete Yönlendirici']  # Sınıf etiketleri
          pie = go.Pie(labels=labels, values=data,layout=layout)
          self.plot_1.data = [pie]
          self.plot_1.layout = layout
      
          data2 = [kategory[1][0], kategory[1][1], kategory[1][2],kategory[1][3], kategory[1][4], kategory[1][5], kategory[1][6]]  # Örnek yüzdelik veriler
          labels2 = ['Dünya', 'Ekonomi', 'Kültür','Sağlık','Siyaset','Spor','Diğer' ]  # Sınıf etiketleri
          pie2 = go.Pie(labels=labels2, values=data2,layout=layout)
          self.plot_2.data = [pie2]
          self.plot_2.layout = layout2
          self.plot_2.visible = True