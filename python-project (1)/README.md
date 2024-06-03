# README
This code is an imitation autonomous car system. To understand how the software works, Continue to the File Structure portion below. 
The car should in theory be able to drive on its own to a set destination, obey traffic lights, and detect objects 
In all honesty this code is very barebones and will be updated once proficiency with the logic has been obtained.
The time provided was only enough to learn how to do what has been outlined in the code.
# Set Up
This code requires python version 3.11+, so please double check that you have it.

To find out if python 3.11+ is installed on your machine, from the command line, type: python -version

If you don't have it installed, you can install it from python.org.

Once you have the correct version, you can run this program, by making this folder your active directory, and then typing:

python app/main.py

# File Structure
The file structure has been created in a way so that allow for as much flexibility as possible

# SelfDriving/Actions
This contains the components that aid an autonomous vehicle to move.
You have an actuator which two components obey:
  •	Accelerator: This class represents an accelerator pedal
  •	Brake: This class represents a brake pedal
These two classes also take into consideration the speed class when updating the speed
A class also exist for handling the steering.

# SelfDriving/DataStructures
This is is where the Fixed Array component is defined.
This is used to store the data as bytearrays.

# SelfDriving/Sensors
This where the component that aid the autonomous vehicle in sensing.
All components obey a sensor abstract base class.
The components in this are:
•	Camera: This class encapsulates the camera sensor on the car
•	GPS: This encapsulates the GPS sensor.
•	LIDAR: This encapsulates the LIDAR sensor.

# SelfDriving/Tests
This place is where the tests of the system is located for the components above.

# Main
This is where the main decision making modules are as well as the test for them.