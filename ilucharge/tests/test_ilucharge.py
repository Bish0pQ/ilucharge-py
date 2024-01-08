import unittest
from unittest.mock import MagicMock
from ilucharge import ChargerStatusFetcher
import requests


class TestChargerStatusFetcher(unittest.TestCase):

    def setUp(self):
        # Create a ChargerStatusFetcher instance with a mocked IP address
        self.charger_instance = ChargerStatusFetcher(ip_address="192.168.0.174")

    def test_construct_status_url(self):
        # Test the construct_status_url method
        url = self.charger_instance.construct_status_url("status")
        self.assertEqual(url, "http://192.168.0.174/status")

    def test_get_charger_status_success(self):
        # Test the get_charger_status method for a successful response
        expected_response = r"""'{'mode': 'STA', 'wifi_client_connected': 1, 'eth_connected': 0, 'net_connected': 1, 
        'ipaddress': '192.168.0.174', 'emoncms_connected': 0, 'packets_sent': 0, 'packets_success': 0, 
        'mqtt_connected': 1, 'ocpp_connected': 0, 'ocpp_visable': False, 'free_heap': 165532, 'comm_sent': 21540, 
        'comm_success': 21536, 'rapi_connected': 1, 'evse_connected': 1, 'amp1': 0, 'voltage1': 0, 'amp2': 0, 
        'voltage2': 0, 'amp3': 0, 'voltage3': 0, 'pilot': 9, 'power': 0, 'wh': 1003782, 'session_energy': 0, 
        'total_energy': 1003.782, 'temp': 237, 'temp_max': 237, 'temp1': 237, 'temp2': False, 'temp3': False, 
        'proximity': False, 'state': 1, 'flags': 512, 'vehicle': 0, 'colour': 2, 'manual_override': 0, 'freeram': 
        165532, 'divertmode': 1, 'srssi': -64, 'status': 'active', 'elapsed': 0, 'wattsec': 0, 'watthour': 1003782, 
        'gfcicount': 0, 'nogndcount': 4, 'stuckcount': 0, 'solar': 0, 'grid_ie': 0, 'charge_rate': 0, 
        'divert_update': 14041, 'ota_update': 0, 'time': '2024-01-08T20:22:42Z', 'offset': '+0000', 
        'vehicle_state_update': 14041, 'tesla_vehicle_count': False, 'tesla_vehicle_id': False, 'tesla_vehicle_name': 
        False}"""

        # Mock the requests.get method to return a MagicMock with a JSON method
        with unittest.mock.patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = expected_response
            mock_get.return_value = mock_response

            # Call the method under test
            json_response = self.charger_instance.get_charger_status()

        json_start = json_response[0] + json_response[1]
        # Assert that the response is as expected
        self.assertEqual(json_start, r"'{")

    def test_get_charger_status_failure(self):
        # Test the get_charger_status method for a failure scenario
        with unittest.mock.patch('requests.get') as mock_get:
            # Mock the requests.get method to raise a RequestException
            mock_get.side_effect = requests.exceptions.RequestException("Mocked error")

            # Call the method under test
            json_response = self.charger_instance.get_charger_status()

        # Assert that the response is None in case of failure
        self.assertIsNone(json_response)


if __name__ == '__main__':
    unittest.main()
