#Python3
#Language code by sTiKyt
import sys
import gettext
from Defs.Configurations import readConfig

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
    language = readConfig().get("Settings", "Language")

    if language == "en":
        langEnglish()
    elif language == "ru":
        langRussian()
    elif language == "uk":
        langUkrainian()
    else:
        langEnglish()


def languageSelector():
    for arg in sys.argv:
        if arg in ["--language", "--lang"]:
            for arg in sys.argv:
                if arg in ["ru", "russian", "ru_RU"]:
                    langRussian()
                elif arg in["en", "eng", "english", "en_UK", "en_US"]:
                    langEnglish()
                elif arg in["uk", "ukraine", "ukrainian", "uk_UA"]:
                    langUkrainian()
        else:
            exit()
