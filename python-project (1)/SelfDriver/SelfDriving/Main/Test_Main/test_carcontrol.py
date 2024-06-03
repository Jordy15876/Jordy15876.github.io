import unittest
from unittest.mock import MagicMock
from SelfDriving.Main.Car_Control import CarControl

class TestCarControl(unittest.TestCase):

    def setUp(self):
        self.car = CarControl()

    def test_accelerate(self):
        initial_speed = self.car.get_current_speed()
        self.car.execute_command("accelerate")
        increased_speed = self.car.get_current_speed()
        self.assertGreater(increased_speed, initial_speed)

    def test_brake(self):
        initial_speed = self.car.get_current_speed()
        self.car.execute_command("brake")
        decreased_speed = self.car.get_current_speed()
        self.assertLess(decreased_speed, initial_speed)

    # To test further functionalities of the code more test can be added

if __name__ == '__main__':
    unittest.main()
