from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient

"""
client = MongoClient()
db = client.test
tb = db.stackoverflow_collection
"""
for i in range(1, 10):
    html_page = urlopen("https://stackoverflow.com/users?page=" + repr(i) + "&tab=reputation&filter=all")
    soup = BeautifulSoup(html_page, "lxml")
    user_details = soup.find_all('div', class_="user-details")
    for i in user_details:
        for tag in i.children:
            if(tag.string == None):
                continue
            elif(len(tag.string) > 1):
                print(tag.string)
        print('\n')

