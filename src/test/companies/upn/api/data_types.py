import unittest
from src.main.companies.upn.api.data_types.implementation import APIDataTypes


class TestUPNAPIDataTypes(unittest.TestCase):
    def setUp(self):
        self._data_types = APIDataTypes()

    def test_should_get_primitive_type(self) -> None:
        self.assertEqual(str, self._data_types.type("string"))

    def test_should_get_primitive_instance(self) -> None:
        self.assertEqual("", self._data_types.instance("string"))

    def test_should_get_primitive_instance_with_value(self) -> None:
        self.assertEqual(
            "Hello, World!",
            self._data_types.instance("string", "Hello, World!")
        )

    def test_should_get_container_type(self) -> None:
        self.assertEqual(list, self._data_types.type("array"))

    def test_should_get_container_instance(self) -> None:
        self.assertEqual([], self._data_types.instance("array"))

    def test_should_raise_exception_with_invalid_type(self) -> None:
        with self.assertRaises(ValueError):
            _ = self._data_types["BreakMe"]


if __name__ == '__main__':
    unittest.main()
