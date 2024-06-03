import unittest
from unittest.mock import patch, Mock
import requests
from SelfDriving.Sensors.GPS import GPS

class TestGPS(unittest.TestCase):

    def setUp(self):
        self.gps = GPS(memory_size=5)

    def test_write_data_valid(self):
        self.gps.write_data(10)
        self.assertEqual(self.gps.read_data(), [10])

    def test_write_data_invalid(self):
        with self.assertRaises(ValueError):
            self.gps.write_data('invalid')
        self.assertEqual(self.gps.read_data(), [])
        
        with self.assertRaises(ValueError):
            self.gps.write_data(300)  # Invalid byte value
        self.assertEqual(self.gps.read_data(), [])

    def test_memory_size_exceeded(self):
        for i in range(5):
            self.gps.write_data(i)
        with self.assertRaises(MemoryError):
            self.gps.write_data(5)

    def test_clear_memory(self):
        self.gps.write_data(10)
        self.gps.clear_memory()
        self.assertEqual(self.gps.read_data(), [])

    @patch('requests.get')
    def test_fetch_gps_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'raw_data': 30}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        self.gps.fetch_gps_data('http://example.com/api')
        self.assertEqual(self.gps.read_data(), [30])

    @patch('requests.get')
    def test_fetch_gps_data_failure(self, mock_get):
        mock_get.side_effect = requests.RequestException("Connection Error")

        self.gps.fetch_gps_data('http://example.com/api')
        self.assertEqual(self.gps.read_data(), [])

if __name__ == '__main__':
    unittest.main()
0