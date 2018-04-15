from bs4 import BeautifulSoup
import re

def extract_hyperlink_from_rip (page):

    with open(page, encoding="utf-8") as f:
        data = f.read()
        soup = BeautifulSoup(data, 'html.parser')

        linkList = []

        for link in soup.find_all('a'):
            linkList.append(link.get('href'))

        good_url = {}

        for link in linkList:
            if ('hybrid' in link or 'indica' in link or 'sativa' in link):
                name = re.sub('[/indica/][/hybrid/][/sativa/]', '', link)
                name = name.replace('/', '')
                good_url[name] = 'https://www.leafly.com'+link

    return good_url