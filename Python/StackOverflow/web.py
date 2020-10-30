import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

x = input('Enter the Location: ')
#print('Retrieving ',x)
str1 = ''
fhand = urllib.request.urlopen(x)
for line in fhand:
    word = line.decode()
    str1 += word
#print(str1)
try:
    tree = ET.fromstring(str1)
    lst = tree.findall('.//')
except:
    print('No Element Found!!')
for i in lst:
    print(i.text)
    #print(type(i))
    #print(i.tag, i.attrib)
    #print('Count: ',i)
print('End of Website')