import unittest
from src.main.consignment.service_options import ServiceOptions


class TestServiceOptions(unittest.TestCase):
    def should_create_default_service_options(self):
        service_options = ServiceOptions()

        checks = [
            service_options.main_service.is_next_day(),
            service_options.premium_service.is_not_required(),
            service_options.additional_service.is_not_required(),
            service_options.tail_lift.is_not_required()
        ]

        for check in checks:
            self.assertTrue(check)


if __name__ == '__main__':
    unittest.main()
