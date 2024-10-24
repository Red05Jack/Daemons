# No-IP DDNS Updater Daemon

This Python script automatically updates your No-IP Dynamic DNS (DDNS) entry with your current public IP address. It checks whether your internet connection is active and, if needed, updates your No-IP configuration. This ensures that your hostname remains updated with your public IP, allowing you to consistently reach your devices even when your IP changes.

## Features

- Pings `www.google.com` and `www.noip.com` to verify internet connectivity.
- Retrieves the public IP address using `https://api.ipify.org`.
- Updates the No-IP DDNS entry if the public IP address has changed.
- Configurable credentials and hostname via a `config.json` file.

## Requirements

- Python 3.x
- The following Python modules:
  - `requests`
  - `json`
  - `os`
  - `platform`
  - `time`

To install the required Python libraries, run:

```sh
pip install requests
```

## Configuration

The script relies on a `config.json` file for the configuration of No-IP credentials. The structure of the `config.json` file should be as follows:

```json
{
  "noip": {
    "username": "your_noip_username",
    "password": "your_noip_password",
    "hostname": "your_noip_hostname"
  }
}
```

Replace `your_noip_username`, `your_noip_password`, and `your_noip_hostname` with your actual No-IP credentials.

## Usage

1. Clone this repository or download the files.
2. Install the required dependencies.
3. Create the `config.json` file in the same directory as the script with your No-IP credentials.
4. Run the script:

```sh
python main.py
```

The script will continuously monitor your connection and update your No-IP DDNS entry as needed.

## How It Works

1. **Ping Check**: The script pings `www.google.com` and `www.noip.com` to determine if the internet connection is active.
2. **Public IP Retrieval**: If a connection is available, it retrieves your public IP address using `https://api.ipify.org`.
3. **No-IP Update**: If the public IP changes or an update is needed, the script sends a request to the No-IP update URL with your credentials to update the DDNS entry.

## Error Handling

- If the configuration file (`config.json`) is missing or incorrect, the script will notify the user.
- In case of issues with retrieving the public IP or updating No-IP, appropriate error messages are displayed.

## Notes

- This script will run indefinitely until manually stopped using `CTRL+C`.
- Make sure to keep your No-IP credentials secure and do not share them publicly.

## License

This project is licensed under the MIT License.
