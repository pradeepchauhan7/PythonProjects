from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request

file = input("Enter the file path :\n")
with open(file) as fp:
   line = fp.readline()
   while line:
        page = line.strip()
        reqs = Request(page, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
        html_page = urlopen(reqs).read()
        soup = BeautifulSoup(html_page, "lxml")
        links = []
        print("\n")
        print(line.strip() + "\n")
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            links.append(link.get('href'))
        for link in links:
            req = Request(link, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
            html_page = urlopen(req).read()
            #html_page = urlopen(link)
            soup = BeautifulSoup(html_page, "lxml")
            #soup = html_page.read().decode('utf-8')
            #print("\n")
            if(len(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?!png|gif)[A-Za-z]{2,4}", str(soup))) > 0):
                for i in set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?!png|gif)[A-Za-z]{2,4}", str(soup))):
                    print(i)

        line = fp.readline()