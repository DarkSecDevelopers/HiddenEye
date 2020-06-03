#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import Defs.ThemeManager.theme as theme

default_palette = theme.default_palette


def print_sorted_as_menu(sorting_list):
    col_width = max(len(word) for row in sorting_list for word in row) + 2
    for row in sorting_list:
        print("".join(word.ljust(col_width)
                      for word in row).format(default_palette[0],
                                              default_palette[2]))
