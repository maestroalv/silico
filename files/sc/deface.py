#!/bin/usr/python3.8.x
# coding=utf-8
# Create Shell Deface

import os,sys
from time import sleep
try:
	from tqdm import tqdm
except:
	os.system('pip install tqdm')

def logo():
	print("""
\033[1;97m|\033[1;96m------------\033[1;93m__Create__\033[1;96m-------------\033[1;97m|
\033[1;91m ╔═╗\033[1;90m┬ ┬┌─┐┬  ┬    \033[1;91m╔╦╗\033[1;90m┌─┐┌─┐┌─┐┌─┐┌─┐
\033[1;91m ╚═╗\033[1;90m├─┤├┤ │  │    \033[1;91m ║║\033[1;90m├┤ ├┤ ├─┤│  ├┤ 
\033[1;91m ╚═╝\033[1;90m┴ ┴└─┘┴─┘┴─┘  \033[1;91m═╩╝\033[1;90m└─┘└  ┴ ┴└─┘└─┘
\033[1;97m|\033[1;96m-----------------------------------\033[1;97m|
 \033[47;1;91m     Coded by : {}F4K3#R00t{}      \033[0m
	""")

class Main:
	def __init__(self):
		self.ask()
		
	def ask(self):
		os.system('clear')
		logo()
		print("""
     \033[1;97m{\033[1;96m01\033[1;97m}\033[1;91m---\033[1;97mShell Deface Personal
     \033[1;97m{\033[1;96m02\033[1;97m}\033[1;91m---\033[1;97mShell Deface For Team
     \033[1;97m{\033[1;96m00\033[1;97m}\033[1;91m---\033[1;97mBack to main menu
     \033[1;97m{\033[1;96mx\033[1;97m}\033[1;91m----Exit from programs
		""")
		choose=input("     \033[1;97mhurt/\033[1;92mscdeface \033[1;97m>\033[1;90m ")
		if choose in ['1','01']:
			sleep(1)
			create.personal()
		elif choose in ['2','02']:
			sleep(1)
			create.team()
		elif choose in ['0','00']:
			sleep(1)
			os.system('python hurt.py')
		elif 'x' in choose:
			sleep(1)
			exit("\033[1;91mExit from programs!")
		else:
			print("\033[1;91m[!]\033[1;97m Please enter a number...")
			input("press enter...")
			Main()

class create:
	def personal():
		try:
			os.system('clear')
			logo()
			print("\033[1;91m•\033[1;92m Fill in the document below to create Your Shell Deface")
			print()
			title=input("\033[1;97m[\033[1;93m+\033[1;97m]\033[1;97m Title :\033[1;92m ")
			head=input("\033[1;97m[\033[1;93m+\033[1;97m]\033[1;97m Hacked by : \033[1;92m")
			image=input("\033[1;97m[\033[1;93m+\033[1;97m] Link Image (your photo) :\033[1;92m ")
			background=input("\033[1;97m[\033[1;93m+\033[1;97m] Link Background image :\033[1;92m ")
			print("\033[1;91m•\033[1;97m Type <br> for next text")
			message=input("\033[1;97m[\033[1;93m+\033[1;97m] Your Message :\033[1;92m ")
			sleep(1)
			print("\033[1;91m[!]\033[1;97m Loading....")
			sleep(5)
			a="""<html>"""
			b="""<head>"""
			c="""<title> """+title+"""</title>"""
			d="""</head>"""
			e="""<body background="""+background+""">"""
			f="""<marquee><font color="red" face="arial" size="5"> You Has been Hacked by : """+head+"""</marquee></font>"""
			g="""<center><font color="red" face="arial" size="6"> Hacked by : """+head+"""</font></center>"""
			h="""<center><img src="""+image+""" width=250px height=250px>"""
			i="""<center><font color="blue" face="arial" size="4">"""+message+"""</font></center>"""
			j="""</body>"""
			k="""</html>"""
			print("\033[0m Create Loading....")
			for load in tqdm(range(100)):
				sleep(0.1)
				pass
			print(load)
			sleep(1)
			crt=open('files/sc/shell/index.html','w')
			crt.write(a)
			crt.write(b)
			crt.write(c)
			crt.write(d)
			crt.write(e)
			crt.write(f)
			crt.write(g)
			crt.write(h)
			crt.write(i)
			crt.write(j)
			crt.write(k)
			crt.close()
			print("done")
			print()
			sleep(1)
			print("\033[1;97m[\033[1;91m+\033[1;97m]\033[1;96m File saved :\033[1;92m files/sc/shell/index.html")
			input("[enter]")
			Main()
		except (KeyboardInterrupt, EOFError):
			exit()
	
	def team():
		try:
			os.system('clear')
			logo()
			print("\033[1;91m•\033[1;92m Fill in the document below to create Your Shell Deface")
			print()
			title=input("\033[1;97m[\033[1;93m+\033[1;97m]\033[1;97m Title :\033[1;92m ")
			head=input("\033[1;97m[\033[1;93m+\033[1;97m]\033[1;97m Hacked by : \033[1;92m")
			image=input("\033[1;97m[\033[1;93m+\033[1;97m] Link Image (your photo) :\033[1;92m ")
			background=input("\033[1;97m[\033[1;93m+\033[1;97m] Link Background image :\033[1;92m ")
			print("\033[1;91m•\033[1;97m Type <br> for next text")
			message=input("\033[1;97m[\033[1;93m+\033[1;97m] Your Message :\033[1;92m ")
			thanks=input("\033[1;97m[\033[1;93m+\033[1;97m] Thanks To :\033[1;92m ")
			sleep(1)
			print("\033[1;91m[!]\033[1;97m Loading....")
			sleep(5)
			a="""<html>"""
			b="""<head>"""
			c="""<title> """+title+"""</title>"""
			d="""</head>"""
			e="""<body background="""+background+""">"""
			f="""<marquee><font color="red" face="arial" size="5"> You Has been Hacked by : """+head+"""</marquee></font>"""
			g="""<center><font color="red" face="arial" size="6"> Hacked by : """+head+"""</font></center>"""
			h="""<center><img src="""+image+""" width=250px height=250px>"""
			i="""<center><font color="blue" face="arial" size="4">"""+message+"""</font></center>"""
			x="""<marquee>Thanks to : """+thanks+"""</marquee>"""
			j="""</body>"""
			k="""</html>"""
			print("\033[0m Create Loading....")
			for load in tqdm(range(100)):
				sleep(0.1)
				pass
			print(load)
			sleep(1)
			crt=open('files/sc/shell/index.html','w')
			crt.write(a)
			crt.write(b)
			crt.write(c)
			crt.write(d)
			crt.write(e)
			crt.write(f)
			crt.write(g)
			crt.write(h)
			crt.write(i)
			crt.write(j)
			crt.write(k)
			crt.write(x)
			crt.close()
			print("done")
			print()
			sleep(1)
			print("\033[1;97m[\033[1;91m+\033[1;97m]\033[1;96m File saved :\033[1;92m files/sc/shell/index.html")
			input("[enter]")
			Main()
		except (KeyboardInterrupt, EOFError):
			exit()

Main()