import urllib.request,urllib.parse,urllib.error
import bs4

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

But soft what light through yonder window breaks