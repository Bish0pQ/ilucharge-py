from urllib.parse import urlunparse
import requests


class ChargerStatusFetcher:
    def __init__(self, ip_address):
        self.IP = ip_address

    def construct_status_url(self, path):
        scheme = "http"
        netloc = self.IP
        path = path.strip('/')  # Remove leading/trailing slashes to ensure proper concatenation
        return urlunparse((scheme, netloc, path, '', '', ''))

    def get_charger_status(self):
        try:
            response = requests.get(self.construct_status_url('status'))
            response.raise_for_status()  # Raise an HTTPError for bad responses
            json_data = response.json()
            return json_data
        except requests.exceptions.RequestException as e:
            print(f"Error making HTTP request: {e}")
            return None


if __name__ == "__main__":
    # Example usage
    charger_instance = ChargerStatusFetcher(ip_address="192.168.0.174")
    json_response = charger_instance.get_charger_status()

    if json_response:
        print("JSON Response:")
        print(json_response)
    else:
        print("Failed to retrieve JSON.")
