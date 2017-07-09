import configparser
import os

def crudConfig(path):
    """
    create, read, update and delete config
    :param path:
    :return:
    """
    if not os.path.exists(path):
        createConfig(path)

    config=configparser.ConfigParser()
    config.read(path)

    font=config.get("Settings","font")
    font_size=config.get("Settings","font_size")

    config.set("Settings","font","12")

    config.remove_option("Settings","font_style")

    with open(path,'w') as config_file:
        config.write(config_file)


if __name__=='__main__':
    path="settings.ini"
    crudConfig(path)
