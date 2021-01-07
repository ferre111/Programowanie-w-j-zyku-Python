import os

path = "C:\\Karol\\Studia\\Semestr 5\\DL"


def fun(path):
    file = []
    dir = []
    all_files = []

    for all_files in os.listdir(path):
        if os.path.isfile(os.path.join(path, all_files)):
            file.append(all_files)
        else:
            dir.append(os.path.join(path, all_files))

    print(path + ":")
    print("    -" + ', '.join(file))

    for dir_path in dir:
        fun(dir_path)


fun(path)
