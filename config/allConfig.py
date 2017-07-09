import configparser
import os

def create_config(path):
    """
    create a config file
    :param path:
    :return:
    """
    config=configparser.ConfigParser()
    config.add_section("settings")
    config.set("setting", "font", "Courier")
    config.set("setting", "font_size", "15")
    config.set("setting", "font_style", "Normal")
    config.set("Settings", "font_info", "You are using %(font)s at %(font_size)s pt")

    with open(path,'w') as config_file:
        config.write(config_file)

def get_config(path):
    """
    return the config object
    :param path:
    :return:
    """
    if not os.path.exists(path):
        create_config(path)

    config=configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    """
    print out a setting
    :param path:
    :param section:
    :param setting:
    :return:
    """
    config=get_config(path)
    value=config.get(section,setting)
    msg="{section} {setting} is {value}".format(section=section, setting=setting, value=value)
    print(msg)
    return msg

def update_setting(path, section, setting, value):
    """
    update a setting
    :param path:
    :param section:
    :param setting:
    :param value:
    :return:
    """
    config=get_config(path)
    config.set(section,setting,value)

    with open(path, 'w') as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    delete a setting
    :param path:
    :param section:
    :param setting:
    :return:
    """
    config=get_config(path)
    config.remove_option(section,setting)

    with open(path, 'w') as config_file:
        config.write(config_file)


if __name__=='__main__':
    path='settings.ini'
    font=get_setting(path,"Settings","font")
    font_size=get_setting(path, "Settings", "font_size")
    update_setting(path, "Settings", "font_size", "21")
    delete_setting(path, "Settings", "font_style")
