#!/usr/bin/python

from random import randint
import os

cor = ['\033[95m', '\033[96m', '\033[92m','\033[93m','\033[91m','\033[0m']
colors = cor[randint(0,5)]

def examples():
	os.system("clear")
        print(colors+ """

    /$$$$$$$              /$$     /$$$$$$$$               /$$$$$$$$       
   | $$__  $$            | $$    | $$_____/              |__  $$__/       
   | $$  \ $$  /$$$$$$  /$$$$$$  | $$     /$$$$$$   /$$$$$$ | $$  /$$$$$$ 
   | $$$$$$$  /$$__  $$|_  $$_/  | $$$$$ /$$__  $$ /$$__  $$| $$ /$$__  $$
   | $$__  $$| $$  \__/  | $$    | $$__/| $$  \ $$| $$  \__/| $$| $$$$$$$$
   | $$  \ $$| $$        | $$ /$$| $$   | $$  | $$| $$      | $$| $$_____/
   | $$$$$$$/| $$        |  $$$$/| $$   |  $$$$$$/| $$      | $$|  $$$$$$$
   |_______/ |__/         \___/  |__/    \______/ |__/      |__/ \_______/

	       [***] Welcome To Brute Force Attack Tools [***]
	           [+]---------------------------------[+]
	       [***]        By: Oseid Aldary             [***]
	           [+]---------------------------------[+]
	       [***]	           V: 2.1:               [***]
		   [*]---------------------------------[*]""")
	print(cor[5] + """\nExamples:
----------------
Emails:
----------------
./BrtForTe.py -F oseid@gmail.com -W /usr/share/wordlists/rockyou.txt   ::> this example [ Brute Force On [ FaceBoock Account ]]
./BrtForTe.py -I joker11         -L /usr/share/wordlists/rockyou.txt   ::> this example [ Brute Force On [ InstaGram Account ]]
./BrtForTe.py -T joker11         -C /usr/share/wordlists/rockyou.txt   ::> this example [ Brute Force On [ Twitter Account   ]]
./BrtForTe.py -G oseid@gmail.com -A /usr/share/wordlists/rockyou.txt   ::> this example [ Brute Force On [ Gmail Account     ]]

-p --use-proxy ::>  You can use this option for use [ Proxy ] with all emails options for bypass server Blooked :)
-----------------
SERVER:
-----------------
./BrtForTe.py -S 192.168.1.2  -U root -D /root/wordlist.txt  ::> this example [ Brute Force On [ SSH-SERVER    ]]
./BrtForTe.py -f 192.168.1.2  -E toor -K /root/wordlist.txt  ::> this example [ Brute Force On [ FTP-SERVER    ]]
------------------
HASH:
------------------
./BrtForTe.py -M 2095312189753de6ad47dfe20cbe97ec -m /root/wordlist.txt ::> this example [ Brute Force On [MD5 HASH]
./BrtForTe.py -Z aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d -z /root/list.txt ::> this example [ Brute Force On [SHA1 HASH]
./BrtForTe.py -Q ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193 -q /root/list.txt ::> this example [ Brute Force On [SHA224 HASH]
./BrtForTe.py -X 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 -x /root/wl.txt ::> this example [ Brute Force On [SHA256 HASH]
------------------
WEB:
------------------
./BrtForTe.py -N www.google.com [ -n for  Custom links] or Default Links and [-a] if you like using proxy whit scan :)
""")
