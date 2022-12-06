import unittest
from src.main.companies.upn.api.marshalling import references


class TestUPNReferencesMarshaller(unittest.TestCase):
    def setUp(self):
        self._raw_input = {
            'ConBarcode': 'W213359799C',
            'ConNo': 'gr221004388',
            'CustRef': '49632',
        }

    def test_should_unmarshall_references(self) -> None:
        result = references.unmarshall_references(self._raw_input)

        self.assertEqual("gr221004388", result.consignment_no)
        self.assertEqual("49632", result.customer_reference)
        self.assertEqual("W213359799C", result.barcode)


if __name__ == "__main__":
    unittest.main()
