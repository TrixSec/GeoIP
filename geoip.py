# Copyright (c) 2024 Trixsec
# See the file 'LICENSE' for copying permission.

import argparse
import requests
import random
from termcolor import colored
import sys

GEOIP_VERSION = "1.0"
AUTHOR = "Trix Cyrus"
COPYRIGHT = "Copyright © 2024 Trixsec Org"

def print_banner():
    banner = r"""
 ██████╗ ███████╗ ██████╗ ██╗██████╗ 
██╔════╝ ██╔════╝██╔═══██╗██║██╔══██╗
██║  ███╗█████╗  ██║   ██║██║██████╔╝
██║   ██║██╔══╝  ██║   ██║██║██╔═══╝ 
╚██████╔╝███████╗╚██████╔╝██║██║     
 ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝      v1.0      :coded by Trix:
    """
    print(colored(banner, 'cyan'))
    print(colored(f"GeoIP Version: {GEOIP_VERSION}", 'yellow'))
    print(colored(f"Made by {AUTHOR}", 'yellow'))
    print(colored(COPYRIGHT, 'yellow'))

def generate_random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def get_ip_info(ip):
    url = f"https://ipwho.is/{ip}"
    
    random_ip = generate_random_ip()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.183 Safari/537.36",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",  
        "Cache-Control": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Referer": "https://ipwho.is/",
        "X-Forwarded-For": random_ip,  
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_info(data):
    if data:
        
        keys_to_skip = ['flag'] 
        nested_keys = ['connection', 'timezone']  
        
        for key, value in data.items():
            if key in keys_to_skip:
                continue
            
            if isinstance(value, dict):
                print(colored(f"{key.capitalize()}: ", 'cyan', attrs=['bold']))
                for sub_key, sub_value in value.items():
                    print(colored(f"  {sub_key.capitalize()}: {sub_value}", 'green', attrs=['bold']))
                print("-------------->")
            else:
                if key.lower() in ['success', 'is_eu', 'is_dst']: 
                    print(colored(f"{key.capitalize()}: {value}", 'cyan', attrs=['bold']))
                else:
                    print(colored(f"{key.capitalize()}: {value}", 'cyan', attrs=['bold']))
                print("-------------->")

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Get IP geolocation information.")
    parser.add_argument('--ip', type=str, required=True, help="IP address to lookup")
    
    args = parser.parse_args()
    
    try:
        ip_info = get_ip_info(args.ip)
        display_info(ip_info)
    except KeyboardInterrupt:
        print("\nOperation aborted by user. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()

