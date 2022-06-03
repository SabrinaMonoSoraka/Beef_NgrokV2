#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from time import sleep
import sys

def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        elif color.lower() == "yellow":
            attr.append('33')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

def hor():
    os.system("clear")
    print color ("  Hours        Date","green")
    os.system(' date +"  %R      %D" ')

hor()
print color("""
    ───▄▄▄
    ─▄▀░▄░▀▄
    ─█░█▄▀░█
    ─█░▀▄▄▀█▄█▄▀
    ▄▄█▄▄▄▄███▀

 Checking System ...  

""","yellow")

if os.system("gnome-terminal --help > /dev/null 2>&1"):
    print color(" [ X ] gnome-terminal not found","red")
    print color(" installing ...","blue")
    os.system("sudo apt-get install gnome-terminal -y > /dev/null 2>&1")
    print color(" [ ✔ ] gnome-terminal ","yellow")
else:
    print color(" [ ✔ ] gnome-terminal ","yellow")
sleep(1.0)
if os.system("./server/ngrok -v > /dev/null 2>&1"):
    print color(" [ X ] Server not found","red")
    print color(" installing ...","blue")
    os.system("wget https://github.com/SabrinaMonoSoraka/Fake_Screen/raw/main/ngrok && mv ngrok server && chmod +x server/ngrok > /dev/null 2>&1")
    print color(" [ ✔ ] server ","yellow")
else:
    print color(" [ ✔ ] Server ","yellow")
sleep(1.0)
if os.system("apache2 -v > /dev/null 2>&1"):
    print color(" [ X ] apache2 not found","red")
    print color(" installing ...","blue")
    os.system("sudo apt-get install apache2 -y > /dev/null 2>&1")
    print color(" [ ✔ ] apache2 ","yellow")
else:
    print color(" [ ✔ ] apache2 ","yellow")
sleep(1.0)

print("")
print color(" All ready :)", "green")
print("")


