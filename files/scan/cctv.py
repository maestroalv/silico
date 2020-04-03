#!/bin/usr/python3.8.x
# coding:utf-8
# Scan CCTV

import os,sys,requests,re
from time import sleep

def logo():
	print("""
\033[1;97m|\033[1;96m------------------------------------\033[1;97m|
\033[1;90m		____
	   _[]_/____\__n_
	  |_____.--.__()_|
	  |   //# \\      | 
	  |   \\__//      |
	  |    '--'      |
	  |______________|
\033[1;97m|\033[1;96m------------------------------------\033[1;97m|
 \033[47;1;91m         Coded By : Aqnes           \033[0m
	""")

class main:
	def __init__(self):
		self.scan()
		
	def scan(self):
		os.system('clear')
		logo()
		print("\033[1;91m•\033[1;92m Select a Country ")
		print("""
   \033[1;97m{\033[1;96m01\033[1;97m}\033[1;91m----\033[1;97mIndonesian
   \033[1;97m{\033[1;96m02\033[1;97m}\033[1;91m----\033[1;97mJapan
   \033[1;97m{\033[1;96m03\033[1;97m}\033[1;91m----\033[1;97mAmerican
   \033[1;97m{\033[1;96m04\033[1;97m}\033[1;91m----\033[1;97mItaly
   \033[1;97m{\033[1;96m05\033[1;97m}\033[1;91m----\033[1;97mFrance
   \033[1;97m{\033[1;96m00\033[1;97m}\033[1;91m----\033[1;97mBack to main menu
   \033[1;97m{\033[1;96mx\033[1;97m}\033[1;91m-----\033[1;97mExit
		""")
		choose=input("   \033[1;97mhurt/\033[1;92mscan\033[1;97m >\033[1;90m ")
		if choose in ['1','01']:
			sleep(1)
			scan.ind()
		else:
			sleep(1)
			print("\033[1;91m[!]\033[1;97m Your choose not found")
			input("press enter to menu.....…")
			main()

class scan:
	def ind():
		os.system('clear')
		logo = """
		
		"""
		print(logo)
		usragnt = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		global page
		url = requests.get('https://www.insecam.org/en/bycountry/ID/', headers=usragnt)
		chg=re.findall('"?page=",\s\d+', url.text)[1]
		find=chg.replace('page='', ', '')
		print("\033[1;97m[\033]1;92m > \033[1;91m Total list page \033[1;97m:\033[1;92m %s"%(find))
		print()
		print("\033[1;91m•\033[1;92m In all ip Vuln:")
		try:
			page = "9"
			ulrs= ("https://www.insecam.org/en/bycountry/ID/?page="+str(page))
			print()
			ack=requests.get(urls, headers=usragnt)
			ip = re.findall('http://\d+.\d+.\d+.\d+:\d+', ack.text)
			count = 1
			for notbad in ip:
				total = notbad[count]
				print("\033[1;97m%s. \033[1;92m  "%(total))
				count +=1
			print("\033[1;92m[✓] \033[1;97m Done!")
			input("\033[0mPress enter to menu")
			main()
		except KeyboardInterrupt: sys.exit()
		
main()