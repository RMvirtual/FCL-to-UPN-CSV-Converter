import unittest

from src.main.forward_office.dashboard.export.parser.address \
    import AddressParser


class TestCargoParser(unittest.TestCase):
    def setUp(self) -> None:
        self._field_indexes = {
            "contact_name": 0,
            "company_name": 1,
            "address_line_1": 2,
            "address_line_2": 3,
            "address_line_3": 4,
            "town": 5,
            "post_code": 6,
            "telephone_no": 8
        }

        self._values_to_parse = [
            "Mr Susan Cheshire",
            "10 BRAMBLING RISE",
            "HEMEL HEMPSTEAD",
            "",
            "",
            "HEMEL HEMPSTEAD",
            "HP2 6DT",
            "...",
            "(078) 4133 2424"
        ]

    def test_should_read_cargo_stuff(self):
        self.fail("Dummy fail for cargo parser.")


if __name__ == '__main__':
    unittest.main()
