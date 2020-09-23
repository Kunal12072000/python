import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck</name>
    <phone type = "intl">
        +91 8887608359
    </phone>
    <email hide = "yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
input = """
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>kunal</name>
        </user>
        <user x="5">
            <id>005</id>
            <name>himanshi</name>
        </user>
    </users>
</stuff>"""
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print("user count",len(lst))
for items in lst:
    print('Name:',items.find('name').text)
    print("ID:",items.find('id').text)
    print('attributes:',items.get("x"))
