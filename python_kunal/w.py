# un tag the uslful lines tried and tested
import bs4 as bs
import urllib.request
souce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/")
soup = bs.BeautifulSoup(souce,"lxml")
print(soup.title.text)             #printing the whole string
#print(soup.find_all('p'))          # finding any specific character
#for i in soup.find_all('p'):       #itereating throug the strings

 #   print(i.string)
print(soup.get_text())        #usefull in finding the text in the doc coz it may be possible that the website don't use the paragraph tags
for url in soup.find_all('a'):
    #print(url)                # prints the whole url
    print(url.text)    # pints the text in the url
  #  print(url.get('href'))  # prints the workable url