from abc import ABC, abstractmethod

class Actuator(ABC):
    """
    This is an abstract base class for an actuator component.

    the purpose of this class is to encapsulate the hardware that
    drives the autonomous vehicle.
    """

    @abstractmethod
    def perform_action(self, action):
        """
        Performs an action.

        Parameters:
            action (str): The action to be performed by the actuator.
        """
        pass
