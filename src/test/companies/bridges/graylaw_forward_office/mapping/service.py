import unittest
from src.main.companies.bridges.graylaw_forward_office.mapping\
    .service import FclServiceCodeMap


class TestFCLServiceCodeMappings(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_map_basic_service(self):
        service_mappings = FclServiceCodeMap()
        service = service_mappings[2]

        self.assertTrue(service.is_priority())
        self.assertFalse(service.has_premium_service())
        self.assertFalse(service.has_booked_service())
        self.assertFalse(service.is_saturday())

    def test_should_verify_if_priority_code_contained(self):
        service_mappings = FclServiceCodeMap()
        service = service_mappings

        self.assertTrue(service.contains(1))
        self.assertFalse(service.contains(111))

    def test_should_map_complex_service(self):
        service_mappings = FclServiceCodeMap()
        service = service_mappings[11]

        self.assertTrue(service.is_economy())
        self.assertTrue(service.has_premium_service())
        self.assertTrue(service.is_am())
        self.assertTrue(service.is_saturday())
        self.assertFalse(service.has_booked_service())


if __name__ == '__main__':
    unittest.main()
