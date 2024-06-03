from SelfDriving.Action.abstract.actuator import Actuator
from SelfDriving.Action.speed import Speed

class Accelerator(Actuator):
    '''An accelerator pedal.'''

    def __init__(self, speed: Speed):
        super().__init__()
        self._key = "Accelerator"
        self._speed = speed

    def perform_action(self, action: str) -> None:
        '''Performs an action'''
        if action == "press":
            self._speed.increase(10)  # Increase the speed by 10 units
            self._speed.stop_deceleration()  # Stop deceleration when accelerator is pressed
        elif action == "release":
            self._speed.start_deceleration()  # Start deceleration when accelerator is released
        elif action == "balanced":
            pass  # Placeholder for handling balanced action
