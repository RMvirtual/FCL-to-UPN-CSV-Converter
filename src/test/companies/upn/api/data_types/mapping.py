import unittest
from src.main.companies.upn.api.data_types.mapping import MappingMarshaller


class TestMappingMarshaller(unittest.TestCase):
    def setUp(self) -> None:
        self._marshaller = MappingMarshaller()

    def test_should_unmarshall_mapping_without_values(self) -> None:
        result = self._marshaller.unmarshal_to_mapping({"type": "string"})

        self.assertEqual(str, result.type)
        self.assertEqual([], result.values)

    def test_should_unmarshall_mapping_with_values(self) -> None:
        result = self._marshaller.unmarshal_to_mapping({
            "type": "string",
            "values": ["Full", "Euro", "Half", "Quarter", "Micro"]
        })

        self.assertEqual(str, result.type)

        self.assertListEqual(
            ["Full", "Euro", "Half", "Quarter", "Micro"], result.values)


if __name__ == '__main__':
    unittest.main()
