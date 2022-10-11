import unittest

from src.main.forward_office.consignment_import.controller \
    import FclImportController


class TestCanImportOneLinerConsignment(unittest.TestCase):
    def setUp(self) -> None:
        self._import_format = {
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

        self._simple_example = [[
            "Ryan Matfen", "Graylaw Freight Group", "Gillibrands Road",
            "", "", "Skelmersdale",
            "WN8 9TA", "GR221003000", "01695 729101",
            "500", "1", "PALL", "PALLETS N/D",
            "Disneyworld",
            "", "", "", "",
            "", "", "", "",
            "", "", "", "",
            "Tail Lift", "",
            "1:00pm", "06-Oct-22", "OL1234",
            "1", "02", "Yes"
        ]]

    def test_should_import_one_liner_consignment(self):
        importer = FclImportController(self._import_format)
        report = importer.import_consignments(self._simple_example)

        self._check_errors(report)
        consignment = report.consignments.popitem()[1]

        self._check_reference(consignment)
        self._check_service(consignment)
        self._check_address(consignment)
        self._check_cargo(consignment)
        self._check_shipment_dates(consignment)
        self._check_instructions(consignment)

    def _check_errors(self, report):
        self.assertEqual(1, len(report.consignments))
        self.assertFalse(report.errors)
        self.assertFalse(report.advisories)

    def _check_reference(self, consignment):
        self.assertEqual("GR221003000", consignment.reference)

    def _check_service(self, consignment):
        self.assertTrue(consignment.service.is_priority())
        self.assertTrue(consignment.service.is_tail_lift_required())

    def _check_address(self, consignment):
        self.assertEqual("Disneyworld", consignment.client_name)
        self.assertEqual("Ryan Matfen", consignment.address.contact_name)
        self.assertEqual("Graylaw Freight Group", consignment.address.name)
        self.assertEqual("Gillibrands Road", consignment.address.line_1)
        self.assertEqual("Skelmersdale", consignment.address.town)
        self.assertEqual("WN8 9TA", consignment.address.post_code)
        self.assertEqual("01695 729101", consignment.address.telephone_number)

    def _check_cargo(self, consignment):
        self.assertEqual(1, len(consignment.cargo))
        self.assertEqual(1, consignment.cargo[0].quantity)
        self.assertEqual("full", consignment.cargo[0].package_type.name)
        self.assertEqual("pallet", consignment.cargo[0].package_type.base_type)

        self.assertEqual(
            "normal", consignment.cargo[0].package_type.oversize_option)

        self.assertTupleEqual(
            (1, 500), consignment.cargo[0].quantity_and_weight)

    def _check_shipment_dates(self, consignment):
        self.assertEqual(6, consignment.shipment_dates.delivery_date.day)
        self.assertEqual(10, consignment.shipment_dates.delivery_date.month)
        self.assertEqual(2022, consignment.shipment_dates.delivery_date.year)

    def _check_instructions(self, consignment):
        self.assertEqual(1, len(consignment.delivery_instructions))
        self.assertEqual("Tail Lift", consignment.delivery_instructions[0])


if __name__ == '__main__':
    unittest.main()
