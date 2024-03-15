import requests
from bs4 import BeautifulSoup
import xlsxwriter

URL = 'https://busaat.az/politics'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
sayfa = requests.get(URL, headers = headers)
icerik = BeautifulSoup(sayfa.content,'html.parser')

list = icerik.find("section", {"class": "article-list-class grid-list ajax-list"})
date = list.find_all("div", {"class": "meta-date meta-item"})
title = list.find_all("div", {"class": "article-title"})

umumiAd = []
umumiTarix = []
umumiLink = []

for adlar in title:
    umumiAd += adlar

for tarix in date:
    umumiTarix += tarix

for href in list:
   umumiLink += href

book = xlsxwriter.Workbook('Elchin_Novruzov.xlsx')
page = book.add_worksheet()

x = range(0, 24)
y = -1

for n in x:
    page.write(n, 0, umumiTarix[n].get_text())
    page.write(n, 1, umumiAd[n].get_text())

for z in x:
    umumiLink[z] = title[z].find("a").get("href")
    page.write(z, 2, umumiLink[z])


book.close()