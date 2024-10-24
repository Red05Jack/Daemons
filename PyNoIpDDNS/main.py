import requests
from requests.auth import HTTPBasicAuth
import json


# Funktion zum Laden der Konfiguration aus einer JSON-Datei
def load_config(file_path="config.json"):
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print(f"Die Konfigurationsdatei '{file_path}' wurde nicht gefunden.")
        return None
    except json.JSONDecodeError:
        print(f"Fehler beim Lesen der JSON-Datei '{file_path}'.")
        return None


# Funktion zum Abrufen der öffentlichen IP-Adresse
def get_public_ip():
    try:
        # Externe Dienstleistung zum Abrufen der öffentlichen IP
        ip = requests.get('https://api.ipify.org').text
        return ip
    except requests.RequestException as e:
        print(f"Fehler beim Abrufen der IP: {e}")
        return None


# Funktion zum Aktualisieren des No-IP DDNS-Eintrags
def update_no_ip(username, password, hostname):
    ip_address = get_public_ip()

    if ip_address:
        try:
            # URL von No-IP für das DDNS-Update
            update_url = f"https://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={ip_address}"

            # Anfrage zum Aktualisieren der IP senden
            response = requests.get(update_url, auth=HTTPBasicAuth(username, password))

            # Rückmeldung von No-IP
            if response.status_code == 200:
                print(f"DDNS-Update erfolgreich: {response.text}")
            else:
                print(f"Fehler beim Aktualisieren des DNS-Eintrags: {response.text}")
        except requests.RequestException as e:
            print(f"Fehler beim Senden der Update-Anfrage: {e}")
    else:
        print("Keine IP-Adresse verfügbar, Update nicht möglich.")


# Skript ausführen
if __name__ == "__main__":
    # Konfiguration aus JSON laden
    config = load_config("config.json")

    if config:
        # Anmeldeinformationen und Hostnamen aus der JSON-Konfigurationsdatei holen
        no_ip_username = config["noip"]["username"]
        no_ip_password = config["noip"]["password"]
        hostname = config["noip"]["hostname"]

        # No-IP DDNS-Update durchführen
        update_no_ip(no_ip_username, no_ip_password, hostname)
