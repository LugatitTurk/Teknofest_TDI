from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time
import json
import os
import configparser
from browsermobproxy import Server
import requests
import re

words ={"kelime"} #Buraya aratmak istediğiniz kelimeleri yazın 
      


def scrape_twitter_with(search_word):
    print("Çalışma dizini:", os.getcwd())

    username = "Twitter Kullanıcı Adı"
    password = "Twitter Şifreniz"
    word = search_word
    max_tweets = 50 #kaç tweet aramak isterseniz girin


    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    url = "https://x.com/login"
    ileri = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'
    giris = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'
    driver.get(url)

    wait = WebDriverWait(driver,20)
    retry_amount=0
    while True:
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[autocomplete = "username"]'))).send_keys(username)
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH,ileri)))
            next_button.click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[autocomplete = "current-password"]'))).send_keys(password)
            giris_button = wait.until(EC.element_to_be_clickable((By.XPATH,giris)))
            giris_button.click()
            # Sayfanın yüklenmesi için biraz bekleyin
            time.sleep(5)

            url2 = "https://x.com/search?q=cat&src=typed_query"

            #tweets = driver.find_elements(By.CSS_SELECTOR, 'div[lang]')
            driver.get("https://x.com/search?q=" + search_word + "&src=typed_query&f=live")
            time.sleep(10)

            tweets = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article div[lang]'))
            )
            break
        except:
            print("trying again")
            time.sleep(5)
            if retry_amount>5:
                time.sleep(100)

    # Belirli sayıda tweet toplamak için bir döngü ve sayaç kullanın
    collected_tweets = 0
    tweets_text = set()
    tweets_data = []
    
    
    # specified the file path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "TeknoFest")
    file_path = os.path.join(desktop_path, search_word + '.json')


    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_tweets = json.load(f)
            existing_tweet_ids = {tweet['id'] for tweet in existing_tweets}
    else:
        existing_tweets = []
        existing_tweet_ids = set()

    while collected_tweets < max_tweets:
        # Tweet'leri seçmek için CSS seçiciyi kullanın
        tweets = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article'))
        )

        # Tweetleri toplama sayısını güncelleyerek listeye ekleyin
        for tweet in tweets:
            try:
                tweet_text_element = tweet.find_element(By.CSS_SELECTOR, 'div[lang]')
            except:
                continue
            tweet_text = tweet_text_element.text if tweet_text_element else ""

            # Mention'ları kaldırmak için tweet metnini temizle
            cleaned_tweet_text = re.sub(r'@\w+', '', tweet_text).strip()

            # img elementlerini al ve src attribute'larını çek
            tweet_images = tweet.find_elements(By.CSS_SELECTOR, 'img')
            images = [img.get_attribute('src') for img in tweet_images if 'pbs.twimg.com/media' in img.get_attribute('src')]
            
        
            # Tweet ID'sini tweet URL'sinden al
            tweet_id_element = tweet.find_element(By.CSS_SELECTOR, 'a[href*="/status/"]')
            tweet_id = tweet_id_element.get_attribute('href').split('/')[-1]

            if tweet_id not in existing_tweet_ids:  # Aynı tweet'i birden fazla kez almamak için
                tweets_data.append({"id": tweet_id, "tweet": cleaned_tweet_text, "images": images})
                collected_tweets += 1
                existing_tweet_ids.add(tweet_id)
            if collected_tweets >= max_tweets:
                break

        # Daha fazla tweet yüklemek için sayfayı kaydırın
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)  # Sayfanın yüklenmesi için bekleyin

    # WebDriver'ı kapat
    driver.quit()


    # Yeni tweet verilerini mevcut verilerle birleştir
    existing_tweets.extend(tweets_data)

    # Birleştirilmiş verileri JSON dosyasına kaydet
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_tweets, f, ensure_ascii=False, indent=4)

    print(f"{len(tweets_data)} yeni tweet toplandı ve mevcut 'tweets.json' dosyasına eklendi.")
    
    
    
for word in words:
    print("\nscraping " + word)
    json_file = f"{word}.json"
    if os.path.exists(json_file):
        print(f"{json_file} already exists. Skipping scraping for {word}.")
    else:
        scrape_twitter_with(word)
        time.sleep(10)
