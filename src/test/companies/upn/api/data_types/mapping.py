import unittest
from src.main.companies.upn.api.data_types.mapping import Mapping
from src.main.companies.upn.api.data_types.mapping import MappingMarshaller


class TestMappingMarshaller(unittest.TestCase):
    def setUp(self) -> None:
        self._marshaller = MappingMarshaller()

    def set_up_mapping_without_values_test_case(self):
        self.set_up_unmarshalling_candidate_without_values()
        self.set_up_correct_mapping_without_values()

    def set_up_mapping_with_values_test_case(self):
        self.set_up_unmarshalling_candidate_with_values()
        self.set_up_correct_mapping_with_values()

    def set_up_unmarshalling_candidate_without_values(self):
        self._candidate = {
            "type": "string",
            "mapping": "ConBarcode",
        }

    def set_up_unmarshalling_candidate_with_values(self):
        self._candidate = {
            "type": "string",
            "mapping": "PalletType",
            "values": ["Full", "Euro", "Half", "Quarter", "Micro"]
        }

    def set_up_correct_mapping_with_values(self):
        self._correct_result = Mapping()
        self._correct_result.type = str
        self._correct_result.mapping = "PalletType"
        self._correct_result.values = [
            "Full", "Euro", "Half", "Quarter", "Micro"]

    def set_up_correct_mapping_without_values(self):
        self._correct_result = Mapping()
        self._correct_result.type = str
        self._correct_result.mapping = "ConBarcode"
        self._correct_result.values = []

    def test_should_marshall_mapping_without_values(self) -> None:
        self.set_up_mapping_without_values_test_case()
        result = self._marshaller.unmarshal_to_mapping(self._candidate)

        self.assertEqual(self._correct_result, result)

    def test_should_marshall_mapping_with_values(self) -> None:
        self.set_up_mapping_with_values_test_case()
        result = self._marshaller.unmarshal_to_mapping(self._candidate)

        self.assertEqual(self._correct_result, result)


if __name__ == '__main__':
    unittest.main()
