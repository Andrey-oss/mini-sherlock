'''Service parser'''
import json

def service_parser():
    '''Service parser'''

    with open('services.json', "r+", encoding='utf-8') as cfg:
        services = json.load(cfg)

    return services
