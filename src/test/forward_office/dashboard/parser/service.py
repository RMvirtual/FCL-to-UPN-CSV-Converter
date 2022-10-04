import unittest
from src.main.forward_office.dashboard.parser.service.model \
    import ServiceParser


class TestServiceParser(unittest.TestCase):
    def setUp(self) -> None:
        self._dashboard_format = {
            "priority_code": 32,
            "tail_lift_required": 33
        }

    def _load_simple_example(self):
        self._dashboard_input = [
            "Mr Susan Cheshire", "10 BRAMBLING RISE",
            "HEMEL HEMPSTEAD", "", "", "HEMEL HEMPSTEAD", "HP2 6DT",
            "GR220806951", "(078)41332424",
            "1000", "1", "PAL2", "PALLETS N/D",
            "PROP PAL LTD",
            "", "", "", "",
            "", "", "", "",
            "", "", "", "",
            "TEL: 07841 332424, TAIL LIFT", "",
            "", "23-Aug-22", "", "1", "2", "Yes"
        ]

    def _load_complex_example(self):
        self._dashboard_input = [
            "Mr Susan Cheshire", "10 BRAMBLING RISE",
            "HEMEL HEMPSTEAD", "", "", "HEMEL HEMPSTEAD", "HP2 6DT",
            "GR220806951", "(078)41332424",
            "2000", "2", "PALL", "PALLETS N/D",
            "PROP PAL LTD",
            "600", "2", "QPL3", "",
            "800", "8", "MPAL", "",
            "1000", "2", "HPL2", "",
            "TEL: 07841 332424, TAIL LIFT", "",
            "", "23-Aug-22", "", "1", "11", "Yes"
        ]

    def test_should_parse_simple_example(self):
        self._load_simple_example()
        parser = ServiceParser(self._dashboard_format)
        service = parser.parse(self._dashboard_input)

        self.assertTrue(service.is_priority())
        self.assertTrue(service.is_tail_lift_required())
        self.assertFalse(service.has_premium_service())
        self.assertFalse(service.has_booked_service())
        self.assertFalse(service.is_saturday())

    def test_should_parse_complex_example(self):
        self._load_complex_example()
        parser = ServiceParser(self._dashboard_format)
        service = parser.parse(self._dashboard_input)

        self.assertTrue(service.is_economy())
        self.assertTrue(service.has_premium_service())
        self.assertTrue(service.is_saturday())
        self.assertTrue(service.is_am())
        self.assertTrue(service.is_tail_lift_required())
        self.assertFalse(service.is_booked())


if __name__ == '__main__':
    unittest.main()
