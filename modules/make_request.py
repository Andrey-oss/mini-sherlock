'''Module for request creating and then handling'''

import requests

def make_request(service_config, nickname):
    '''Make and handle request with service params'''

    url = service_config["url"] + nickname
    method = service_config["method"].lower()

    try:
        response = requests.request(
            method=method,
            url=url,
            timeout=15
        )

        if response.status_code == service_config["success_code"]:
            print(f"[+] {url} — Found!")
        else:
            print(f"[-] {url} — Not found")

    except requests.exceptions.RequestException as e:
        print(f"[!] Some error occurred {url}: {e}")
