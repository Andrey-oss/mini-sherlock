# Подключения библиотек

import os
import requests

os.system("clear")
print ('''

███╗░░░███╗██╗███╗░░██╗██╗░░░░░░░██████╗██╗░░██╗███████╗██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
████╗░████║██║████╗░██║██║░░░░░░██╔════╝██║░░██║██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██╔████╔██║██║██╔██╗██║██║█████╗╚█████╗░███████║█████╗░░██████╔╝██║░░░░░██║░░██║██║░░╚═╝█████═╝░
██║╚██╔╝██║██║██║╚████║██║╚════╝░╚═══██╗██╔══██║██╔══╝░░██╔══██╗██║░░░░░██║░░██║██║░░██╗██╔═██╗░
██║░╚═╝░██║██║██║░╚███║██║░░░░░░██████╔╝██║░░██║███████╗██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝
                                                        Coded by https://t.me/Andreyoss


''')

# Ввод никнейма
nickname = input ("Введите пожалуйста никнейм для проверки: ")

os.system("clear")
os.system("clear")
print ('''

███╗░░░███╗██╗███╗░░██╗██╗░░░░░░░██████╗██╗░░██╗███████╗██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
████╗░████║██║████╗░██║██║░░░░░░██╔════╝██║░░██║██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██╔████╔██║██║██╔██╗██║██║█████╗╚█████╗░███████║█████╗░░██████╔╝██║░░░░░██║░░██║██║░░╚═╝█████═╝░
██║╚██╔╝██║██║██║╚████║██║╚════╝░╚═══██╗██╔══██║██╔══╝░░██╔══██╗██║░░░░░██║░░██║██║░░██╗██╔═██╗░
██║░╚═╝░██║██║██║░╚███║██║░░░░░░██████╔╝██║░░██║███████╗██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝

                             Пожалуйста подождите


''')
# Подготовка сервисов
github = requests.get ("https://github.com/"+nickname)
gitlab = requests.get("https://gitlab.com/"+nickname)
facebook = requests.get("https://m.facebook.com/"+nickname)
instagram = requests.get("https://www.instagram.com/"+nickname)
medium = requests.get("https://medium.com/@"+nickname)
youtube = requests.get("https://www.youtube.com/c/"+nickname)
soundcloud = requests.get("https://soundcloud.com/"+nickname)
disqus = requests.get("https://disqus.com/"+nickname)
pinterest = requests.get("https://www.pinterest.com/"+nickname)
vimeo = requests.get("https://vimeo.com/"+nickname)
aboutme = requests.get("https://about.me/"+nickname)
flipboard = requests.get("https://flipboard.com/@"+nickname)
slideshare = requests.get("https://www.slideshare.net/"+nickname)
spotify = requests.get("https://open.spotify.com/user/"+nickname)
scribd = requests.get("https://www.scribd.com/"+nickname)
patreon = requests.get("https://www.patreon.com/"+nickname)
bitbucket = requests.get("https://bitbucket.org/"+nickname)
roblox = requests.get("https://www.roblox.com/user.aspx?username="+nickname)
gravatar = requests.get("http://en.gravatar.com/"+nickname)
imgsrcru = requests.head("https://imgsrc.ru/main/user.php?user="+nickname)
dailymotion = requests.get("https://www.dailymotion.com/"+nickname)
etsy = requests.get("https://www.etsy.com/shop/"+nickname)
behance = requests.get("https://www.behance.net/"+nickname)
goodreads = requests.get("https://www.goodreads.com/"+nickname)
instructables = requests.get("https://www.instructables.com/member/"+nickname)

# Обработка

if  github.status_code == 200:
    print ("Github - https://github.com/"+nickname)
else:
    print ("Github - не найденo")

os.system ("sleep 0.1")

if  gitlab.status_code == 200:
    print ("Gitlab - https://gitlab.com/"+nickname)
else:
    print ("Gitlab - не найденo")

os.system ("sleep 0.1")

if  facebook.status_code == 200:
    print ("Facebook - https://www.facebook.com/"+nickname)
else:
    print ("Facebook - не найден")

os.system ("sleep 0.1")

if  instagram.status_code == 200:
    print ("Instagram - https://www.instagram.com/"+nickname)
else:
    print ("Instagram - не найден")

os.system ("sleep 0.1")

if  medium.status_code == 200:
    print ("Medium - https://medium.com/@"+nickname)
else:
    print ("Medium - не найден")

os.system ("sleep 0.1")

if  youtube.status_code == 200:
    print ("Youtube - https://youtube.com/c/"+nickname)
else:
    print ("Youtube - не найден")

os.system ("sleep 0.1")

if  soundcloud.status_code == 200:
    print ("Soundcloud - https://soundcloud.com/"+nickname)
else:
    print ("Soundcloud - не найден")

os.system ("sleep 0.1")

if  disqus.status_code == 200:
    print ("Disqus - https://disqus.com/"+nickname)
else:
    print ("Disqus - не найден")

os.system ("sleep 0.1")

if  pinterest.status_code == 200:
    print ("Pinterest - https://www.pinterest.com/"+nickname)
else:
    print ("Pinterest - не найден")

os.system ("sleep 0.1")

if  vimeo.status_code == 200:
    print ("Vimeo - https://vimeo.com/"+nickname)
else:
    print ("Vimeo - не найден")

os.system ("sleep 0.1")

if  aboutme.status_code == 200:
    print ("About.me - https://about.me/"+nickname)
else:
    print ("About.me - не найден")

os.system("sleep 0.1")

if  flipboard.status_code == 200:
    print ("FlipBoard - https://flipboard.com/@"+nickname)
else:
    print ("FlipBoard - не найден")

os.system("sleep 0.1")

if  slideshare.status_code == 200:
    print ("SlideShare - https://slideshare.net/"+nickname)
else:
    print ("SlideShare - не найден")

os.system("sleep 0.1")

if  spotify.status_code == 200:
    print ("Spotify - https://open.spotify.com/user/"+nickname)
else:
    print ("Spotify - не найден")

os.system("sleep 0.1")

if  scribd.status_code == 200:
    print ("Scribd - https://www.scribd.com/"+nickname)
else:
    print ("Scribd - не найден")

os.system("sleep 0.1")

if  patreon.status_code == 200:
    print ("Patreon - https://www.patreon.com/"+nickname)
else:
    print ("Patreon - не найден")

os.system("sleep 0.1")

if  bitbucket.status_code == 200:
    print ("BitBucket - https://bitbucket.org/"+nickname)
else:
    print ("BitBucket - не найден")

os.system("sleep 0.1")

if  roblox.status_code == 200:
    print ("Roblox - https://www.roblox.com/user.aspx?username="+nickname)
else:
    print ("Roblox - не найден")

os.system("sleep 0.1")

if  gravatar.status_code == 200:
    print ("Gravatar - http://en.gravatar.com/"+nickname)
else:
    print ("Gravatar - не найден")

os.system("sleep 0.1")

if  imgsrcru.status_code == 200:
    print ("iMGSRC.RU - https://imgsrc.ru/main/user.php?user="+nickname)
else:
    print ("iMGSRC.RU - не найден")

os.system("sleep 0.1")

if  dailymotion.status_code == 200:
    print ("DailyMotion - https://www.dailymotion.com/"+nickname)
else:
    print ("DailyMotion - не найден")

os.system("sleep 0.1")

if  etsy.status_code == 200:
    print ("Etsy - https://www.etsy.com/shop/"+nickname)
else:
    print ("Etsy - не найден")

os.system("sleep 0.1")

if  behance.status_code == 200:
    print ("Behance - https://www.behance.net/"+nickname)
else:
    print ("Behance - не найден")

os.system("sleep 0.1")

if  goodreads.status_code == 200:
    print ("Goodreads - https://www.goodreads.com/"+nickname)
else:
    print ("Goodreads - не найден")

os.system("sleep 0.1")

if  instructables.status_code == 200:
    print ("Instructables - https://www.instructables.com/member/"+nickname)
else:
    print ("Instructbales - не найден")
