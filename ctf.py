import os
import time
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
Документ № KGB-PERS-7781/B
Дата: 17.08.2024
Классификация: СЕКРЕТНО

Тема: Уязвимые точки ключевых сотрудников по личным и семейным обстоятельствам

1. Полковник **Алексей Трофимов**
   - Семейное положение: женат, 2 детей (Артем, 14 лет; Елизавета, 9 лет)
   - Жена работает в школе №92 г. Москва
   - Часто ссорится с супругой, по данным прослушки были угрозы развода
   - Обнаружено: незадекларированная квартира в Болгарии, оформлена на имя племянника
   - Увлечение: коллекционные шахматы, подписан на закрытый форум collectors.ru
   - Слабость: азартные игры (онлайн-платформа "Volna Casino")

2. Капитан **Ирина Михайлова**
   - Одинокая мать, сын Павел (6 лет), детсад "Северные пчелки"
   - Участвует в родительском комитете, известна как доброжелательная
   - Использует Telegram и WhatsApp, iPhone 13 (пароль: Pavel20017!)
   - Психологическое наблюдение: признаки депрессии после смерти матери в 2022
   - Поддерживает связь с бывшим коллегой, уволенным за утечку данных

3. Старший аналитик **Дмитрий Лавров**
   - Женат, но имеет внебрачную связь с гражданкой Латвии
   - Регулярно посещает отель "Ласточка" в районе Красногорск
   - Финансовая активность превышает официальный доход в 3 раза
   - Сын Антон учится в лицее №125, часто забирается отцом (расписание приложено)
   - Хранит фотографии семьи на Yandex.Disk, доступ через website: lavrov1980.yandex.ru

Рекомендации:
- Усилить наблюдение
- Использовать данные для контроля/мягкого давления
- В случае необходимости — задействовать отдел S (внешнее психологическое воздействие)

Подпись: Н.Г. Иванов  
Утверждено: Центр Психоанализа и Контроля КГБ

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
for i in range(0x10000, 0x110000):  # Unicode range (BMP dışı dahil)
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

    if yazi in nmap:
        print(nmap)
    elif yazi in "http://10.0.10.0":
        print("bi halt yok")
    elif yazi in "gobuster":
        print('[Mail Server] - smtp.voteportal.gov (10.0.0.11)')
    elif yazi in "http://smtp.voteportal.gov":
        print('ipucu sızdıktan sonra kullanıcan')
    elif yazi in 'gobuster dir':
        print(cikti)
    elif yazi in "/login.php":
        print("welcome to login")
    elif yazi in "/admin/":
        print("forbidden")
    elif yazi in "/admin/upload":
        print("forbidden")
    elif yazi in "/config.php.bak":
        print("mysql:Apache Tika-server < 1.18")
    elif yazi in 'msf':
        print(msf)
    elif yazi in 'use exploit/multi/http/tika_server_injection':
        
        while True:
            yazi2 = input("msf> ").strip()

            if yazi2 in "exit":
                print("msf modundan çıkılıyor...")
                break
            elif yazi2 in "ls":
                print("mysql.db")
            elif yazi2 in "cat mysql.db":
                print(kgb)
                print('umarım gobuster atmışsındır. Napman gerektiğin gayet iyi biliyorsun...')
            elif yazi2 in 'lavrov1980.yandex.ru':
                print(dosyalar)
            elif yazi2 in ['1', '2', '3', '4', '5', '7', '8']:
                print('güzel günler')
            elif yazi2 in ['6', '9']:
                print('uygunsuz bi fotoğraf var çocuğuyla ilgili işte anladın sen bu bilgiyi kullan social engineering için umarım gobuster atmışsındır başında?')
                print('ne yapacağını anlamadıysan bana mı soruyorsun kardeş hayal gücünü kullan he unutmadan şifre 123')
            elif yazi2 in "http://smtp.voteportal.gov":
                os.system('python3 2.py')
            elif yazi2 in "/tetikle":
                yazi3 = input('tekrardan hoş geldin çok işimiz var: ').strip()
                if yazi3 in 'reg add':
                    print('yetkili olduğumuza göre dosyaları okuyalım')
                elif yazi3 in 'ls':
                    print('iletişim.exe')
                elif yazi3 in 'iletişim.exe':
                    os.system('python3 iletişim.py')
                elif yazi3 in '/bağlan':
                    yazi4 = input('son saldırı yorumluş olmalısın hazırmısın: bilgitopla.py ').strip()
                    if yazi4 in 'python3 bilgitopla.py':
                        print(zafiyet)
                    elif yazi4 in 'gbd run info register':
                        print('264')
                    elif yazi4 in 'leak puts_addr base_libc = puts_addr - offset_puts':
                        print('güzel şimdi exploit diyerek exploit i yaz')
                        print(ex)
                        print('bunu kullan')
                    elif yazi4 in 'exploit':
                        os.system('python3 exploit.py')
            else:
                print("msf: Komut tanınmadı.")
    else:
        print("Komut tanınmadı.")
