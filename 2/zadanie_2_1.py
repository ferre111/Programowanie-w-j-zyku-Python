import os

path = "C:\\"

path, dirs, files = next(os.walk(path))
print(len(files))
