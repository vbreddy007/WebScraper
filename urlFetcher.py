#get URLs from answers.sap.com
# python -m pip install requests
#python -m pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep

def getURL(page_num):
     url_collected=[]
     URL_template = "https://answers.sap.com/index.html?page={}&pageSize=15&sort=active&filter=all"
     URL = URL_template.format(page_num)
     print(URL)
     req = requests.get(URL)
     soup = bs(req.text, 'html.parser')
#dm-contentListItem__title
     div_tags = soup.find_all('div',class_='dm-contentListItem__title')
     url_collected = [item.get('href') for item in div_tags]
     href_values = []
     for div_tag in div_tags:
        a_tags = div_tag.find_all('a')
        href_values += [a_tag.get('href') for a_tag in a_tags]

     print(len(div_tags))
     string = 'https://answers.sap.com'
     final_list=[string + s for s in href_values]
     #temp_final_list = final_list[0:1]
     #for i in temp_final_list:
        #print(i)
     with open('urls1.txt', 'a') as file:
    # Loop through the URLs and write each one to a new line in the file
        for url in final_list:
         file.write(url + '\n')
     #return final_list
for i in range(101,200):    
  getURL(i)

#first run iscompleted untill 100 pages urls
#urls collected into urls.txt until 4 to 100 pages 1st iteration
#urls collected into urls.txt until 101 to 200 pages 1st iteration





#print(href_values)

#urls_final = list(dict.fromkeys(url_collected))
#urls_final = list(filter(None, urls_final))




