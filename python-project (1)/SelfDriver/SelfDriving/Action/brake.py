from SelfDriving.Action.abstract.actuator import Actuator
from SelfDriving.Action.speed import Speed


class Brake(Actuator):
    '''A brake pedal. This also acts as a decelerator pedal.'''

    def __init__(self, speed: Speed):
        super().__init__()
        self._key = "Brake"
        self._speed = speed

    def perform_action(self, action: str) -> None:
        '''Performs an action'''
        if action == "press":
            self._speed.decrease(10)
        elif action == "release":
            self._speed.stop_deceleration()
        elif action == "hold_down":
            self._speed.hold_down_to_stop()
