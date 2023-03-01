## This script will scrap the content from the question URL
#from urlFetcher import getURL
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#url_list = getURL()
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

#for url in url_list:
#print(url)
#req = requests.get("https://answers.sap.com/questions/13824788/api-for-sd-invoice-download.html")
urls = []
processed = 0
with open('urls1.txt', 'r') as file:
    #urls = file.read().splitlines()
    #urls = file.readline().strip()
    urls = file.readlines()
    urls = [url.strip() for url in urls[416:1485]]
    

for url in urls: 
 with open('urls_visisted_log1.txt', 'a',encoding='utf-8') as file:
  file.write(url + '\n') 
 req = requests.get(url)
 soup = bs(req.text, 'html.parser')
 div_tags = soup.find('div',class_='ds-question__content')
 #print(div_tags)
 p_tags = div_tags.find('p')
 #print(p_tags.text)
 with open('scrapedQandA1.txt', 'a',encoding='utf-8') as file:
  file.write(p_tags.text + '\n')
 # write the text to scrapedQandA.txt file
 driver.get(url)
 #print("the content in driver URL"+url)
 html = driver.page_source
 soup1 = bs(html, "html.parser")
 answer_div_tags = soup1.find_all(class_='ds-answer__content')
 #print(answer_div_tags)
 for answer_div in answer_div_tags:
  answer_p_tags = answer_div.find_all("p")
  for answer_p in answer_p_tags:
	     #print(answer_p.text)
	     # write content to the scrapedQandA.txt file
   with open('scrapedQandA1.txt', 'a',encoding='utf-8') as file:
    file.write(answer_p.text + '\n')
    processed += 1
    print(f"Processed{processed} URLs.") 
print(f"Total {processed}Processed URLs.") 






	 
	


# div with class name : ds-question__content
# div with class name : ds-answer__content



       