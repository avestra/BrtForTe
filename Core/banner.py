# coding: utf-8
#!/usr/bin/python

from random import randint

cor = ['\033[95m', '\033[96m', '\033[92m','\033[93m','\033[91m','\033[0m']
colors = cor[randint(0,5)]
def banner():
    banner0 = colors + """
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
               [***]               V: 2.1:               [***]
                   [*]---------------------------------[*]
                                                                        
"""


    banner1 = colors + """
  ____       _   ______      _______                  
 |  _ \     | | |  ____|    |__   __|                 
 | |_) |_ __| |_| |__ ___  _ __| | ___                
 |  _ <| '__| __|  __/ _ \| '__| |/ _ \               
 | |_) | |  | |_| | | (_) | |  | |  __/               
 |____/|_|   \__|_|  \___/|_|  |_|\___|               
                                       v 2.1                        
                                                                
"""

    banner2 = colors + """
 ____   ____  ______  _____   ___   ____  ______    ___ 
|    \ |    \|      ||     | /   \ |    \|      |  /  _]
|  o  )|  D  )      ||   __||     ||  D  )      | /  [_ 
|     ||    /|_|  |_||  |_  |  O  ||    /|_|  |_||    _]
|  O  ||    \  |  |  |   _] |     ||    \  |  |  |   [_ 
|     ||  .  \ |  |  |  |   |     ||  .  \ |  |  |     |
|_____||__|\_| |__|  |__|    \___/ |__|\_| |__|  |_____|       
-------------------------------------------------------------------
[+>]====>> By: oseid Aldary <<====[-]====>> Version: 2.1 <<====[<+]
-------------------------------------------------------------------                                   
"""

    banner3 = colors + """
										
 ██████╗ ██████╗ ████████╗███████╗ ██████╗ ██████╗ ████████╗███████╗		
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝		
██████╔╝██████╔╝   ██║   █████╗  ██║   ██║██████╔╝   ██║   █████╗  		
██╔══██╗██╔══██╗   ██║   ██╔══╝  ██║   ██║██╔══██╗   ██║   ██╔══╝  		
██████╔╝██║  ██║   ██║   ██║     ╚██████╔╝██║  ██║   ██║   ███████╗		
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
-------------------------------------------------------------------
[+>]====>> By: oseid Aldary <<====[-]====>> Version: 2.1 <<====[<+]
-------------------------------------------------------------------		
                                                                   		
"""



    banner4 = colors + """
   ___      _     ___         _____     
  / __\_ __| |_  / __\__  _ _/__   \___                 
 /__\// '__| __|/ _\/ _ \| '__|/ /\/ _ \                
/ \/  \ |  | |_/ / | (_) | |  / / |  __/                
\_____/_|   \__\/   \___/|_|  \/   \___| 
				        V 2.1
[---] By: Oseid Aldary [---]
               
                                                        
"""
    banner5 = colors + """
 ______   _______ _________ _______  _______  _______ _________ _______           
(  ___ \ (  ____ )\__   __/(  ____ \(  ___  )(  ____ )\__   __/(  ____ \          
| (   ) )| (    )|   ) (   | (    \/| (   ) || (    )|   ) (   | (    \/          
| (__/ / | (____)|   | |   | (__    | |   | || (____)|   | |   | (__              
|  __ (  |     __)   | |   |  __)   | |   | ||     __)   | |   |  __)             
| (  \ \ | (\ (      | |   | (      | |   | || (\ (      | |   | (                
| )___) )| ) \ \__   | |   | )      | (___) || ) \ \__   | |   | (____/\          
|/ \___/ |/   \__/   )_(   |/       (_______)|/   \__/   )_(   (_______/
------------------------------------------------------------------------
[+>] =====>> By: oseid Aldary <<====[--]=====>> Version: 2.1 <<==== [<+]
------------------------------------------------------------------------

"""

    banner6 = colors + """
							
________       _______________            ________     	
___  __ )________  /___  ____/_______________  __/____ 	
__  __  |_  ___/  __/_  /_   _  __ \_  ___/_  /  _  _ \	
_  /_/ /_  /   / /_ _  __/   / /_/ /  /   _  /   /  __/	
/_____/ /_/    \__/ /_/      \____//_/    /_/    \___/ 	
                                                     V 2.1
                                                      	
"""

    banners = [banner0, banner1, banner2, banner3, banner4, banner5, banner6]
    print banners[randint(0,6)]


