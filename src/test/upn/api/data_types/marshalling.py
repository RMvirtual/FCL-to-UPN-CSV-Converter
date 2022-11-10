import dataclasses
import unittest
from src.main.upn.api.data_types.marshalling import DataTypeMarshaller
from datetime import datetime


class TestUpnApiTypeMarshalling(unittest.TestCase):
    @dataclasses.dataclass
    class InstanceToUnmarshall:
        type_name: str
        value: str or int
        correct_value: any

    def setUp(self):
        self._marshaller = DataTypeMarshaller()

    def test_should_unmarshall_primitive_types(self):
        self.assertEqual(str, self._marshaller.unmarshall_to_type("string"))
        self.assertEqual(int, self._marshaller.unmarshall_to_type("int"))

        self.assertEqual(
            datetime, self._marshaller.unmarshall_to_type("datetime"))

    def test_should_unmarshall_container_types(self):
        self.assertEqual(list, self._marshaller.unmarshall_to_type("array"))

        self.assertEqual(
            dict, self._marshaller.unmarshall_to_type("dictionary"))

    def test_should_unmarshall_primitive_instances(self):
        marshalling_candidates = [
            self.InstanceToUnmarshall("string", "test_1", "test_1"),
            self.InstanceToUnmarshall("int", "1", 1)
        ]

        for candidate in marshalling_candidates:
            result = self._marshaller.unmarshall_to_instance(
                candidate.type_name, candidate.value)

            self.assertEqual(candidate.correct_value, result)

    def test_should_unmarshall_container_instances(self):
        marshalling_candidates = [
            self.InstanceToUnmarshall("array", "test_1", []),
            self.InstanceToUnmarshall("dictionary", "1", {})
        ]

        for candidate in marshalling_candidates:
            result = self._marshaller.unmarshall_to_instance(
                candidate.type_name, candidate.value)

            self.assertEqual(candidate.correct_value, result)


if __name__ == '__main__':
    unittest.main()
