import urllib.request,urllib.parse,urllib.error
import json
a = input("enter--")
url = urllib.request.urlopen(a).read()
A = json.loads(url)
items = (A["comments"])
sum = 0
for i in items:
    sum += i["count"]
print(sum)