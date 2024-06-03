
class Steering():
    '''A class to manage the steering of the vehicle.'''

    def __init__(self):
        self.angle = 0  # Assuming the angle scale is from -90 to 90 degrees

    def turn_left(self, degrees: int) -> None:
        '''Turn the steering left by a certain number of degrees.'''
        self.angle = max(self.angle - degrees, -90)
        print(f"Steering turned left to {self.angle} degrees")

    def turn_right(self, degrees: int) -> None:
        '''Turn the steering right by a certain number of degrees.'''
        self.angle = min(self.angle + degrees, 90)
        print(f"Steering turned right to {self.angle} degrees")

    def straighten(self) -> None:
        '''Straighten the steering.'''
        self.angle = 0
        print("Steering straightened")

    def get_angle(self) -> int:
        '''Get the current steering angle.'''
        return self.angle
