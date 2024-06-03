
from typing import Union

class FixedArray:
    def __init__(self, size: int) -> None:
        self._size = size #This is the size of the FixedArray
        self._data = bytearray(size) #This creates an empty bytearray which will have a specified size

    def __repr__(self) -> str:
        return f"FixedArray({self._data})"

    def __len__(self) -> int:
        return self._size 

    def __getitem__(self, key: Union[int, slice]) -> Union[int, bytes]:
        if isinstance(key, slice):
            return self._data[key]
        else:
            if key < 0 or key >= self._size:
                raise IndexError("Index out of range") #This will raise an IndexError if the key is out of the specified range
            return self._data[key] #This will return an item at the specified index

    def __setitem__(self, key: int, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if not 0 <= value <= 255:
            raise ValueError("Value must be in the range [0, 255]")
        self._data[key] = value

    def update(self, data: Union[bytes, bytearray]) -> None:
        if len(data) != self._size:
            raise ValueError("Data size must match the size of the FixedArray")
        self._data = bytearray(data)

    @property
    def data(self) -> bytes:
        return bytes(self._data)#This will return the data of the FixedArray as bytes

    @property
    def size(self) -> int:
        return self._size#This will return the size of the FixedArray