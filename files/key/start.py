#!/bin/usr/python3.7.x
# coding:utf-8
# Key Tambahan Termux

import os
from time import sleep

def mulai():
	os.system('clear')
	print("[!] Memasang Key tambahan Termux")
	try:
		os.mkdir('/data/data/com.termux/files/home/.termux')
	except:
		pass
		sleep(2)
		print("[!] Loading.....")
		sleep(1)
		key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
		pasang = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
		pasang.write(key)
		pasang.close()
		os.system('termux-reload-settings')
		print("[!] Selesai!")
		
	
mulai()
