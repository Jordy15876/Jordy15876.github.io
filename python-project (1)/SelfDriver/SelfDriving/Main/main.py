from SelfDriving.Main.Car_Navigation import CarNavigation as nav
from SelfDriving.Main.User_Input import AutomatedCarUI as aiu
from SelfDriving.Main.Car_Control import CarControl as cont
from SelfDriving.Main.Environment_Perception import EnvironmentalPerception as percept

class Driverless:
    def __init__(self):
        self.create_components()
        self.location()
        
       
    def __call__(self):
        self.introduce_ai()
        navigation_status, navigation_info = self.start_navigation()  # Store the status and information returned by start_navigation
        return navigation_status, navigation_info  # Return the status and information to indicate success or failure

    def create_components(self):
        self.aiu = aiu()
        self.nav = nav(memory_size=10)
        self.cont = cont()
        self.percept = percept(camera_buffer_size=10, lidar_buffer_size=10)

    def location(self, position=None):
        if not position:
            self.nav.fetch_current_location()
        else:
            self.nav.update_location()

    def destination(self):
        destination = self.aiu.get_destination()
        self.nav.set_destination(destination)

    def get_route(self):
        self.nav.update_navigation()

    def drive_route(self):
        navigation_info = []  # Initialize an empty list to store navigation information
        self.percept.process_sensor_data()
        if self.percept.detected_objects:
            self.cont.execute_command("brake")
            navigation_info.append("Brake applied")  # Append brake information to navigation info
        else:
            self.cont.execute_command("accelerate")
            navigation_info.append("Accelerate")  # Append acceleration information to navigation info

        navigation_info.append("Reached destination")  # Append destination reached information
        return "Success", navigation_info  # Return success status and navigation information

    def introduce_ai(self):
        self.aiu.ux_print("Starting the AI interface...")

    def start_navigation(self):
        self.destination()
        self.get_route()
        navigation_status, navigation_info = self.drive_route()  # Store the status and information returned by drive_route
        return navigation_status, navigation_info  # Return the status and information to indicate success or failure

if __name__ == "__main__":
    driverless = Driverless()
    status, info = driverless()  # Call the instance to introduce the AI and get the status and information
    print("Navigation Status:", status)  # Print the status returned by the __call__ method
    print("Navigation Information:", info)  # Print the navigation information returned by the __call__ method


        

