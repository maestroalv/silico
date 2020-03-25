#!/bin/usr/python
# coding:utf-8
# Ai Speech for help you open something

import os,sys,datetime
from time import sleep

class main:
	def __init__(self):
		self.main()
		
	def start():
		os.system('clear')
		print("""
		
   _   _       __                      _     
  /_\ (_)     / _\_ __   ___  ___  ___| |__  
 //_\\| |_____\ \| '_ \ / _ \/ _ \/ __| '_ \ 
/  _  \ |_____|\ \ |_) |  __/  __/ (__| | | |
\_/ \_/_|     \__/ .__/ \___|\___|\___|_| |_|
                 |_|                         
		""")
		print("[+] Membuka sesuatu dengan sekali ketik")
		while True:
			try:
				command=input('perintah : ')
				if 'open_yt' in command:
					sleep(1)
					print("[!] Membuka Youtube.......")
					sleep(1)
					os.system('xdg-open https://m.youtube.com/')
				if 'open_fb' in command:
					sleep(1)
					print("[!] Membuka Facebook......")
					os.system('xdg-open https://m.facebook.com/')
				if 'open_ig' in command:
					sleep(1)
					print("[!] Membuka Instagram.......")
					os.system('xdg-open https://www.instagram.com/')
				if 'open_tweet' in command:
					sleep(1)
					print("[!] Membuka Tweeter.......")
					os.system('xdg-open https://www.tweeter.com/')
				if 'open_wa' in command:
					sleep(1)
					print("[!] Membuka WA......")
					os.system('xdg-open https://api.whatsapp.com/send?phone=6285366745525&text=Hai+kk')
				if 'exit' in command:
					sleep(1)
					exit("[!] Keluar dari program!")
				else:
					sleep(1)
					print("Saya hanya mengerti beberapa perinta berikut:\n\n > open_yt      ---| Untuk membuka Youtube\n > open_fb     ---| Untuk membuka Facebook\n > open_ig     ---| Untuk membuka Instagram\n > open_tweet     ---| Untuk membuka Tweeter\n > open_wa     ---| Untuk membuka WhatsApp\n > exit     | Untuk keluar")
					sleep(1)
			except KeyboardInterrupt: exit()
			
main.start()