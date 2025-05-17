import os
import subprocess

nmap = """
# Nmap 7.94 scan initiated Sat May 17 21:30:22 2025 as: nmap -sS -sV -p- -T4 -Pn voteportal.gov
Nmap scan report for voteportal.gov (10.0.0.10)
Host is up (0.012s latency).
Not shown: 65529 closed ports

PORT     STATE SERVICE    VERSION
80/tcp   open  http       
443/tcp  open  ssl/http   Apache httpd 2.4.41 ((Ubuntu))
3306/tcp open  mysql      MySQL 5.7.29
8080/tcp open  http-proxy nginx 1.18.0

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
"""

cikti = """
/login.php
/admin/
/admin/upload.php
/config.php.bak
"""

msf = """
exploit/multi/http/tomcat_mgr_upload
exploit/multi/http/struts2_content_type_ognl
exploit/windows/smb/ms17_010_eternalblue
exploit/linux/smtp/exim_rce
exploit/multi/http/git_config_traversal
exploit/linux/mysql/mysql_udf_payload
auxiliary/scanner/http/gobuster_like
exploit/unix/webapp/wp_admin_shell_upload
exploit/windows/http/iis_webdav_scstoragepathfromurl
exploit/multi/http/drupal_drupalgeddon2
exploit/windows/http/printnightmare_rce
exploit/linux/http/apache_mod_cgi_bash_env_exec
auxiliary/scanner/ftp/anonymous
exploit/windows/http/joomla_com_fields_sqli_rce
exploit/multi/http/laravel_rce_log_poison
exploit/windows/local/token_impersonation_priv_esc
exploit/multi/http/symfony_var_dump_rce
exploit/multi/http/tika_server_injection
"""

kgb = '''
[!] KGB DOSYASI:
(İçeriği uzun olduğu için buraya kısaca yazıldı)
'''

dosyalar = '''
1.png
2.png
3.png
4.png
5.png
6.png
7.png
8.png
9.png
'''

zafiyet = '''
# unicode_fuzz.py
for i in range(0x10000, 0x110000):
    try:
        payload = chr(i) * 600
        proc = subprocess.run(["./unicode_filterd"], input=payload.encode('utf-8'), capture_output=True, timeout=1)
        if b"Segmentation fault" in proc.stderr:
            print(f"[!] Crash at {hex(i)} char -> Offset suspected!")
    except:
        continue
'''

ex = '''
b"\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80",  # execve /bin/sh
b"\\x90\\x90\\x90\\x90"
'''

while True:
    yazi = input("welcome.apt: ").strip()

    if "nmap" in yazi:
        print(nmap)
    elif "http://10.0.10.0" in yazi:
        print("bi halt yok")
    elif "gobuster dir" in yazi:
        print(cikti)
    elif "gobuster" in yazi:
        print('[Mail Server] - smtp.voteportal.gov (10.0.0.11)')
    elif "/login.php" in yazi:
        print("welcome to login")
    elif "/admin/upload" in yazi:
        print("forbidden")
    elif "/admin/" in yazi:
        print("forbidden")
    elif "/config.php.bak" in yazi:
        print("mysql:Apache Tika-server < 1.18")
    elif "msf" == yazi:
        print(msf)
    elif "use exploit/multi/http/tika_server_injection" in yazi:
        while True:
            yazi2 = input("msf> ").strip()

            if "exit" in yazi2:
                print("msf modundan çıkılıyor...")
                break
            elif "ls" == yazi2:
                print("mysql.db")
            elif "cat mysql.db" in yazi2:
                print(kgb)
                print("umarım gobuster atmışsındır. Napman gerektiğin gayet iyi biliyorsun...")
            elif "lavrov1980.yandex.ru" in yazi2:
                print(dosyalar)
            elif yazi2 in ['1', '2', '3', '4', '5', '7', '8']:
                print("güzel günler")
            elif yazi2 in ['6', '9']:
                print('uygunsuz bi fotoğraf var... bunu social engineering için kullanabilirsin.')
            elif "http://smtp.voteportal.gov" in yazi2:
                os.system("python3 2.py")
            elif "/tetikle" in yazi2:
                yazi3 = input('tekrardan hoş geldin çok işimiz var: ').strip()
                if "reg add" in yazi3:
                    print("yetkili olduğumuza göre dosyaları okuyalım")
                elif "ls" in yazi3:
                    print("iletişim.exe")
                elif "iletişim.exe" in yazi3:
                    os.system("python3 iletişim.py")
                elif "/bağlan" in yazi3:
                    yazi4 = input("son saldırı yorumluş olmalısın hazırmısın: bilgitopla.py ").strip()
                    if "python3 bilgitopla.py" in yazi4:
                        print(zafiyet)
                    elif "gbd run info register" in yazi4:
                        print("264")
                    elif "leak puts_addr base_libc" in yazi4:
                        print("güzel şimdi exploit diyerek exploit i yaz")
                        print(ex)
                    elif "exploit" in yazi4:
                        os.system("python3 exploit.py")
            else:
                print("msf: Komut tanınmadı.")
    else:
        print("Komut tanınmadı.")
