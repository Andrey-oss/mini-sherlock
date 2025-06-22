'''Simple sherlock realisation using requests library'''

import requests

BANNER = '''

███╗░░░███╗██╗███╗░░██╗██╗░░░░░░░██████╗██╗░░██╗███████╗██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
████╗░████║██║████╗░██║██║░░░░░░██╔════╝██║░░██║██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██╔████╔██║██║██╔██╗██║██║█████╗╚█████╗░███████║█████╗░░██████╔╝██║░░░░░██║░░██║██║░░╚═╝█████═╝░
██║╚██╔╝██║██║██║╚████║██║╚════╝░╚═══██╗██╔══██║██╔══╝░░██╔══██╗██║░░░░░██║░░██║██║░░██╗██╔═██╗░
██║░╚═╝░██║██║██║░╚███║██║░░░░░░██████╔╝██║░░██║███████╗██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝
                                    {0}


'''
print (BANNER.format('Coded by https://t.me/Andreyoss'))

nickname = input ("Enter nickname: ")

print (BANNER.format('Please wait..'))

github = requests.get ("https://github.com/"+nickname, timeout=15)
gitlab = requests.get("https://gitlab.com/"+nickname, timeout=15)
facebook = requests.get("https://m.facebook.com/"+nickname, timeout=15)
instagram = requests.get("https://www.instagram.com/"+nickname, timeout=15)
medium = requests.get("https://medium.com/@"+nickname, timeout=15)
youtube = requests.get("https://www.youtube.com/c/"+nickname, timeout=15)
soundcloud = requests.get("https://soundcloud.com/"+nickname, timeout=15)
disqus = requests.get("https://disqus.com/"+nickname, timeout=15)
pinterest = requests.get("https://www.pinterest.com/"+nickname, timeout=15)
vimeo = requests.get("https://vimeo.com/"+nickname, timeout=15)
aboutme = requests.get("https://about.me/"+nickname, timeout=15)
flipboard = requests.get("https://flipboard.com/@"+nickname, timeout=15)
slideshare = requests.get("https://www.slideshare.net/"+nickname, timeout=15)
spotify = requests.get("https://open.spotify.com/user/"+nickname, timeout=15)
scribd = requests.get("https://www.scribd.com/"+nickname, timeout=15)
patreon = requests.get("https://www.patreon.com/"+nickname, timeout=15)
bitbucket = requests.get("https://bitbucket.org/"+nickname, timeout=15)
roblox = requests.get("https://www.roblox.com/user.aspx?username="+nickname, timeout=15)
gravatar = requests.get("http://en.gravatar.com/"+nickname, timeout=15)
imgsrcru = requests.head("https://imgsrc.ru/main/user.php?user="+nickname, timeout=15)
dailymotion = requests.get("https://www.dailymotion.com/"+nickname, timeout=15)
etsy = requests.get("https://www.etsy.com/shop/"+nickname, timeout=15)
behance = requests.get("https://www.behance.net/"+nickname, timeout=15)
goodreads = requests.get("https://www.goodreads.com/"+nickname, timeout=15)
instructables = requests.get("https://www.instructables.com/member/"+nickname, timeout=15)
keybase = requests.get("https://keybase.io/"+nickname, timeout=15)

if  github.status_code == 200:
    print ("Github - https://github.com/"+nickname, timeout=15)
else:
    print ("Github - not found")

if  gitlab.status_code == 200:
    print ("Gitlab - https://gitlab.com/"+nickname, timeout=15)
else:
    print ("Gitlab - not found")

if  facebook.status_code == 200:
    print ("Facebook - https://www.facebook.com/"+nickname, timeout=15)
else:
    print ("Facebook - not found")

if  instagram.status_code == 200:
    print ("Instagram - https://www.instagram.com/"+nickname, timeout=15)
else:
    print ("Instagram - not found")

if  medium.status_code == 200:
    print ("Medium - https://medium.com/@"+nickname, timeout=15)
else:
    print ("Medium - not found")

if  youtube.status_code == 200:
    print ("Youtube - https://youtube.com/c/"+nickname, timeout=15)
else:
    print ("Youtube - not found")

if  soundcloud.status_code == 200:
    print ("Soundcloud - https://soundcloud.com/"+nickname, timeout=15)
else:
    print ("Soundcloud - not found")

if  disqus.status_code == 200:
    print ("Disqus - https://disqus.com/"+nickname, timeout=15)
else:
    print ("Disqus - not found")

if  pinterest.status_code == 200:
    print ("Pinterest - https://www.pinterest.com/"+nickname, timeout=15)
else:
    print ("Pinterest - not found")

if  vimeo.status_code == 200:
    print ("Vimeo - https://vimeo.com/"+nickname, timeout=15)
else:
    print ("Vimeo - not found")

if  aboutme.status_code == 200:
    print ("About.me - https://about.me/"+nickname, timeout=15)
else:
    print ("About.me - not found")

if  flipboard.status_code == 200:
    print ("FlipBoard - https://flipboard.com/@"+nickname, timeout=15)
else:
    print ("FlipBoard - not found")

if  slideshare.status_code == 200:
    print ("SlideShare - https://slideshare.net/"+nickname, timeout=15)
else:
    print ("SlideShare - not found")

if  spotify.status_code == 200:
    print ("Spotify - https://open.spotify.com/user/"+nickname, timeout=15)
else:
    print ("Spotify - not found")

if  scribd.status_code == 200:
    print ("Scribd - https://www.scribd.com/"+nickname, timeout=15)
else:
    print ("Scribd - not found")

if  patreon.status_code == 200:
    print ("Patreon - https://www.patreon.com/"+nickname, timeout=15)
else:
    print ("Patreon - not found")

if  bitbucket.status_code == 200:
    print ("BitBucket - https://bitbucket.org/"+nickname, timeout=15)
else:
    print ("BitBucket - not found")

if  roblox.status_code == 200:
    print ("Roblox - https://www.roblox.com/user.aspx?username="+nickname, timeout=15)
else:
    print ("Roblox - not found")

if  gravatar.status_code == 200:
    print ("Gravatar - http://en.gravatar.com/"+nickname, timeout=15)
else:
    print ("Gravatar - not found")

if  imgsrcru.status_code == 200:
    print ("iMGSRC.RU - https://imgsrc.ru/main/user.php?user="+nickname, timeout=15)
else:
    print ("iMGSRC.RU - not found")

if  dailymotion.status_code == 200:
    print ("DailyMotion - https://www.dailymotion.com/"+nickname, timeout=15)
else:
    print ("DailyMotion - not found")

if  etsy.status_code == 200:
    print ("Etsy - https://www.etsy.com/shop/"+nickname, timeout=15)
else:
    print ("Etsy - not found")

if  behance.status_code == 200:
    print ("Behance - https://www.behance.net/"+nickname, timeout=15)
else:
    print ("Behance - not found")

if  goodreads.status_code == 200:
    print ("Goodreads - https://www.goodreads.com/"+nickname, timeout=15)
else:
    print ("Goodreads - not found")

if  instructables.status_code == 200:
    print ("Instructables - https://www.instructables.com/member/"+nickname, timeout=15)
else:
    print ("Instructbales - not found")

if  keybase.status_code == 200:
    print ("Keybase - https://keybase.io/"+nickname, timeout=15)
else:
    print ("Keybase - not found")
