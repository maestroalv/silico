#!/bin/usr/python3.8.x
# coding:utf-8
# Home Page Termux
# Recode aku sayang

import os,sys
from time import sleep

class main:
	def __init__(self):
		self.start()
		
	def start(self):
		os.system('clear')
		print("\033[1;91m• \033[1;97mChange your Home Page Termux")
		print("\033[1;97m[\033[1;92m+\033[1;97m]\033[1;96m Choose You theme")
		print("""
	\033[1;97m{\033[1;96m01\033[1;97m}\033[1;91m---\033[1;97mKali
	\033[1;97m{\033[1;96m02\033[1;97m}\033[1;91m---\033[1;97mParrot
	\033[1;97m{\033[1;96m03\033[1;97m}\033[1;91m---\033[1;97mWindows7
	\033[1;97m{\033[1;96m04\033[1;97m}\033[1;91m---\033[1;97mWindows10
	\033[1;97m{\033[1;96m05\033[1;97m}\033[1;91m---\033[1;97mUbuntu
	\033[1;97m{\033[1;96m06\033[1;97m}\033[1;91m---\033[1;97mArch
	\033[1;97m{\033[1;96m07\033[1;97m}\033[1;91m---\033[1;97mDebian
	\033[1;97m{\033[1;96m00\033[1;97m}\033[1;91m---\033[1;91mBack to main menu
		""")
		choose=input("    \033[1;97mhurt/\033[1;92mhome-page \033[1;97m>\033[1;90m ")
		if choose in ['1','01']:
			theme.kali()
		elif choose in ['2','02']:
			theme.parrot()
		elif choose in ['3','03']:
			theme.win7()
		elif choose in ['4','04']:
			theme.win10()
		elif choose in ['5','05']:
			theme.ubuntu()
		elif choose in ['6','06']:
			theme.arch()
		elif choose in ['7','07']:
			theme.debian()
		elif choose in ['0','00']:
			os.system('python hurt.py')
		else:
			print("\033[1;91mYour choose not found!")
			sleep(2)
			main()
			
class theme:
	def kali():
		print("\033[1;91m+ \033[1;92mEnter your name terminal")
		name_terminal=input("\033[1;97m[\033[1;93m?\033[1;97m]\033[1;96m Name Terminal \033[1;97m:\033[1;92m ")
		create_bashrc=open('files/home-page/bash.bashrc','w')
		create_bashrc.write("""
command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[01;31m\]root\[\033[01;39m@\]\[\033[01;31m\]"""+name_terminal+"""\[\033[01;39m\]/\[\033[01;32m\]${PWD/*\//}\[\033[01;39m\] :~#\[\033[01;30m\] '

clear
neofetch --ascii_distro kali

		""")
		create_bashrc.close()
		sleep(2)
		os.system('sh files/home-page/tes.sh')
		print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;92m Finish!, Close u Termux and open again");sleep(2)
		os.system('python hurt.py')
	
	
	def parrot():
		print("\033[1;91m+ \033[1;92mEnter your name terminal")
		name_terminal=input("\033[1;97m[\033[1;93m?\033[1;97m]\033[1;96m Name Terminal \033[1;97m:\033[1;92m ")
		create_bashrc=open('files/home-page/bash.bashrc','w')
		create_bashrc.write("""
command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[01;31m\]root\[\033[01;39m@\]\[\033[01;31m\]"""+name_terminal+"""\[\033[01;39m\]/\[\033[01;32m\]${PWD/*\//}\[\033[01;39m\] :~#\[\033[01;30m\] '

clear
neofetch --ascii_distro Parrot

		""")
		create_bashrc.close()
		sleep(2)
		os.system('sh files/home-page/tes.sh')
		print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;92m Finish!, Close u Termux and open again");sleep(2)
		os.system('python hurt.py')
		
	def win7():
		print("\033[1;91m+ \033[1;92mEnter your name terminal")
		name_terminal=input("\033[1;97m[\033[1;93m?\033[1;97m]\033[1;96m Name Terminal \033[1;97m:\033[1;92m ")
		create_bashrc=open('files/home-page/bash.bashrc','w')
		create_bashrc.write("""
command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[01;31m\]root\[\033[01;39m@\]\[\033[01;31m\]"""+name_terminal+"""\[\033[01;39m\]/\[\033[01;32m\]${PWD/*\//}\[\033[01;39m\] :~#\[\033[01;30m\] '

clear
neofetch --ascii_distro Windows7

		""")
		create_bashrc.close()
		sleep(2)
		os.system('sh files/home-page/tes.sh')
		print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;92m Finish!, Close u Termux and open again");sleep(2)
		os.system('python hurt.py')
		
		
	def win10():
		print("\033[1;91m+ \033[1;92mEnter your name terminal")
		name_terminal=input("\033[1;97m[\033[1;93m?\033[1;97m]\033[1;96m Name Terminal \033[1;97m:\033[1;92m ")
		create_bashrc=open('files/home-page/bash.bashrc','w')
		create_bashrc.write("""
command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[01;31m\]root\[\033[01;39m@\]\[\033[01;31m\]"""+name_terminal+"""\[\033[01;39m\]/\[\033[01;32m\]${PWD/*\//}\[\033[01;39m\] :~#\[\033[01;30m\] '

clear
neofetch --ascii_distro Windows10

		""")
		create_bashrc.close()
		sleep(2)
		os.system('sh files/home-page/tes.sh')
		print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;92m Finish!, Close u Termux and open again");sleep(2)
		os.system('python hurt.py')
		
	def ubuntu():
		print("\033[1;91m+ \033[1;92mEnter your name terminal")
		name_terminal=input("\033[1;97m[\033[1;93m?\033[1;97m]\033[1;96m Name Terminal \033[1;97m:\033[1;92m ")
		create_bashrc=open('files/home-page/bash.bashrc','w')
		create_bashrc.write("""
command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[01;31m\]root\[\033[01;39m@\]\[\033[01;31m\]"""+name_terminal+"""\[\033[01;39m\]/\[\033[01;32m\]${PWD/*\//}\[\033[01;39m\] :~#\[\033[01;30m\] '

clear
neofetch --ascii_distro Ubuntu

		""")
		create_bashrc.close()
		sleep(2)
		os.system('sh files/home-page/tes.sh')
		print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;92m Finish!, Close u Termux and open again");sleep(2)
		os.system('python hurt.py')
		
	def arch():
		print("\033[1;91m+ \033[1;92mEnter your name terminal")
		name_terminal=input("\033[1;97m[\033[1;93m?\033[1;97m]\033[1;96m Name Terminal \033[1;97m:\033[1;92m ")
		create_bashrc=open('files/home-page/bash.bashrc','w')
		create_bashrc.write("""
command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[01;31m\]root\[\033[01;39m@\]\[\033[01;31m\]"""+name_terminal+"""\[\033[01;39m\]/\[\033[01;32m\]${PWD/*\//}\[\033[01;39m\] :~#\[\033[01;30m\] '

clear
neofetch --ascii_distro Arch

		""")
		create_bashrc.close()
		sleep(2)
		os.system('sh files/home-page/tes.sh')
		print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;92m Finish!, Close u Termux and open again");sleep(2)
		os.system('python hurt.py')
		
	def debian():
		print("\033[1;91m+ \033[1;92mEnter your name terminal")
		name_terminal=input("\033[1;97m[\033[1;93m?\033[1;97m]\033[1;96m Name Terminal \033[1;97m:\033[1;92m ")
		create_bashrc=open('files/home-page/bash.bashrc','w')
		create_bashrc.write("""
command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[01;31m\]root\[\033[01;39m@\]\[\033[01;31m\]"""+name_terminal+"""\[\033[01;39m\]/\[\033[01;32m\]${PWD/*\//}\[\033[01;39m\] :~#\[\033[01;30m\] '

clear
neofetch --ascii_distro Debian

		""")
		create_bashrc.close()
		sleep(2)
		os.system('sh files/home-page/tes.sh')
		print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;92m Finish!, Close u Termux and open again");sleep(2)
		os.system('python hurt.py')
		

main()