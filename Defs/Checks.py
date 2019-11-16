#Checks functions

from urllib.request import urlopen
from os import *
from time import sleep
from subprocess import check_output
from platform import system as systemos, architecture
from wget import download
from Defs.Languages import *
import os
import subprocess
import ctypes

RED, GREEN, DEFAULT = '\033[91m', '\033[1;32m', '\033[0m'

installGetText()
languageSelector()
	
def checkConnection(host='https://google.com'): #Connection check
    system('clear')
    try:
        urlopen(host, timeout=10)
        print(_("{0}HURRAY!! Internet is available.. We can Continue{1}").format(GREEN, DEFAULT))
        print(_("\n\n{0}Wait! Checking for Neccesary Packages{1}...\n ").format(GREEN, DEFAULT))
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

def checkbinaryLT(): #LocalTunnel Binary File check.
    if path.isfile('Server/lt') == False:  #Is LocalTunnel downloaded?
        print(_('[*] LocalTunnel Binary File Not Found !!'))
        print(_('[*] Downloading LocalTunnel...'))
        system("wget https://www.wa4e.com/downloads/lt-linux.zip")
        system('unzip lt*.zip && rm lt*.zip && mv lt* lt && mv lt Server/lt ')
        system('clear')
	    
def checkLT(): #Ask to install npm,node.js,localtunnel(packages).
    if 256 == system('which lt > /dev/null'):
       system('clear')
       print(_("{0}[{1}?{0}] Do You Want To Install LOCALTUNNEL(Tunneling Service) Packages.\n{0}[{1}*{0}]{1} May take time , Skip if not wants to use LocalTunnel(Package Version).").format(RED, GREEN, DEFAULT))
       choice = input(" \n({1}Y{2}/{2}(N)>> {2}".format(RED, GREEN, DEFAULT))
       if choice == 'y' or choice == 'Y':
          system('clear')
          installLT()
       elif choice == 'n' or choice == 'N':
          print(_("\n{0}[{1}!{0}]{0} You can not use LocalTunnel(Package Version).\n{0}[{1}!{0}]{0} But still You Can Use LocalTunnel(Binary Version).\n\n\n").format(RED, GREEN, DEFAULT))
          input('Press Enter To Continue')
          system('clear')
       else:
          return checkLT()
    else:
       print("[*] LocalTunnel Packages Found !!")
       sleep(2)
       system('clear')
        	    
def installLT(): #Localtunnel check
        print(_('[*] Installing LocalTunnel...'))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            system("apt-get -y update;apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel-termux;clear")
            checkagainLT()
        else:
            system("apt-get -y update;apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel;clear")
            checkagainLT()

def checkagainLT(): #Check if Localtunnel installed correctly or not.
    if 256 == system('which lt > /dev/null'):
        system('clear')
        print('[ERROR]: LocalTunnel Packages Does Not Installed Correctly...')
        print('')
        input('[^] Press Enter To Go Back To installation..')
        checkLT()
    else:
        print('[SUCCESS] LocalTunnel Installed.')
        sleep(2)
        
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
