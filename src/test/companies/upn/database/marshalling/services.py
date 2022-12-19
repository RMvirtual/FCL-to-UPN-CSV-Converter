import unittest
from src.main.companies.upn.database.marshalling.services \
    import UPNServicesUnmarshaller


class TestUPNServicesUnmarshaller(unittest.TestCase):
    def setUp(self):
        self._raw_input = {
            'MainService': 'P',
            'PremiumService': None,
            'TailLift': None,
            'ExtraService': None,
        }

    def test_should_unmarshall_basic_next_day_services(self) -> None:
        marshaller = UPNServicesUnmarshaller()
        result = marshaller.services(self._raw_input)

        self.assertEqual("P", result.main_service.selection)
        self.assertEqual("", result.premium_service.selection)
        self.assertEqual("", result.tail_lift_required.selection)
        self.assertEqual("", result.additional_service.selection)


if __name__ == "__main__":
    unittest.main()
