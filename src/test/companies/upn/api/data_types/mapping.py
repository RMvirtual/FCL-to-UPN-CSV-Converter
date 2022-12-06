import unittest
from src.main.companies.upn.api.data_types.constraints import ConstraintsMarshaller


class TestMappingMarshaller(unittest.TestCase):
    def setUp(self) -> None:
        self._marshaller = ConstraintsMarshaller()

    def test_should_unmarshall_mapping_without_values(self) -> None:
        result = self._marshaller.unmarshal_constraint({"type": "string"})

        self.assertEqual(str, result.type)
        self.assertEqual([], result.constraints)

    def test_should_unmarshall_mapping_with_values(self) -> None:
        result = self._marshaller.unmarshal_constraint({
            "type": "string",
            "values": ["Full", "Euro", "Half", "Quarter", "Micro"]
        })

        self.assertEqual(str, result.type)

        self.assertListEqual(
            ["Full", "Euro", "Half", "Quarter", "Micro"], result.constraints)


if __name__ == '__main__':
    unittest.main()
