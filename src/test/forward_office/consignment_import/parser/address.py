import unittest

from src.main.forward_office.consignment_import.parser import address

from src.main.forward_office.consignment_import.parser.requests.types \
    import AddressParseRequest


class TestAddressParser(unittest.TestCase):
    def setUp(self) -> None:
        self._request = AddressParseRequest()
        self._request.contact_name = "Mr Susan Cheshire"
        self._request.name = "10 BRAMBLING RISE"
        self._request.line_1 = "HEMEL HEMPSTEAD"
        self._request.line_2 = ""
        self._request.line_3 = ""
        self._request.town = "HEMEL HEMPSTEAD"
        self._request.post_code = "HP2 6DT"
        self._request.telephone_number = "(078) 4133 2424"

    def test_should_parse_an_address(self):
        result = address.parse(self._request)

        self.assertEqual(result.name, "10 BRAMBLING RISE")
        self.assertEqual(result.lines[0], "HEMEL HEMPSTEAD")
        self.assertEqual(result.lines[1], "")
        self.assertEqual(result.lines[2], "")
        self.assertEqual(result.town, "HEMEL HEMPSTEAD")
        self.assertEqual(result.post_code, "HP2 6DT")
        self.assertEqual(result.country, "GB")
        self.assertEqual(result.contact_name, "Mr Susan Cheshire")
        self.assertEqual(result.telephone_number, "(078) 4133 2424")


if __name__ == '__main__':
    unittest.main()
