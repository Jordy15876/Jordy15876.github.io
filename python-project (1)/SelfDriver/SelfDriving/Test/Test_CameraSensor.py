import unittest
from SelfDriving.Sensors.Camera import CameraSensor
import numpy as np

class TestCameraSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = CameraSensor(100)  # Create a CameraSensor instance with a data buffer size of 100 bytes

    def test_write_and_read_data(self):
        # Test writing and reading data
        image_data = self.generate_image_data(100)  # Generate random image data of size 100 bytes
        self.sensor.write_data(image_data)
        self.assertEqual(self.sensor.read_data(), image_data)

    def test_size_property(self):
        # Test size property
        self.assertEqual(self.sensor.size, 100)

    @staticmethod
    def generate_image_data(size: int) -> bytes:
        # Generate random image data of the specified size
        return np.random.randint(0, 256, size=size, dtype=np.uint8).tobytes()

if __name__ == '__main__':
    unittest.main()
