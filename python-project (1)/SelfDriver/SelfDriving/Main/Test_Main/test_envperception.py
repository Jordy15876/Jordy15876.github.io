import unittest
from SelfDriving.Main.Environment_Perception import EnvironmentalPerception

class TestEnvironmentalPerception(unittest.TestCase):
    def setUp(self):
        # Initialize Environmental_Perception instance for testing
        self.env_perception = EnvironmentalPerception(camera_buffer_size=10, lidar_buffer_size=10)

    def test_process_sensor_data(self):
        # Test processing sensor data
        self.env_perception.process_sensor_data()
        self.assertTrue(isinstance(self.env_perception.detected_objects, list))
        self.assertTrue(isinstance(self.env_perception.traffic_light_state, dict))
        

    def test_detect_objects(self):
        # Test object detection
        camera_data = b'sample_camera_data'
        self.env_perception.detect_objects(camera_data)
        self.assertTrue(isinstance(self.env_perception.detected_objects, list))
       

    def test_process_traffic_lights(self):
        # Test processing lidar data to determine traffic light state
        lidar_data = [1.0, 2.0, 3.0]  # Example lidar data
        self.env_perception.process_traffic_lights(lidar_data)
        self.assertTrue(isinstance(self.env_perception.traffic_light_state, dict))
       
       # To test further functionalities of the code more test can be added

if __name__ == '__main__':
    unittest.main()
