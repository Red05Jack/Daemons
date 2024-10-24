from math import trunc

import requests
from requests.auth import HTTPBasicAuth
import json
import os
import platform
import time


# Function to perform a ping to a specific host.
def ping(host):
    system_name = platform.system().lower()

    if system_name == "windows":
        # Windows uses -n for the number of pings, -w for timeout in milliseconds
        param = '-n 1 -w 1000'
    else:
        # Linux/macOS use -c for the number of pings, -W for timeout in seconds
        param = '-c 1 -W 1'

    command = f"ping {param} {host}"

    # Execute the command and check the return value
    response = os.system(command)

    # If the return value is 0, the ping was successful (target reachable)
    if response == 0:
        return True
    else:
        return False


# Function to load configuration from a JSON file
def load_config(file_path="config.json"):
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print(f"The configuration file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error reading the JSON file '{file_path}'.")
        return None


# Function to get the public IP address
def get_public_ip():
    try:
        # External service to get the public IP address
        ip = requests.get('https://api.ipify.org').text
        return ip
    except requests.RequestException as e:
        print(f"Error fetching the IP address: {e}")
        return None


# Function to update the No-IP DDNS entry
def update_no_ip(username, password, hostname):
    ip_address = get_public_ip()

    if ip_address:
        try:
            # No-IP URL for DDNS update
            update_url = f"https://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={ip_address}"

            # Send request to update the IP address
            response = requests.get(update_url, auth=HTTPBasicAuth(username, password))

            # Response from No-IP
            if response.status_code == 200:
                print(f"DDNS update successful: {response.text}")
            else:
                print(f"Error updating the DNS entry: {response.text}")
        except requests.RequestException as e:
            print(f"Error sending the update request: {e}")
    else:
        print("No IP address available, update not possible.")


if __name__ == "__main__":
    config = load_config("config.json")
    need_update = False
    is_connected = False

    if config:
        while True:
            try:
                if need_update:
                    update_no_ip(
                        username=config["noip"]["username"],
                        password=config["noip"]["password"],
                        hostname=config["noip"]["hostname"]
                    )
                    need_update = False

                if ping("www.google.com") and ping("www.noip.com"):
                    if not is_connected:
                        need_update = True
                    is_connected = True
                else:
                    is_connected = False

                time.sleep(5)
            except KeyboardInterrupt:
                print("Script terminated.")
                break
