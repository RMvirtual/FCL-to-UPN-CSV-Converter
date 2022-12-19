import unittest
from src.main.companies.upn.database.marshalling.customer \
    import UPNCustomerUnmarshaller


class TestUPNCustomerMarshaller(unittest.TestCase):
    def setUp(self):
        self._raw_input = {
            'CustomerID': 4236,
            'Consignor': 'GRAYLAW',
        }

    def test_should_unmarshall_customer(self) -> None:
        marshaller = UPNCustomerUnmarshaller()
        result = marshaller.customer(self._raw_input)

        self.assertEqual(4236, result.id)
        self.assertEqual("GRAYLAW", result.name)


if __name__ == "__main__":
    unittest.main()
