#Python3
#Language code by sTiKyt
import sys
import gettext
from Defs.Configurations import ConfigurationManager

class LocalizationManager:
    def installGetText():
        gettext.install('hiddeneye', './locale')

    def langRussian():
        ru = gettext.translation('hiddeneye',localedir='./locale', languages=['ru'])
        ru.install()

    def langUkrainian():
        uk = gettext.translation('hiddeneye',localedir='./locale', languages=['uk'])
        uk.install()

    def langEnglish():
        en = gettext.translation('hiddeneye',localedir='./locale', languages=['en'])
        en.install()


    def checkAndSetLanguage():
        language = ConfigurationManager.readConfig().get("Settings", "Language")

        if language == "en":
            LocalizationManager.langEnglish()
        elif language == "ru":
            LocalizationManager.langRussian()
        elif language == "uk":
            LocalizationManager.langUkrainian()
        else:
            LocalizationManager.langEnglish()


    def languageSelector():
        for arg in sys.argv:
            if arg in ["--language", "--lang", "-l"]:
                for arg in sys.argv:
                    if arg in ["ru", "russian", "ru_RU"]:
                        LocalizationManager.langRussian()
                    elif arg in["en", "eng", "english", "en_UK", "en_US"]:
                        LocalizationManager.langEnglish()
                    elif arg in["uk", "ukraine", "ukrainian", "uk_UA"]:
                        LocalizationManager.langUkrainian()
                    else:
                        exit
