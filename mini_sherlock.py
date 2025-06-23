'''Simple sherlock realisation using requests library'''

from modules.service_parser import service_parser as SP
from modules.make_request import make_request

BANNER = '''

███╗░░░███╗██╗███╗░░██╗██╗░░░░░░░██████╗██╗░░██╗███████╗██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
████╗░████║██║████╗░██║██║░░░░░░██╔════╝██║░░██║██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██╔████╔██║██║██╔██╗██║██║█████╗╚█████╗░███████║█████╗░░██████╔╝██║░░░░░██║░░██║██║░░╚═╝█████═╝░
██║╚██╔╝██║██║██║╚████║██║╚════╝░╚═══██╗██╔══██║██╔══╝░░██╔══██╗██║░░░░░██║░░██║██║░░██╗██╔═██╗░
██║░╚═╝░██║██║██║░╚███║██║░░░░░░██████╔╝██║░░██║███████╗██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝
                                    {0}


'''

print (BANNER.format(f'Coded by https://t.me/Andreyoss; Loaded: {len(SP())} services'))

nickname = input ("Enter nickname: ")

print (BANNER.format('Please wait..'))

for service_name, config in SP().items():
    print(f"Checking {service_name}...")
    make_request(config, nickname)
