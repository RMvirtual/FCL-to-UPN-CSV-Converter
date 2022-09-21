import unittest
from src.main.forward_office.dashboard.fields.upn_edi_imp \
    import format


class TestDashboardExportReader(unittest.TestCase):
    CORRECT_FIELDS = {
        "contact_name": 0,
        "company_name": 1,
        "address_line_1": 2,
        "address_line_2": 3,
        "address_line_3": 4,
        "town": 5,
        "post_code": 6,
        "reference": 7,
        "telephone_no": 8,
        "line_1_weight": 9,
        "line_1_quantity": 10,
        "line_1_package_type": 11,
        "line_1_description": 12,
        "principal_client": 13,
        "line_2_weight": 14,
        "line_2_quantity": 15,
        "line_2_package_type": 16,
        "line_2_description": 17,
        "line_3_weight": 18,
        "line_3_quantity": 19,
        "line_3_package_type": 20,
        "line_3_description": 21,
        "line_4_weight": 22,
        "line_4_quantity": 23,
        "line_4_package_type": 24,
        "line_4_description": 25,
        "delivery_instruction_1": 26,
        "delivery_instruction_2": 27,
        "booking_time": 28,
        "delivery_date": 29,
        "shipper_reference": 30,
        "total_pallets": 31,
        "priority_code": 32,
        "tail_lift_required": 33
    }

    def setUp(self) -> None:
        self._fields = format()

    def test_should_read_correct_number_of_fields(self):
        self.assertEqual(len(self.CORRECT_FIELDS), len(self._fields))

    def test_should_read_all_fields(self):
        for field in self.CORRECT_FIELDS:
            self.assertEqual(self.CORRECT_FIELDS[field], self._fields[field])


if __name__ == '__main__':
    unittest.main()