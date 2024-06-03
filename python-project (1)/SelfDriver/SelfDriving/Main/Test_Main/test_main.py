import unittest
from unittest.mock import MagicMock
from SelfDriving.Main.main import Driverless, nav, aiu, cont,percept

class TestDriverless(unittest.TestCase):
    def test_driverless(self):
        # Create mock objects for dependencies
        ui_mock = MagicMock(spec=aiu)
        navigation_mock = MagicMock(spec=nav)
        car_control_mock = MagicMock(spec=cont)
        environment_perception_mock = MagicMock(spec=percept)
        
        expected_location = (0.0, 0.0)  # This sets the expected location of the car
        navigation_mock.fetch_current_location.return_value = expected_location
        
        
        # In this testing, we use mock to test them
        with unittest.mock.patch('__main__.aiu', return_value=ui_mock), \
             unittest.mock.patch('__main__.nav', return_value=navigation_mock), \
             unittest.mock.patch('__main__.cont', return_value=car_control_mock), \
             unittest.mock.patch('__main__.percept', return_value=environment_perception_mock):
            
            Driverless()
        
     # To test further functionalities of the code more test can be added
        
if __name__ == '__main__':
    unittest.main()
