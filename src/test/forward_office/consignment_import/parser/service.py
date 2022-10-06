import unittest

from src.main.forward_office.consignment_import.parser.service import ServiceParser

from src.main.forward_office.consignment_import.parser.requests.types \
    import ServiceParseRequest


class TestServiceParser(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def _load_simple_example(self):
        self._example = ServiceParseRequest()
        self._example.priority_code = 2
        self._example.tail_lift_requested = True

    def _load_complex_example(self):
        self._example = ServiceParseRequest()
        self._example.priority_code = 11
        self._example.tail_lift_requested = False

    def test_should_parse_simple_example(self):
        self._load_simple_example()
        parser = ServiceParser()
        service = parser.parse(self._example)

        self.assertTrue(service.is_priority())
        self.assertTrue(service.is_tail_lift_required())
        self.assertFalse(service.has_premium_service())
        self.assertFalse(service.has_booked_service())
        self.assertFalse(service.is_saturday())

    def test_should_parse_complex_example(self):
        self._load_complex_example()
        parser = ServiceParser()
        service = parser.parse(self._example)

        self.assertTrue(service.is_economy())
        self.assertTrue(service.has_premium_service())
        self.assertTrue(service.is_saturday())
        self.assertTrue(service.is_am())
        self.assertFalse(service.is_tail_lift_required())
        self.assertFalse(service.is_booked())


if __name__ == '__main__':
    unittest.main()
