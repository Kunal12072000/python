import re
hand = open('ass11')
l = list()
for i in hand:
    i = i.rstrip()
    stuff = re.findall('([0-9]+)',i)
    for i in range(len(stuff)):
        num = int(stuff[i])
        l.append(num)
a = sum(l)
print(a)