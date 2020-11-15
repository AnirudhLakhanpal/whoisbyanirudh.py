#!/usr/bin/python2

import os
import sys

#THIS TOOL IS CODED IN PYTHON2 BY ANIRUDH LAKHANPAL
print("\033[93m ")
os.system("figlet WHOIS BY ANIRUDH")


url = raw_input("[+] Enter website : ")
os.system("whois %s" (url))