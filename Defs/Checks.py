#Checks functions

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
	
def checkConnection(host='https://google.com'): #Connection check
    system('clear')
    try:
        urlopen(host, timeout=10)
        print(_("{0}HURRAY!! Internet is available.. We can Continue{1}").format(GREEN, DEFAULT))
        return True
    except:
        return False

if checkConnection() == False:
        print (_('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}

          {0}[{1}!{0}]{1} ^Network error^. Verify your Internet connection.\n
''').format(RED, DEFAULT))
        exit(0)
	
def checkNgrok(): #Ngrok check
    
    if path.isfile('Server/ngrok') == False:  #Is Ngrok downloaded?
        print(_('[*] Ngrok Not Found !!'))
        print(_('[*] Downloading Ngrok...'))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')

def checkLocalxpose(): #Localxpose check
    if path.isfile('Server/loclx') == False:  #Is Localxpose downloaded?
        print(_('[*] Localxpose Not Found !!'))
        print(_('[*] Downloading Localxpose...'))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'loclx-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'loclx-linux-amd64.zip'.format(ostype)
            else:
                filename = 'loclx-linux-386.zip'.format(ostype)
        url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
        download(url)
        system('unzip loclx*.zip && rm loclx*.zip')
        system('mv loclx* loclx')
        system('mv loclx Server/')
        system('clear')
def checkLT(): #Localtunnel check
        print(_('[downloading localtunnel]'))
        if not system('lt')!=256:
            if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):system('apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel-termux')
            elif systemos()=='Windows': #windows
                download('https://nodejs.org/dist/v12.13.0/node-v12.13.0-x{0}.msi'.format('64' if architecture()[0]=='64bit' else '86'))
                print('Select NodeJS and Node Package Manager (npm) for installation.')
                system('node-v12.13.0-x{0}.msi'.format('64' if architecture()[0]=='64bit' else '86'))
                system('npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel')
            else:
                ch=input('1 npm installation\n2 Binary installation\nHiddenEye>>> ')
                if ch=='1':system('apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel;echo 1 > .ltrc')#linux
                elif ch=='2':system('wget https://wa4e.com/downloads/lt-linux.zip;unzip lt-linux.zip;chmod +x lt*;mv lt* Server/lt;echo 0 > .ltrc')
                else: checkLT()
        system('clear')
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
                raise PermissionError("{0}Permissions denied! Please run as '{1}sudo{0}'".format(RED, GREEN)) 
        else:
            raise PermissionError("{0}Permissions denied! Unexpected platform".format(RED))
