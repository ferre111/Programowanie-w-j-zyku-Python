import os, re
from PIL import Image

path = "C:\\Karol\\Studia\\Semestr 5\\PwJP\\2"

for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(path, filename))
        data = re.search(r"(.*)\.", filename)
        image.save(os.path.join(path, data.group(1) + ".png"))
