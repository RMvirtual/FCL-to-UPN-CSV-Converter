import unittest
from src.main.forward_office.dashboard.parser.consignment \
    import ConsignmentParser


class TestConsignmentParser(unittest.TestCase):
    def setUp(self) -> None:
        self._field_indexes = {
            "contact_name": 0,
            "company_name":  1,
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

        self._simple_example = [
            "Mr Susan Cheshire", "10 BRAMBLING RISE",
            "HEMEL HEMPSTEAD", "", "", "HEMEL HEMPSTEAD", "HP2 6DT",
            "GR220806951", "(078)41 332424",
            "1000", "1", "PALL", "PALLETS N/D AM",
            "PROP PAL LTD",
            "", "", "",  "",
            "", "", "", "",
            "", "", "", "",
            "TEL: 07841 332424, TAIL LIFT", "",
            "1:00pm", "23-Aug-22",
            "", "1",
            "3", "Yes"
        ]

    def test_should_parse_consignment_address(self):
        parser = ConsignmentParser(self._field_indexes)
        consignment = parser.parse(self._simple_example)

        address = consignment.address
        self.assertEqual("Mr Susan Cheshire", address.contact_name)
        self.assertEqual("10 BRAMBLING RISE", address.name)
        self.assertEqual("HEMEL HEMPSTEAD", address.line_1)
        self.assertEqual("", address.line_2)
        self.assertEqual("", address.line_3)
        self.assertEqual("HEMEL HEMPSTEAD", address.town)
        self.assertEqual("HP2 6DT", address.post_code)
        self.assertEqual("(078)41 332424", address.telephone_number)
        self.assertEqual("GB", address.country)

    def test_should_parse_reference(self):
        parser = ConsignmentParser(self._field_indexes)
        consignment = parser.parse(self._simple_example)

        reference = consignment.reference
        self.assertEqual("GR220806951", str(reference))

    def test_should_parse_cargo(self):
        parser = ConsignmentParser(self._field_indexes)
        consignment = parser.parse(self._simple_example)

        cargo = consignment.cargo
        self.assertEqual(1, len(cargo))

        entry = cargo[0]
        self.assertTupleEqual((1, 1000), entry.quantity_and_weight)

        package_type = entry.package_type
        self.assertEqual("full", package_type.name)
        self.assertEqual("pallet", package_type.base_type)
        self.assertEqual("normal", package_type.oversize_option)

    def test_should_parse_delivery_instructions(self):
        parser = ConsignmentParser(self._field_indexes)
        consignment = parser.parse(self._simple_example)

        correct_instructions = ["TEL: 07841 332424, TAIL LIFT"]

        self.assertListEqual(
            correct_instructions, consignment.delivery_instructions)

    def test_should_parse_principal_client(self):
        parser = ConsignmentParser(self._field_indexes)
        consignment = parser.parse(self._simple_example)

        self.assertEqual("PROP PAL LTD", consignment.client_name)

    def test_should_parse_service(self):
        parser = ConsignmentParser(self._field_indexes)
        consignment = parser.parse(self._simple_example)

        service = consignment.service

        self.assertTrue(service.is_priority())
        self.assertTrue(service.is_timed())
        self.assertTrue(service.has_premium_service())
        self.assertFalse(service.has_booked_service())

    def test_should_parse_delivery_date(self):
        parser = ConsignmentParser(self._field_indexes)
        consignment = parser.parse(self._simple_example)

        date = consignment.delivery_date

        self.assertEqual(23, date.day)
        self.assertEqual(8, date.month)
        self.assertEqual(2022, date.year)

    def test_should_parse_delivery_time(self):
        parser = ConsignmentParser(self._field_indexes)
        consignment = parser.parse(self._simple_example)

        time = consignment.delivery_time
        self.assertEqual(13, time.hour)
        self.assertEqual(0, time.minute)


if __name__ == '__main__':
    unittest.main()
