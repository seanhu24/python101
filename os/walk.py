import os

path=r"d:\\PycharmProjects\\python101\\"

for root,dirs,files in os.walk(path):
    print(root)
    for _dir in dirs:
        print(_dir)
    for _file in files:
        print(_file)