import unittest
from src.main.companies.upn.api.data_types.factory import APIDataTypesFactory


class TestUPNDataTypeMarshalling(unittest.TestCase):
    def setUp(self):
        self._factory = APIDataTypesFactory()

    def test_should_get_primitive_type(self) -> None:
        self.assertEqual(str, self._factory.type("string"))

    def test_should_get_primitive_instance(self) -> None:
        self.assertEqual("", self._factory.instance("string"))

    def test_should_get_primitive_instance_with_value(self) -> None:
        self.assertEqual(
            "Hello, World!", self._factory.instance("string", "Hello, World!"))

    def test_should_get_container_type(self) -> None:
        self.assertEqual(list, self._factory.type("array"))

    def test_should_get_container_instance(self) -> None:
        self.assertEqual([], self._factory.instance("array"))


if __name__ == '__main__':
    unittest.main()
