from configobj import ConfigObj

config=ConfigObj('config.ini')
print(config["product"])
print(config["accessories"])