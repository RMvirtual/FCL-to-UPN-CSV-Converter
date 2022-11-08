import unittest
from src.main.upn.api.structures import arrays


class TestArrays(unittest.TestCase):
    def test_should_extract_underlying_array_object_type(self):
        result = arrays.extract_array_object_name("array_of_network_pallet")
        self.assertEqual("network_pallet", result)


if __name__ == '__main__':
    unittest.main()
