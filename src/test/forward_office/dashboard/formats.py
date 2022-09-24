import unittest
from src.main.forward_office.dashboard.format.formats import DashboardFormats


class TestDashboardFormats(unittest.TestCase):
    def setUp(self) -> None:
        self._correct_format = {
            'contact_name': 0, 'company_name': 1, 'address_line_1': 2,
            'address_line_2': 3, 'address_line_3': 4, 'town': 5,
            'post_code': 6, 'reference': 7, 'telephone_no': 8,
            'line_1_weight': 9, 'line_1_quantity': 10,
            'line_1_package_type': 11, 'line_1_description': 12,
            'principal_client': 13, 'line_2_weight': 14,
            'line_2_quantity': 15, 'line_2_package_type': 16,
            'line_2_description': 17, 'line_3_weight': 18,
            'line_3_quantity': 19, 'line_3_package_type': 20,
            'line_3_description': 21, 'line_4_weight': 22,
            'line_4_quantity': 23, 'line_4_package_type': 24,
            'line_4_description': 25, 'delivery_instruction_1': 26,
            'delivery_instruction_2': 27, 'booking_time': 28,
            'delivery_date': 29, 'shipper_reference': 30,
            'total_pallets': 31, 'priority_code': 32,
            'tail_lift_required': 33
        }

    def test_can_get_a_dashboard_format(self):
        formats = DashboardFormats()
        dashboard_format = formats.UPNEDIIMP

        self.assertDictEqual(self._correct_format, dashboard_format)


if __name__ == '__main__':
    unittest.main()
