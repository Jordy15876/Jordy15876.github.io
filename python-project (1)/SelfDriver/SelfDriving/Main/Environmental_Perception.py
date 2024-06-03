from SelfDriving.Sensors.Camera import CameraSensor
from SelfDriving.Sensors.LIDAR import LidarSensor
from typing import List
from collections import deque

class EnvironmentalPerception:
    def __init__(self, camera_buffer_size: int = 10, lidar_buffer_size: int = 10):
        self.camera_sensor = CameraSensor(camera_buffer_size)
        self.lidar_sensor = LidarSensor(lidar_buffer_size)
        self.detected_objects = []
        self.detected_objects_history = deque(maxlen=100)
        self.traffic_light_state = {}

    def process_sensor_data(self):
        camera_data = self.camera_sensor.read_data()
        self.detect_objects(camera_data)
        lidar_data = self.lidar_sensor.read_data()
        self.process_traffic_lights(lidar_data)

    def detect_objects(self, camera_data: bytes) -> List[str]:
        # Simulate detecting objects
        detected_objects = []  # Initialize detected objects list
        
        if b"car" in camera_data:
            detected_objects.append("car")
        if b"pedestrian" in camera_data:
            detected_objects.append("pedestrian")
        if b"traffic_sign" in camera_data:
            detected_objects.append("traffic_sign")

        self.detected_objects = detected_objects
        self.detected_objects_history.append(detected_objects)

    def process_traffic_lights(self, lidar_data: List[float]) -> dict:
        # This simulates the processing of traffic light data 
        
        traffic_light_data = {"traffic_light_1": 0.5, "traffic_light_2": 0.8}  # Placeholder for lidar data
        self.traffic_light_state = {}
        for light, distance in traffic_light_data.items():
            if distance < 1.0:  # Assuming threshold for red light detection
                self.traffic_light_state[light] = "red"
            else:
                self.traffic_light_state[light] = "green"
