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
./BrtForTe.py -M <multi hash> you can set any hash from this hashes>[ MD5,SHA1,SHA224,SHA256,SHA384,SHA512 ]

#MD5
./BrtForTe.py -M 5d41402abc4b2a76b9719d911017c592 -m /root/wordlist.txt

------------------
WEB:
------------------
./BrtForTe.py -N www.google.com

[-n] if you like set Custom links file
and [-a] if you like use proxy whit scan :)

./BrtForTe.py -N www.google.com -n /root/links.txt -a
""")
