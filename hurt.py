#!/bin/usr/python3.8.x
# coding:utf-8
# Hurt Toolkit v1.0.2 (Update)

try:
	import os,sys,json
	from time import sleep
except Exception as module:
	exit("[ModuleNotFound] > %s"%(module))

def logo():
	print("""\033[1;97mWelcome to Hurt Toolkit!
	
\033[1;91m*\033[1;92m Author:\033[1;96m   LeON
\033[1;91m*\033[1;92m Support:  \033[1;96mAqnes \033[1;97m|\033[1;96m Indonesian Hurt Security \033[1;97m|\033[1;96m ./F4K3 \033[1;97m|\033[1;96m \033[1;97m{\033[1;96m\033[1;97m}\033[1;91mF4K3#R00t\033[1;97m{\033[1;96m\033[1;97m}\033[1;91m
\033[1;91m*\033[1;92m Version:  \033[1;90m1.0.2
\033[1;91m*\033[1;92m Github:   \033[47;1;91mhttps://github.com/LeON101-coder\033[0m

		\033[1;90mdb   db db    db d8888b. d888888b
		88   88 88    88 88  `8D `~~88~~'
		88ooo88 88    88 88oobY'    88
		88~~~88 88    88 88`8b      88
		88   88 88b  d88 88 `88.    88
		YP   YP ~Y8888P' 88   YD    YP\033[0m""")

class Main:
	def __init__(self):
		self.start()
		
	def start(self):
		os.system('clear')
		self.arg()
		
	def arg(self):
		logo()
		print("""
    \033[1;97m{\033[1;96m01\033[1;97m}\033[1;91m---\033[1;97mChange Home Page
    \033[1;97m{\033[1;96m02\033[1;97m}\033[1;91m---\033[1;97mDistributed Denial of Service
    \033[1;97m{\033[1;96m03\033[1;97m}\033[1;91m---\033[1;97mScan Vuln CCTV
    \033[1;97m{\033[1;96m04\033[1;97m}\033[1;91m---\033[1;97mCreate Shell Deface
    \033[1;97m{\033[1;96m05\033[1;97m}\033[1;91m---\033[1;97mMass Deface
    \033[1;97m{\033[1;96m00\033[1;97m}\033[1;91m---\033[1;91mExit
		""")
		while True:
			try:
				choose=input("    \033[1;97mhurt >\033[1;90m ")
				if choose in ['1','01']:
					sleep(1)
					try:
						import figlet
					except ImportError:
						os.system('pkg install neofetch -y')
					os.system('python files/home-page/change.py')
				elif choose in ['2','02']:
					sleep(1)
					os.system('python files/ddos/attack.py')
					sys.exit()
				elif choose in ['3','03']:
					sleep(1)
					os.system('python files/scan/cctv.py')
					sys.exit()
				elif choose in ['0','00']:
					sleep(1)
					exit("\033[1;91m[!]\033[1;97m Exit from programs")
					sys.exit()
				else:
					sleep(1)
					print("\033[1;91m[!] \033[1;97mWrong input")
			except EOFError: sys.exit()
			except KeyboardInterrupt: sys.exit()
		
Main()