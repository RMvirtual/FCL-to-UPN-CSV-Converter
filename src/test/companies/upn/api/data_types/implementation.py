import unittest
from src.main.companies.upn.api.data_types.implementation import APIDataTypes


class TestUPNAPIDataTypes(unittest.TestCase):
    def setUp(self):
        self._data_types = APIDataTypes()

    def test_should_get_type_of_primitive(self):
        self.assertEqual(str, self._data_types["string"])

    def test_should_get_type_of_container(self):
        self.assertEqual(dict, self._data_types["dictionary"])

    def test_should_raise_exception_with_invalid_type(self) -> None:
        with self.assertRaises(ValueError):
            _ = self._data_types["FooBar"]


if __name__ == '__main__':
    unittest.main()
