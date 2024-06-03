from typing import Union
from SelfDriving.DataStructures.fixedarry import FixedArray
from SelfDriving.Sensors.abstract.sensor import Sensor

class CameraSensor(Sensor):
    def __init__(self, data_size: int) -> None:
        self._data_buffer = FixedArray(data_size)  # Initialize the data buffer with FixedArray
        self._data_size = data_size

    def write_data(self, image_data: bytes) -> None:
        '''Store image data in the sensor'''
        self._data_buffer.update(image_data)  # Update the data buffer with the new image data

    def read_data(self) -> bytes:
        '''Retrieve image data from the sensor'''
        return bytes(self._data_buffer.data)

    @property
    def size(self) -> int:
        return self._data_size