import configobj

def createConfig(path):
    config=configobj.ConfigObj(path)
    config.filename=path
    config["Sony"]={}
    config["Sony"]["product"] = "Sony PS3"
    config["Sony"]["accessories"] = ['controller', 'eye', 'memory stick']
    config["Sony"]["retail price"] = "$400"
    config.write()

if __name__ == '__main__':
    createConfig("config2.ini")