from urllib.request import urlopen
from os import *
from subprocess import check_output
from platform import system as systemos, architecture
from wget import download
from Defs.Languages import *
import os
import ctypes

RED, GREEN, DEFAULT = '\033[91m', '\033[1;32m', '\033[0m'

installGetText()
languageSelector()
	
def checkConnection(host='https://google.com'):
    system('clear')
    try:
        urlopen(host, timeout=10)
        print(("{0}[connection:alive]{1}").format(GREEN, DEFAULT))
        return True
    except:
        return False

if not checkConnection():
        print (('{1}[connection:alive]{0}').format(RED, DEFAULT))
        exit(0)
	
def checkNgrok(): #Ngrok check
    if not path.isfile('Server/ngrok'):
        print('[collecting ngrok]')
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        download('https://bin.equinox.io/c/4VmDzA7iaHb/' + filename)
        system('unzip '+filename+';mv ngrok Server/ngrok;rm -Rf '+filename+';clear')

def checkLocalxpose(): #Localxpose check
    if not path.isfile('Server/loclx'):  #Is Localxpose downloaded?
        print('[collecting localxpose]')
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'loclx-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'loclx-linux-amd64.zip'.format(ostype)
            else:
                filename = 'loclx-linux-386.zip'.format(ostype)
        download('https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename)
        system('unzip loclx*.zip;rm loclx*.zip;mv loclx* loclx;mv loclx Server/;clear')

def checkLT():
    if not path.isfile('/usr/local/bin/lt'):
        print(_('[downloading localtunnel]'))
        system('apt -y install npm;npm cache clean -f; npm install -g n ;n stable ;npm install -g localtunnel ;clear')
def checkPermissions():
        if systemos() == 'Linux':
            if os.getuid() == 0:
                print("{0}Permissions granted!".format(GREEN))
            else:
                raise PermissionError("{0}Permissions denied! Please run as '{1}sudo{0}'".format(RED, GREEN)) 
        elif systemos() == 'Windows':
            if ctypes.windll.shell32.IsUserAnAdmin() != 0:
                print("{0}Permissions granted!".format(GREEN))
            else:
                raise PermissionError("{0}Permissions denied! Please run as Administrator".format(RED))
        elif systemos() == 'Darwin':
            if os.getuid() == 0:
                print("{0}Permissions granted!".format(GREEN))
            else:
                raise PermissionError("{0}Please run as '{1}sudo{0}'".format(RED, GREEN)) 
        else:
            raise PermissionError("{0}[unsupported platform]".format(RED))
