import xml.etree.ElementTree as ET
tree = ET.parse('map.xml')
root = tree.getroot()
data = root[1][0].text
result = [x.strip() for x in data.split(',')]
print (result)
print (int(result[0]))

# root = ET.fromstring('map.xml')