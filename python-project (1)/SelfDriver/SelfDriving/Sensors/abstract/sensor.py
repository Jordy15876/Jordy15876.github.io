from abc import ABC, abstractmethod

class Sensor(ABC):
    '''
    An abstract base class for a sensor component.
    
    The the purpose of this class is to encapsulate hardware that
    provides input data to the autonomous vehicle. 
    '''

    @abstractmethod
    def write_data(self, raw_data: bytes) -> None:
        '''Puts raw_data into memory'''

    @abstractmethod
    def read_data(self) -> bytes:
        '''Gets raw_data from memory'''
