#Primitive config
import configparser
import os

class ConfigurationManager:
    def createConfig(path = "Settings.ini"):
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.add_section("Defaults")
        config.set("Settings", "Language", "en")
        config.set("Settings", "DidBackground", "True")
        config.set("Defaults", "webPage", "Facebook")
        config.set("Defaults", "additionalOption", "1")
        with open(path, 'w') as configFile:
            config.write(configFile)

    def readConfig(path = "Settings.ini"):
        config = configparser.ConfigParser()
        config.read(path)
        return config

    def ifSettingsNotExists():
        if not os.path.exists("Settings.ini"):
            ConfigurationManager.createConfig()
