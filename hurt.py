#!/bin/usr/python3.8.x
# •_• coding:utf-8 •_•
# Hurt ToolKit v1.0.1 (Testing Hacking)

#----------------------------------------------------------------------------#
try:
	import os,sys,random,smtplib,requests
	from Banner import __server__
	from datetime import datetime as date
	from time import sleep
	from prompt_toolkit import prompt
except Exception as ER:
	exit("[ModuleNotFound] %s"%(ER))

longentod="Mau ngapain lo?";asu="Gada kerjaan ya?";kontop="Gaguna Lo sumpah";server_username='serverhurttoolkit@gmail.com';server_password='motherfucker<404>'

class other:
	def __init__(self):
		self.other()
		
	dats=date.now()
	_hour=int(date.now().hour)
	_minute=int(date.now().minute)
	_second=int(date.now().second)
	_day=int(date.now().day)
	_month=int(date.now().month)
	_year=int(date.now().year)
	clear='clear'
		
	def clearScreen():
		os.system(other.clear)
	
class Main:
	def __init__(self):
		self.Main()
	
	def menu():
		other.clearScreen()
		link="https://api.myip.com/"
		re=requests.get(link)
		myip=re.json()['ip']
		try:
			nma=open('Data/nama').read()
			__server__.Logo_utama()
			print()
			print("[+] My IP  : %s"%(myip))
			print("[+] Nama   : %s"%(nma))
			print("""
	1. Ai Speech
	2. Tombol Tambahan Termux
	44. Cek Update
	77. Contact Author
	99. Hapus akun
	00. Keluar
			""")
			while True:
				try:
					pilih=input("     hurt > ")
					if pilih=="":
						sleep(1)
						print("[!] Jangan kosong kak")
					elif '1' in pilih:
						sleep(2)
						os.system('python files/ai/start.py')
					elif '2' in pilih:
						sleep(2)
						os.system('python files/key/start.py')
					elif '77' in pilih:
						other.clearScreen()
						print("""
[!] Contact Author:
                    1. Facebook
                    2. Email
                    3. Kembali
                    4. Keluar
						""")
						tanya_cnt=input("      hurt/contact > ")
						if '1' in tanya_cnt:
							os.system('xdg-open https://m.facebook.com/leon101.coder')
							Main.menu()
						elif '2' in tanya_cnt:
							print("Email > mrleeon404@gmail.com")
							input("Press enter untuk kembali......")
							Main.menu()
						elif '3' in tanya_cnt:
							sleep(2)
						elif '4' in tanya_cnt:
							sleep(1)
							exit("[!] Keluar dari Program!")
					elif '44' in pilih:
						link_update="https://serverhurttoolkit.000webhostapp.com/update.txt"
						c_cekup=requests.get(link_update).text
						if 'tidak perlu update' in c_cekup:
							print("[!] Udate belum tersedia!")
						if 'Perlu update' in c_cekup:
							print("[!] Update tersedia")
					elif '00' in pilih:
						sleep(1)
						exit("[!] Keluar dari program")
					elif '99' in pilih:
						sleep(1)
						other.clearScreen()
						yakin=input("[  Anda yakin ingin menghapus akun? [y/n] ")
						if 'y' in yakin:
							sleep(1)
							print("[!] Loading.....")
							sleep(3)
							os.system('rm -rf Data/nama')
							os.system('rm -rf Data/username')
							os.system('rm -rf Data/password')
							os.system('rm -rf Data/email')
							print("[✓] Berhasil menghapus akun")
							exit()
						elif 'n' in yakin:
							print("Membatalkan....")
							exit()
						else: exit()
					else:
						sleep(1)
						print("[!] Pilihan kk tidak ada :'(")
				except KeyboardInterrupt: exit()
			
		except IOError:
			exit("[!] Terjadi Kesalahan")
		
	def tanya():
		other.clearScreen()
		sleep(2)
		__server__.Logo_utama()
		print()
		print("Date : %s-%s-%s | %s.%s.%s"%(other._day,other._month,other._year,other._hour,other._minute,other._second))
		print("""\033[41;1;97m[Perhatian] >\033[0m Jika belum mempunyai akun Silahkan Daftar!

	1. Masuk
	2. Daftar
	3. Keluar
		""")
		while True:
			try:
				lay=input("[?] Pilih Angka : ")
				if lay=="":
					sleep(1)
					print("[!] Jangan Kosong")
				elif '1' in lay:
					sleep(1)
					login.masuk()
				elif '2' in lay:
					sleep(1)
					login.daftar()
				elif '3' in lay:
					sleep(1)
					exit("[!] Keluar dari program!")
				else:
					sleep(1)
					print("[!] Pilihan anda tidak ada!")
			except KeyboardInterrupt: exit()
			
class login:
	def __init__(self):
		self.login()
		
	def daftar():
		other.clearScreen()
		__server__.Logo_daftar()
		print("Date : %s-%s-%s | %s.%s.%s"%(other._day,other._month,other._year,other._hour,other._minute,other._second))
		print("[+] Silahkan buat akun anda untuk menggunakan Tool ini")
		print()
		nama=input("[?] Nama : ")
		username=input("[?] Username : ")
		password=prompt("[?] Password : ",is_password=True)
		re_password=prompt("[?] RePassword : ",is_password=True)
		email=input("[?] Email : ")
		sleep(2)
		if nama=="":
			exit("Nama Tidak Boleh Kosong")
		if username=="":
			exit("Username wajib di isi")
		if (len(username)) < 6:
			exit("Username minimal 6 digit")
		if password=="":
			exit("Password wajib di isi")
		if (len(password)) < 6:
			exit("Password minimal 6 digit")
		if re_password not in password:
			exit("Password tidak sesuai")
		if email=="":
			exit("Email tidak di isi")
		pass
		print("Loading....")
		sleep(2)
		data=username+password
		hurtmail="hurtsec404@gmail.com"
		datas=username+email+password
		kode = random.randint(110119,943184)
		SUBJECT="Hurt ToolKit"
		TEXT="Hai %s\n\nCode Verifikasi Akun Hurt ToolKit anda adalah : %s\n\n\nSalam hangat:\n-LeON"%(nama,kode)
		pesan='Subject: {}\n\n{}'.format(SUBJECT,TEXT)
		smtp_server=smtplib.SMTP('smtp.gmail.com',587)
		smtp_server.ehlo()
		smtp_server.starttls()
		smtp_server.login(server_username,server_password)
		smtp_server.sendmail(hurtmail,email,pesan)
		while True:
			try:
				sleep(2)
				print("[!] Silahkan Cek email anda, lihat code 6 digit anda")
				very=input("[!] Code Verifikasi : ")
				if very == (str(kode)):
					sleep(2)
					print("[✓] Verifikasi berhasil.....")
					sleep(1)
					usr=open('Data/username','w')
					usr.write(username)
					usr.close()
					pas=open('Data/password','w')
					pas.write(password)
					pas.close()
					eml=open('Data/email','w')
					eml.write(email)
					eml.close()
					nma=open('Data/nama','w')
					nma.write(nama)
					nma.close()
					exit("")
				else:
					sleep(2)
					print("[!] Code Verifikasi anda salah!")
			except KeyboardInterrupt: exit()
		
	def masuk():
		other.clearScreen()
		__server__.Logo_masuk()
		print("Date : %s-%s-%s | %s.%s.%s"%(other._day,other._month,other._year,other._hour,other._minute,other._second))
		try:
			usra=open('Data/username').read()
			pasd=open('Data/password').read()
			emla=open('Data/email').read()
			myusr=usra
			mymail=emla
			mypas=pasd
		except IOError:
			exit("Terjadi Kesalahan")
		print("[+] Silahkan masuk dengan akun yang sudah terdaftar")
		print()
		uname=input("[?] Email/Username : ")
		if usra in uname or emla in uname:
			sleep(1)
			pwd=prompt("[?] Password : ",is_password=True)
			if pasd in pwd:
				sleep(1)
				print("[!] Sedang masuk....")
				sleep(2)
				Main.menu()
			else:
				sleep(2)
				exit("[!] Password Salah")
		else:
			sleep(2)
			exit("[!] Username Salah")
			
if __name__=='__main__':
	try:
		update="https://serverhurttoolkit.000webhostapp.com/update.txt"
		cekup=requests.get(update).text
		if 'tidak perlu update' in cekup:
			Main.tanya()
		elif 'Perlu update' in cekup:
			tanya_upd=input("[!] Update tersedia\n    Update ke versi terbaru? [y/n] : ")
			if 'y' in tanya_upd:
				print("\n[!] Loading.......")
				sleep(2)
				os.system('cd; rm-rf Hurt; git clone https://github.com/LeON101-coder/Hurt.git; cd Hurt')
				exit("[!] Udate selesai")
			else:
				Main.tanya()
	except KeyboardInterrupt: exit()