from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient

"""
client = MongoClient()
db = client.test
tb = db.stackoverflow_collection
"""

html_page = urlopen("https://stackoverflow.com/users")
soup = BeautifulSoup(html_page, "lxml")
print(soup.p['class'])

