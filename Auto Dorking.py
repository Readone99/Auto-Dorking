#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# ===== #
# Xnero13-Id
# YouTube: https://m.youtube.com/channel/UCzXNg0OhpDuckHT_Ty-lF2A
# ===== #

# ===== #
# Created Januari | Copyright (c) 2021 Xnero13-Id
# ===== #

########################################################################

# A notice to all nerds and n00bs...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################


from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time


# Auto Dorking


if sys.version[0] in "2":
    print ("\n[x] ..n00b.. Auto Dorking Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tDorks Eye \033[1;91mI like to See Ya, Hacking \033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = (""" (             )      )\ )             )               
   )\      (  ( /(     (()/(      (   ( /((        (  (  
((((_)(   ))\ )\())(    /(_))  (  )(  )\())\  (    )\))( 
 )\ _ )\ /((_|_))/ )\  (_))_   )\(()\((_)((_) )\ )((_))\ 
 (_)_\(_|_))(| |_ ((_)  |   \ ((_)((_) |(_|_)_(_/( (()(_)
  / _ \ | || |  _/ _ \  | |) / _ \ '_| / /| | ' \)) _` | 
 /_/ \_\ \_,_|\__\___/  |___/\___/_| |_\_\|_|_||_|\__, | 
                                                  |___/ """)




for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)




x = ("""
 Author:  Xnero13-Id
 Github:  https://github.com/Readone99\n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = ("""Siap Untuk Menjelajah Karena Tidak Ada Sytem Yang Aman😃""")
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[+] Outpute File Mau Disimpen Apa Kaga Om ? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] Sampai Jumpa Kembali Nanti \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Saving is Skipped...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] Tulis Dork Nya Disini Bang Jago: ")
        amount = input("[+] Kira Kira Mau Berapa Site Nihh Om? : ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    print ("\n\t\t\t\t\033[34mDorks Eye\033[0m")
    print ("\t\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()