from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
# from pymongo import MongoClient
import urllib, re

print ("Enter the URL")
page = input()
req = Request(page, headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()
html_page = urlopen(page)
soup = html_page.read().decode('utf-8')
#print (re.findall(r"\+\d{2}\s?0?\d{10}", soup))
print("\n")
print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", soup))

#