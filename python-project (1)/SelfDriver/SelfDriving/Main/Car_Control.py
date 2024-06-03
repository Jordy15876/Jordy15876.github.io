from collections import deque
from SelfDriving.Action.accelerator import Accelerator
from SelfDriving.Action.brake import Brake
from SelfDriving.Action.steering import Steering
from SelfDriving.Action.speed import Speed

class CarControl:
    def __init__(self):
        self.current_speed = Speed(50)
        self.speed_history = deque(maxlen=10)
        self.accelerator = Accelerator(self.current_speed)
        self.brake = Brake(self.current_speed)
        self.steering = Steering()

    def execute_command(self, command: str):
        if command == "accelerate":
            self.accelerator.perform_action("press")  # Press is used for the action
        elif command == "brake":
            self.brake.perform_action("press")
        elif command == "turn_left":
            self.steering.turn_left(15)
        elif command == "turn_right":
            self.steering.turn_right(15)
        elif command == "straighten":
            self.steering.straighten()

    def decide_action(self, navigation, perception):
        if self.current_speed.is_stopped():
            if not navigation.is_at_destination():
                self.execute_command("accelerate")
        else:
            if perception.detected_objects and "pedestrian" in perception.detected_objects:
                self.execute_command("brake")
            elif not navigation.is_at_destination():
                self.execute_command("accelerate")
    def get_current_speed(self):
        return self.current_speed.get_speed()
    
    def update_speed(self, new_speed):
        if new_speed != self.current_speed.get_speed():
            self.current_speed = Speed(new_speed)
            self.speed_history.append(new_speed)

    def decide_action(self, navigation, perception):
        if self.current_speed.is_stopped():
            if not navigation.is_at_destination():
                self.execute_command("accelerate")
                self.update_speed(10)  # Adjust speed to 10 when starting from stop
        else:
            if perception.detected_objects and "pedestrian" in perception.detected_objects:
                self.execute_command("brake")
                self.update_speed(0)  # Adjust speed to 0 when detecting pedestrian
            elif not navigation.is_at_destination():
                self.execute_command("accelerate")
                self.update_speed(50)  # Adjust speed to 50 when driving
