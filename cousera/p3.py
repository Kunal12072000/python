import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url = input()
posi = int(input("posi"))
times = int(input("time"))

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
tags = soup('a')
l = []
for tag in tags:
    l.append(tag.get('href','known_by_'))
k = l[posi - 1]
for i in range(times - 1):
    html = urllib.request.urlopen(k).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    l = []
    for tag in tags:
        l.append(tag.get('href', 'known_by_'))
    k = l[posi - 1]
    print(k)
    l.clear()

