import unittest
from src.main.upn.api.data_types.marshalling import UpnApiMarshaller
from datetime import datetime


class TestUpnApiTypeMarshalling(unittest.TestCase):
    def setUp(self):
        self._marshaller = UpnApiMarshaller()

    def test_should_unmarshall_primitive_types(self):
        self.assertEqual(str, self._marshaller.unmarshall_to_type("string"))
        self.assertEqual(int, self._marshaller.unmarshall_to_type("int"))

        self.assertEqual(
            datetime, self._marshaller.unmarshall_to_type("datetime"))

    def test_should_unmarshall_container_types(self):
        self.assertEqual(list, self._marshaller.unmarshall_to_type("array"))

        self.assertEqual(
            dict, self._marshaller.unmarshall_to_type("dictionary"))


if __name__ == '__main__':
    unittest.main()
