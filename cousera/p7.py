import urllib.request,urllib.parse,urllib.error
import json
import  ssl

api_key = False
if api_key is False:
    api_key = 42
    service1 = 'http://py4e-data.dr-chuck.net/json?'
else:
    service1 = "https://maps.googleapis.com/maps/api/geocode/json?"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    adress = input("enter")
    if len(adress) < 1 : break
    parms = dict()
    parms["address"] = adress
    if api_key is not False: parms['key'] = api_key
    url = service1 + urllib.parse.urlencode(parms)
    print('Retriving',url)
    uh = urllib.request.urlopen(url,context=ctx)
    data = uh.read().decode()
    print(len(data))
    js = json.loads(data)
    print(js["results"][0]["place_id"])
