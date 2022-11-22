import datetime
import unittest

from src.main.upn.api.data_structures.network_consignment.marshalling \
    import UpnNetworkConsignmentMarshaller

from src.main.upn.api.data_structures.network_consignment.implementation \
    import NetworkConsignment

from src.main.upn.api.data_structures.network_pallet.implementation \
    import NetworkPallet


class TestNetworkConsignmentMarshaller(unittest.TestCase):
    def setUp(self) -> None:
        self._set_up_raw_network_consignment()
        self._set_up_correct_consignment()
        self._marshaller = UpnNetworkConsignmentMarshaller()

    def test_should_unmarshall_consignment_references(self) -> None:
        result = self._marshaller.unmarshall_references(self._raw_consignment)

        self.assertEqual(self._correct_consignment.references, result)

    def test_should_unmarshall_depot_no(self) -> None:
        result = self._marshaller.unmarshall_depot_no(self._raw_consignment)

        self.assertEqual(self._correct_consignment.depot_no, result)

    def test_should_unmarshall_customer(self) -> None:
        result = self._marshaller.unmarshall_customer(self._raw_consignment)

        self.assertEqual(self._correct_consignment.customer, result)

    def test_should_unmarshall_delivery_address(self) -> None:
        result = self._marshaller.unmarshall_delivery_address(
            self._raw_consignment)

        self.assertEqual(self._correct_consignment.delivery_address, result)

    def test_should_unmarshall_total_weight(self) -> None:
        result = self._marshaller.unmarshall_total_weight(
            self._raw_consignment)

        self.assertEqual(self._correct_consignment.cargo.total_weight, result)

    def test_should_unmarshall_special_instructions(self) -> None:
        result = self._marshaller.unmarshall_special_instructions(
            self._raw_consignment)

        self.assertEqual(
            self._correct_consignment.special_instructions, result)

    def test_should_unmarshall_customer_paperwork_pages(self) -> None:
        result = self._marshaller.unmarshall_customer_paperwork_pages(
            self._raw_consignment)

        self.assertEqual(
            self._correct_consignment.customer_paperwork_pages, result)

    def test_should_unmarshall_dates(self) -> None:
        result = self._marshaller.unmarshall_dates(self._raw_consignment)

        self.assertEqual(self._correct_consignment.dates, result)

    def test_should_unmarshall_services(self) -> None:
        result = self._marshaller.unmarshall_services(self._raw_consignment)

        self.assertEqual(self._correct_consignment.services, result)

    def test_should_unmarshall_pallets(self) -> None:
        result = self._marshaller.unmarshall_pallets(self._raw_consignment)

        self.assertEqual(self._correct_consignment.cargo.pallets, result)

    def _set_up_raw_network_consignment(self) -> None:
        self._raw_consignment = {
            'ConBarcode': 'W213359799C',
            'ConNo': 'gr221004388',
            'CustRef': '49632',
            'Depot': 75,
            'CustomerID': 4236,
            'CustPaperwork': 0,
            'Consignor': 'GRAYLAW',
            'DeliveryCoName': 'GRAYLAW FREIGHT GROUP',
            'DeliveryAdd1': 'GRAYLAW FREIGHT TERMINAL',
            'DeliveryAdd2': 'GILLBRANDS ROAD',
            'DeliveryTown': 'SKELMERSDALE',
            'DeliveryCounty': 'LANCS',
            'DeliveryPostcode': 'WN8  9TA',
            'DeliveryCountry': 'UNITED KINGDOM',
            'DeliveryContactName': 'Katherine   01695 729101',
            'DeliveryPhone': '0',
            'DespatchDate': datetime.datetime(2022, 10, 18, 0, 0),
            'DeliveryDateTime': datetime.datetime(2022, 10, 18, 16, 30),
            'MainService': 'P',
            'PremiumService': None,
            'TailLift': None,
            'ExtraService': None,
            'SpecialInstructions': 'Don\'t smash up this adaptors.',
            'Pallets': {
                'NetworkPallet': [
                    {
                        'ConBarcode': 'W213359799C',
                        'PalletSize': 'N',
                        'PalletType': 'FULL',
                        'PltBarcode': 'W213359800P'
                    },
                    {
                        'ConBarcode': 'W213359799C',
                        'PalletSize': 'N',
                        'PalletType': 'FULL',
                        'PltBarcode': 'W213359801P'
                    },
                ]
            },
            'TotalWeight': 11000
        }

    def _set_up_correct_consignment(self):
        self._correct_consignment = NetworkConsignment()
        self._set_up_correct_references()
        self._correct_consignment.depot_no = 75
        self._correct_consignment.customer_paperwork_pages = 0
        self._set_up_correct_customer()
        self._set_up_correct_delivery_address()
        self._set_up_correct_cargo()
        self._set_up_correct_dates()

        self._correct_consignment.special_instructions = (
            "Don't smash up this adaptors.")

        self._set_up_correct_services()

    def _set_up_correct_references(self) -> None:
        self._correct_consignment.references.consignment_no = "gr221004388"
        self._correct_consignment.references.customer_reference = "49632"
        self._correct_consignment.references.barcode = "W213359799C"

    def _set_up_correct_delivery_address(self) -> None:
        address = self._correct_consignment.delivery_address
        address.name = "GRAYLAW FREIGHT GROUP"
        address.line_1 = "GRAYLAW FREIGHT TERMINAL"
        address.line_2 = "GILLBRANDS ROAD"
        address.town = "SKELMERSDALE"
        address.county = "LANCS"
        address.post_code = "WN8  9TA"
        address.country = "UNITED KINGDOM"
        address.contact_name = "Katherine   01695 729101"
        address.telephone_no = "0"

    def _set_up_correct_services(self) -> None:
        self._correct_consignment.services.main_service = "P"
        self._correct_consignment.services.premium_service = None
        self._correct_consignment.services.tail_lift_required = None
        self._correct_consignment.services.additional_service = None

    def _set_up_correct_cargo(self):
        self._correct_consignment.cargo.total_weight = 11000
        self._set_up_correct_pallets()

    def _set_up_correct_customer(self):
        self._correct_consignment.customer.name = "GRAYLAW"
        self._correct_consignment.customer.id = 4236

    def _set_up_correct_dates(self) -> None:
        self._correct_consignment.dates.despatch = datetime.datetime(
            2022, 10, 18, 0, 0)

        self._correct_consignment.dates.delivery = datetime.datetime(
            2022, 10, 18, 16, 30)

    def _set_up_correct_pallets(self) -> None:
        pallet_1 = NetworkPallet()
        pallet_1.consignment_barcode = "W213359799C"
        pallet_1.size = "N"
        pallet_1.type = "FULL"
        pallet_1.barcode = "W213359800P"

        pallet_2 = NetworkPallet()
        pallet_2.consignment_barcode = "W213359799C"
        pallet_2.size = "N"
        pallet_2.type = "FULL"
        pallet_2.barcode = "W213359801P"

        self._correct_consignment.cargo.pallets = [pallet_1, pallet_2]


if __name__ == '__main__':
    unittest.main()
