# Themes Manager
import sys
from Defs.Configurations import readConfig, ifSettingsNotExists

color = [0, 0, 0, 0, 0]
config = readConfig()


def colorSelector():
    ifSettingsNotExists()
    for arg in sys.argv:
        if arg in ['--theme']:
            for arg in sys.argv:
                if arg in ['anaglyph', '3danaglyph', '3Danaglyph', '3DAnaglyph']:
                    # LightRed, BackgroundCyan, Cyan, Green, ResetAll
                    color = ['\033[91m', '\033[46m',
                             '\033[36m', '\033[32m',  '\033[0m']
                    if arg in ['--default']:
                        config.set("Defaults", "theme", "anaglyph")
                    return color
                if arg in ['ocean', 'breeze', 'blue']:
                    # Cyan, BackgroundCyan, BrightBlue, DarkGray, ResetAll
                    color = ['\033[36m', '\033[46m',
                             '\033[34m', '\033[30m', '\033[0m']
                    if arg in ['--default']:
                        config.set("Defaults", "theme", "ocean")
                    return color
    if config.get("Defaults", "theme") == "anaglyph":
        color = ['\033[91m', '\033[46m', '\033[36m', '\033[32m',
                 '\033[0m']  # LightRed, BackgroundCyan, Cyan, Green, ResetAll
        return color
    elif config.get("Defaults", "theme") == "ocean":
        # Cyan, BackgroundCyan, BrightBlue, DarkGray, ResetAll
        color = ['\033[36m', '\033[46m', '\033[34m', '\033[30m', '\033[0m']
        return color
