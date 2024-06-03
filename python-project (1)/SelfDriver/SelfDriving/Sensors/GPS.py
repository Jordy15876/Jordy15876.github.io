import requests
from SelfDriving.DataStructures.fixedarry import FixedArray
from SelfDriving.Sensors.abstract.sensor import Sensor

class GPS(Sensor):
    '''A simple GPS sensor that stores raw data.'''

    def __init__(self, memory_size):
        self._memory = FixedArray(memory_size)
        self._current_index = 0
        self._route_data = []  # To store route data

    def write_data(self, raw_data):
        '''Write raw data to memory. Only bytes (0-255) are allowed.'''
        if not isinstance(raw_data, int) or not 0 <= raw_data <= 255:
            raise ValueError("Invalid raw data: must be an integer between 0 and 255")
        
        if self._current_index >= self._memory.size:
            raise MemoryError("Memory size exceeded")

        self._memory[self._current_index] = raw_data
        self._current_index += 1

    def read_data(self):
        '''Gets raw data from memory. Returns a list of data up to the current index.'''
        return list(self._memory.data[:self._current_index])

    def clear_memory(self):
        '''Clears memory.'''
        self._memory = FixedArray(self._memory.size)
        self._current_index = 0

    def fetch_gps_data(self, url):
        '''Fetch GPS data from a URL and write it to memory.'''
        try:
            response = requests.get(url)
            response.raise_for_status()
            raw_data = response.json().get('raw_data')
            if raw_data is not None:
                self.write_data(raw_data)
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching GPS data: {e}")

    def set_route_data(self, route_data):
        '''Set route data. Expects a list of route points.'''
        if not isinstance(route_data, list):
            raise ValueError("Route data must be a list")
        self._route_data = route_data

    def get_current_route(self):
        '''Gets current route data.'''
        return self._route_data
# # Example usage:
# if __name__ == "__main__":
#     # Create an instance of GPS sensor
#     gps_sensor = GPS(memory_size=10)
#
#     # Manually provide GPS data
#     gps_sensor.fetch_gps_data(50)  # Example GPS data
#
#     # Read the GPS data from memory
#     gps_data = gps_sensor.read_data()
#     print("GPS Data:", gps_data)
#
#     # Set and get route data
#     gps_sensor.set_route_data([1, 2, 3, 4, 5])
#     route_data = gps_sensor.get_current_route()
#     print("Route Data:", route_data)
