import unittest

from src.main.companies.bridges.graylaw.graylaw.forward_office\
    .consignment_import.controllers.controller \
    import FCLImportController

from src.test.companies.bridges.graylaw.forward_office.consignment_import\
    .controllers.single_line_example import \
    setup


class TestCanImportOneLinerConsignment(unittest.TestCase):
    def setUp(self) -> None:
        self._import_format = setup.import_format()
        self._consignment_input = setup.consignments_to_import()

    def test_should_import_one_liner_consignment(self):
        importer = FCLImportController(self._import_format)
        report = importer.import_consignments(self._consignment_input)

        self._check_errors(report)
        consignment = report.consignments.popitem()[1]
        self._check_consignment(consignment)

    def _check_errors(self, report):
        self.assertEqual(1, len(report.consignments))
        self.assertFalse(report.errors)
        self.assertFalse(report.advisories)

    def _check_consignment(self, consignment):
        self._check_reference(consignment)
        self._check_service(consignment)
        self._check_address(consignment)
        self._check_cargo(consignment)
        self._check_shipment_dates(consignment)
        self._check_instructions(consignment)

    def _check_reference(self, consignment):
        consignment_reference = str(consignment.references.consignment)
        self.assertEqual("GR221003000", consignment_reference)

    def _check_service(self, consignment):
        self.assertTrue(consignment.service.is_priority())
        self.assertTrue(consignment.service.is_tail_lift_required())

    def _check_address(self, consignment):
        self.assertEqual("Disneyworld", consignment.client_name)
        self.assertEqual("Ryan Matfen", consignment.address.contact_name)
        self.assertEqual("Graylaw Freight Group", consignment.address.name)
        self.assertEqual("Gillibrands Road", consignment.address.lines[0])
        self.assertEqual("Skelmersdale", consignment.address.town)
        self.assertEqual("WN8 9TA", consignment.address.post_code)
        self.assertEqual("01695 729101", consignment.address.telephone_number)

    def _check_cargo(self, consignment):
        self.assertEqual(1, len(consignment.cargo))
        cargo_entry = consignment.cargo[0]
        self.assertEqual(1, cargo_entry.quantity)
        self.assertEqual("full", cargo_entry.package_type.name)
        self.assertEqual("pallet", cargo_entry.package_type.base_type)

        oversize_option = cargo_entry.package_type.oversize.selected.name
        self.assertEqual("normal", oversize_option)
        self.assertEqual(1, cargo_entry.quantity)
        self.assertEqual(500, cargo_entry.weight)

    def _check_shipment_dates(self, consignment):
        self.assertEqual(6, consignment.shipment_dates.delivery_date.day)
        self.assertEqual(10, consignment.shipment_dates.delivery_date.month)
        self.assertEqual(2022, consignment.shipment_dates.delivery_date.year)

    def _check_instructions(self, consignment):
        self.assertEqual(1, len(consignment.delivery_instructions))
        self.assertEqual("Tail Lift", consignment.delivery_instructions[0])


if __name__ == '__main__':
    unittest.main()
