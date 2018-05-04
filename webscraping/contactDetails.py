from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re

links = []
c = 0
ur = "http://www.laundryandcleaningnews.com/contractors/indexAtoZ.html"
reqs = Request(ur, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
html_page = urlopen(reqs).read()
soup = BeautifulSoup(html_page, "lxml")


for link in soup.findAll('a', attrs={'href': re.compile("^/contractors[-/a-zA-Z0-9]+/$")}):
    #if (c == 840):
     #   break
    links.append('http://www.laundryandcleaningnews.com' + link.get('href'))
    #c += 1
s = (set(links))
#print(len(links))

print("\n")
for i in s:
    req = Request(i, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, "lxml")
    ud =soup.find_all('p')
    intro = soup.find('h1')
    for j in ud:
        if(len(j)>10):
            print(intro.get_text(strip=True) + "\n")
            print(j.get_text("? ",strip=True))
            #print(''.join(j.findAll(text=True)))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


"""
html_page = urlopen("http://www.laundryandcleaningnews.com/contractors/workwear-rental-products/alexandra-plc/")
soup = BeautifulSoup(html_page, "lxml")
user_details = soup.find_all('p')
#print(user_details.next_sibling)

for i in user_details:
    print(''.join(i.findAll(text=True)))
"""

