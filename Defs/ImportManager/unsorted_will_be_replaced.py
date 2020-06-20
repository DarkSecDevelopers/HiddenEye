#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#


from subprocess import call as run_command, check_call as try_to_run_command, Popen as run_background_command, check_output, CalledProcessError, DEVNULL, PIPE
from distutils.dir_util import copy_tree as webpage_set
from time import sleep as wait
from os import path, system, chmod, stat, mkdir, remove, chdir, replace, getuid
from shutil import rmtree, copyfile
from pathlib import Path as pathlib_Path
from pyngrok import conf as ngrok_conf, ngrok
import re as regular_expression
import getpass
import base64
import socket
import requests
import platform
import requests
from urllib import request as url_request
from zipfile import ZipFile
from io import BytesIO
