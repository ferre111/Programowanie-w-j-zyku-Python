print("\n\r SAX \n\r")

import xml.sax

class BreakfasHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrenData = ""
        self.name = ""
        self.price = ""
        self.description = ""
        self.calories = ""

    def startElement(self, tag, attributes):
        self.CurrenData = tag
        if tag == "food":
            print("***FOOD***")

    def endElement(self, tag):
        if self.CurrenData == "name":
            print("Name:", self.name)
        elif self.CurrenData == "price":
            print("Price:", self.price)
        elif self.CurrenData == "description":
            print("Description:", self.name)
        elif self.CurrenData == "calories":
            print("Calories", self.calories)
        self.CurrenData = ""

    def characters(self, content):
        if self.CurrenData == "name":
            self.name = content
        elif self.CurrenData == "price":
            self.price = content
        elif self.CurrenData == "description":
            self.description = content
        elif self.CurrenData == "calories":
            self.calories = content


parser = xml.sax.make_parser()
# parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = BreakfasHandler()
parser.setContentHandler(Handler)

parser.parse("example.xml")

print("\n\r DOM \n\r")

from xml.dom import minidom

doc = minidom.parse("example.xml")
foods = doc.getElementsByTagName("food")
#change val
for food in foods:
    food = food.getElementsByTagName("price")[0].childNodes[0]
    food.nodeValue = "$3.00"

with open("example_after_discount.xml", "w") as f:
    f.write(doc.toxml())
