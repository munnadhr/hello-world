
import os
from xml.etree import ElementTree
from xml.dom import minidom
file = "test.xml"
full_path = os.path.abspath(os.path.join('data',file))
print(full_path)

#defination for getting the some of all prices
def total(A):
    result = 0
    for i in A:
        result = result + i
        
    return result
#parsing the data
data = ElementTree.parse('test.xml')
catalog = data.findtext('catalog')
book = data.findall('book')

data1 = minidom.parse('test.xml')
book1 = data1.getElementsByTagName('book')

prices = []
for i,j in zip(book,book1):
 #getting the id attribute
    id1 = j.attributes["id"].value
    author = i.find('author').text
    price = i.find('price').text
    prices.append(float(i.find('price').text))
    date = i.find('publish_date').text
    title = i.find('title').text
    print( "'*' {} : {} ':' {} {} {}".format(id1,author,title,date,price))
    
print(total(prices))
