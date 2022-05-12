from lib2to3.pgen2 import driver

from selenium import webdriver


"""
from tkinter.tix import Tree
import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup

import lxml
"""



driver = webdriver.Chrome('/home/curry1824/Desktop/chromedriver_linux64/chromedriver')


url = "https://www.ambito.com/contenidos/dolar.html"
driver.get(url)

content = driver.page_source
"""
response = requests.get(url)



soup = BeautifulSoup(content)


quotes_html = soup.find_all('span', class_="text")
authors_html = soup.find_all('small', class_="author")

print(quotes_html)


for a in soup.findAll('a',href=True, attrs={'class':'second m-0 w-auto'}):
    
    price=a.find('div', attrs={'class':'value data-venta'})
    PrecioDolarBlue = price

print(soup.find_all)
print(PrecioDolarBlue)    
"""


PrecioDolarBlue=(driver.find_element_by_xpath("/html/body/main/div[3]/div[8]/div[2]/div/div[2]/div[2]/span[1]").text)
print(PrecioDolarBlue)

