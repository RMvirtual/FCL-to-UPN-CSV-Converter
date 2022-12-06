import dataclasses
import datetime
import unittest
from src.main.companies.upn.api.data_types.marshalling \
    import UPNDataTypeMarshaller


class TestUPNDataTypeMarshalling(unittest.TestCase):
    def setUp(self):
        self._marshaller = UPNDataTypeMarshaller()

    @dataclasses.dataclass
    class InstanceToUnmarshall:
        type_name: str
        value: str or int
        correct_value: any

    def test_should_unmarshall_primitive_types(self):
        unmarshall_candidates_to_correct_types = list({
            "string": str,
            "int": int,
            "datetime": datetime.datetime
        }.items())

        for candidate, correct_type in unmarshall_candidates_to_correct_types:
            unmarshalled_type = self._marshaller.unmarshall_to_type(candidate)
            self.assertEqual(correct_type, unmarshalled_type)

    def test_should_unmarshall_container_types(self):
        unmarshall_candidates_to_correct_types = list({
            "array": list,
            "dictionary": dict
        }.items())

        for candidate, correct_type in unmarshall_candidates_to_correct_types:
            unmarshalled_type = self._marshaller.unmarshall_to_type(candidate)
            self.assertEqual(correct_type, unmarshalled_type)

    def test_should_unmarshall_primitive_instances_with_values(self):
        unmarshalling_candidates = (
            self.InstanceToUnmarshall("string", "test_1", "test_1"),
            self.InstanceToUnmarshall("int", "1", 1)
        )

        self._validate_callback_against_marshalling_candidates(
            self._marshaller.unmarshall_to_instance, unmarshalling_candidates)

    def test_should_unmarshall_empty_primitive_instances(self):
        unmarshalling_candidates = (
            self.InstanceToUnmarshall("string", None, ""),
            self.InstanceToUnmarshall("int", None, 0)
        )

        self._validate_callback_against_marshalling_candidates(
            self._marshaller.unmarshall_to_instance, unmarshalling_candidates)

    def test_should_unmarshall_empty_container_instances(self):
        unmarshalling_candidates = (
            self.InstanceToUnmarshall("array", "test_1", []),
            self.InstanceToUnmarshall("dictionary", "1", {})
        )

        self._validate_callback_against_marshalling_candidates(
            self._marshaller.unmarshall_to_instance, unmarshalling_candidates
        )

    def _validate_callback_against_marshalling_candidates(
            self,  marshaller_callback: callable,
            unmarshalling_candidates: tuple[InstanceToUnmarshall, ...]
    ) -> None:
        for candidate in unmarshalling_candidates:
            result = marshaller_callback(candidate.type_name, candidate.value)
            self.assertEqual(candidate.correct_value, result)


if __name__ == '__main__':
    unittest.main()
