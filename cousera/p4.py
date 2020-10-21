import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url = input()

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
tags = soup('count')
sum = 0
for i in range(len(tags)):
    sum += int(tags[i].text)
print(sum)
