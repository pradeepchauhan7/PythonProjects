from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request
import os

file = input("Enter the file path :\n")
f = open('newContactDetails.txt', 'a')
f.write(
    "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
with open(file) as fp:
   line = fp.readline()
   while line:
        page = line.strip()
        reqs = Request(page, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
        try:
            html_page = urlopen(reqs).read()
        except:
            print("error ")
        soup = BeautifulSoup(html_page, "lxml")
        links = []
        f.write("\n")
        f.write(str(line.strip()) + "\n")
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            links.append(link.get('href'))
        for link in links:
            req = Request(link, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
            try:
                html_page = urlopen(req).read()
            except:
                print("error")
            #html_page = urlopen(link)
            soup = BeautifulSoup(html_page, "lxml")
            #soup = html_page.read().decode('utf-8')
            #print("\n")
            if(len(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?!png|gif|jpg)[A-Za-z]{2,4}", str(soup))) > 0):
                for i in set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?!png|gif)[A-Za-z]{2,4}", str(soup))):
                    f.flush()
                    os.fsync(f.fileno())
                    f.write(str(i) + "\n")
        f.write(
            "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        line = fp.readline()
f.close()