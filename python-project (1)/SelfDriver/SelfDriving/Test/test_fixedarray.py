import unittest
from SelfDriving.DataStructures.fixedarry import FixedArray

class TestFixedArray(unittest.TestCase):
    def test_creation(self):
        # Test creating a FixedArray
        size = 5
        arr = FixedArray(size)
        self.assertEqual(len(arr), size)
        self.assertEqual(arr.data, bytes(size))

    def test_indexing(self):
        # Test indexing and slicing
        data = bytes([1, 2, 3, 4, 5])
        arr = FixedArray(len(data))
        arr.update(data)

        # Test individual element access
        for i in range(len(data)):
            self.assertEqual(arr[i], data[i])

        # Test slicing
        self.assertEqual(arr[1:4], data[1:4])

    def test_update(self):
        # Test updating the FixedArray
        data = bytes([1, 2, 3, 4, 5])
        arr = FixedArray(len(data))
        arr.update(data)

        new_data = bytes([6, 7, 8, 9, 10])
        arr.update(new_data)
        self.assertEqual(arr.data, new_data)

    def test_setitem(self):
        # Test setting elements using __setitem__
        arr = FixedArray(5)
        arr[0] = 10
        self.assertEqual(arr[0], 10)

    def test_invalid_index(self):
        # Test accessing out-of-range index
        arr = FixedArray(5)
        with self.assertRaises(IndexError):
            value = arr[10]

    def test_invalid_value(self):
        # Test setting invalid value
        arr = FixedArray(5)
        with self.assertRaises(ValueError):
            arr[0] = 300  # Value exceeds 255

if __name__ == '__main__':
    unittest.main()
