import unittest
from src.main.companies.upn.api.marshalling import customer


class TestUPNCustomerMarshaller(unittest.TestCase):
    def setUp(self):
        self._raw_input = {
            'CustomerID': 4236,
            'Consignor': 'GRAYLAW',
        }

    def test_should_unmarshall_customer(self) -> None:
        result = customer.unmarshall(self._raw_input)

        self.assertEqual(4236, result.id)
        self.assertEqual("GRAYLAW", result.name)


if __name__ == "__main__":
    unittest.main()
