import unittest
from unittest.mock import MagicMock
from SelfDriving.Main.Car_Navigation import CarNavigation

class TestCarNavigation(unittest.TestCase):
    def setUp(self):
        self.navigation_system = CarNavigation(memory_size=100)
        
        # Mocking as a means of ensuring that the gps sensor would work
        self.navigation_system.gps.read_data = MagicMock(return_value=(10.0, 20.0))  # Mocking GPS data
        
    def test_fetch_current_location(self):
        location = self.navigation_system.fetch_current_location()
        self.assertEqual(location, (10.0, 20.0))
        
    def test_update_navigation(self):
        self.navigation_system.update_route = MagicMock()  # we use mock for the update 
        
        self.navigation_system.update_navigation()
        
        # Asserting that update_route method is called
        self.navigation_system.update_route.assert_called_once()
        
    def test_update_route(self):
        # This goes by the assumption that the route has been given
        self.navigation_system.gps.get_current_route = MagicMock(return_value=[(10.0, 20.0), (15.0, 25.0)])
        
        self.navigation_system.update_route()
        
        # This asserts that the car coordinates have been updated 
        self.assertEqual(self.navigation_system.route_coordinates, [(10.0, 20.0), (15.0, 25.0)])
        
        # Asserting that route_history is updated
        self.assertEqual(len(self.navigation_system.route_history), 1)
        self.assertEqual(self.navigation_system.route_history[0], [(10.0, 20.0), (15.0, 25.0)])
        
if __name__ == '__main__':
    unittest.main()