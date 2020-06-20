#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#
import base64
import getpass
import platform
import re as regular_expression
import socket
from distutils.dir_util import copy_tree as webpage_set
from io import BytesIO
from os import chdir
from os import chmod
from os import getuid
from os import mkdir
from os import path
from os import remove
from os import replace
from os import stat
from os import system
from pathlib import Path as pathlib_Path
from shutil import copyfile
from shutil import rmtree
from subprocess import call as run_command
from subprocess import CalledProcessError
from subprocess import check_call as try_to_run_command
from subprocess import check_output
from subprocess import DEVNULL
from subprocess import PIPE
from subprocess import Popen as run_background_command
from time import sleep as wait
from urllib import request as url_request
from zipfile import ZipFile

import requests
from pyngrok import conf as ngrok_conf
from pyngrok import ngrok
