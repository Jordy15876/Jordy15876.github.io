from SelfDriving.DataStructures.fixedarry import FixedArray  # Importing FixedArray from your helper functions
from SelfDriving.Sensors.abstract.sensor import Sensor
from typing import List

class LidarSensor(Sensor):
    def __init__(self, array_size: int) -> None:
        self._data_buffer = FixedArray(array_size)

    def write_data(self, raw_data: bytes) -> None:
        '''Store raw_data in the data buffer'''
        self._data_buffer.update(raw_data)

    def read_data(self) -> bytes:
        '''Retrieve raw_data from the data buffer'''
        return self._data_buffer.data

    def process_data(self, raw_data: bytes) -> List[float]:
        '''Process raw_data from Lidar sensor'''
        # Placeholder for data processing logic
        # For now, let's just return an empty list
        return []

    def get_latest_data(self) -> List[float]:
        '''Retrieve and process the latest Lidar data'''
        raw_data = self.read_data()
        if not raw_data:
            return []  # If no data, return an empty list
        processed_data = self.process_data(raw_data)  # Process the latest data
        return processed_data

    @property
    def data_buffer(self) -> bytes:
        '''Get the data buffer'''
        return self._data_buffer.data
    def __init__(self, array_size: int) -> None:
        self._data_buffer = FixedArray(array_size)

    def write_data(self, raw_data: bytes) -> None:
        '''Store raw_data in the data buffer'''
        self._data_buffer.update(raw_data)

    def read_data(self) -> bytes:
        '''Retrieve raw_data from the data buffer'''
        return self._data_buffer.data

    def process_data(self, raw_data: bytes) -> List[float]:
        '''Process raw_data from Lidar sensor'''
        # Placeholder for data processing logic
        # For now, let's just return an empty list
        return []

    def get_latest_data(self) -> List[float]:
        '''Retrieve and process the latest Lidar data'''
        raw_data = self.read_data()
        if not raw_data:
            return []  # If no data, return an empty list
        processed_data = self.process_data(raw_data)  # Process the latest data
        return processed_data

    @property
    def data_buffer(self) -> bytes:
        '''Get the data buffer'''
        return self._data_buffer.data