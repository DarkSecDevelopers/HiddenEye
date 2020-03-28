# HiddenEye Installation Guide

|  Platform| Click Below |
| ------ | ------ |
| Termux App | [Check Here](#install-in-termux-) |
| Userland App | [Check Here](#install-in-userland-app-) |
| Kali/Linux | [Check Here](#install-in-kalilinux-) |
| BlackArch | [Check Here](#install-in-blackarch-) |
| Archlinux/Manjaro | [Check Here](#install-in-arch-linuxmanjaro-) |

--------------------------------------------
## HiddenEye Clone URL

### **```git clone https://github.com/DarkSecDevelopers/HiddenEye.git```**

--------------------------------

## Install In Termux :

* **pkg install git python php curl openssh grep -y**
* **git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git**
* **pip install requests**
* **chmod 777 HiddenEye**
* **cd HiddenEye**

* Run : **python HiddenEye.py** or **./HiddenEye.py**


### Or USE SINGLE COMMAND
```
pkg install git python php curl openssh grep -y && git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git && chmod 777 HiddenEye && cd HiddenEye && pip install requests && python HiddenEye.py
```

------------------------------------

## Install In Userland App :

* **Install userland app from playstore.**
* **Set up app and install kali from app.Set ssh username(anyname) and password.**
* **When kali will run it'll ask for password type the ssh password.Then do su.After that kali will run on your device wothout root and do apt update**
* **For more info read here (https://null-byte.wonderhowto.com/how-to/android-for-hackers-turn-android-phone-into-hacking-device-without-root-0189649/)**

* **sudo apt install python3 python3-pip unzip php git -y**
* **git clone https://github.com/DarkSecDevelopers/HiddenEye.git**
* **chmod 777 HiddenEye**
* **pip3 install requests**
* **cd HiddenEye**

* Run : **python3 HiddenEye.py**

------------------------------------

### Install In Kali/Linux :

* **sudo apt install python3 python3-pip unzip php git -y**
* **git clone https://github.com/DarkSecDevelopers/HiddenEye.git**
* **chmod 777 HiddenEye**
* **sudo pip3 install requests**
* **cd HiddenEye**

* Run : **python3 HiddenEye.py** OR **./HiddenEye.py**

------------------------------------

### Install In BlackArch :

* **sudo pacman -S hidden-eye**
#### Run : **sudo hidden-eye**

------------------------------------

### Install In Arch Linux/Manjaro :

* **sudo pacman -Syu**
* **sudo pacman -S python-pip**
* **chmod 777 HiddenEye**
* **cd HiddenEye**
* **sudo pip3 install requests**

* Run : **sudo python3 HiddenEye.py** OR **sudo ./HiddenEye.py**

------------------------------------

<h3>Fix Ascii error</h3>

`dpkg-reconfigure locales`

`Then select: "All locales" Then select "en_US.UTF-8"`

`After that reboot your machine. Then open terminal and run the command: "locale"`

`There you will see "en_US.UTF-8" which is the default language. Instead of POSIX.`

------------------------------------
