# Подключения библиотек

import os
import requests

# Ввод никнейма

nickname = input ("Введите пожалуйста никнейм для проверки: ")

# Подготовка сервисов
github = requests.get ("https://github.com/"+nickname)
gitlab = requests.get("https://gitlab.com/"+nickname)
facebook = requests.get("https://www.facebook.com/"+nickname)
instagram = requests.get("https://www.instagram.com/"+nickname)
medium = requests.get("https://medium.com/@"+nickname)
youtube = requests.get("https://www.youtube.com/c/"+nickname)
soundcloud = requests.get("https://soundcloud.com/"+nickname)
disqus = requests.get("https://disqus.com/"+nickname)

# Обработка

if  github.status_code == 200:
    print ("Github - https://github.com/"+nickname)
else:
    print ("Github - не найденo")

os.system ("sleep 0.6")

if  gitlab.status_code == 200:
    print ("Gitlab - https://gitlab.com/"+nickname)
else:
    print ("Gitlab - не найденo")

os.system ("sleep 0.6")

if  facebook.status_code == 200:
    print ("Facebook - https://www.facebook.com/"+nickname)
else:
    print ("Facebook - не найден")

os.system ("sleep 0.6")

if  instagram.status_code == 200:
    print ("Instagram - https://www.instagram.com/"+nickname)
else:
    print ("Instagram - не найден")

os.system ("sleep 0.6")

if  medium.status_code == 200:
    print ("Medium - https://medium.com/@"+nickname)
else:
    print ("Medium - не найден")

os.system ("sleep 0.6")

if  youtube.status_code == 200:
    print ("Youtube - https://youtube.com/c/"+nickname)
else:
    print ("Youtube - не найден")

os.system ("sleep 0.6")

if  soundcloud.status_code == 200:
    print ("Soundcloud - https://soundcloud.com/"+nickname)
else:
    print ("Soundcloud - не найден")

os.system ("sleep 0.6")

if  disqus.status_code == 200:
    print ("Disqus - https://disqus.com/"+nickname)
else:
    print ("Disqus - не найден")
