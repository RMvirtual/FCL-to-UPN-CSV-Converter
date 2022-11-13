import datetime
import unittest

from src.main.upn.api.data_structures.network_consignment.marshalling \
    import UpnNetworkConsignmentMarshaller

from src.main.upn.api.data_structures.network_consignment.structure \
    import NetworkConsignment


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

    def test_should_unmarshall_customer_id(self) -> None:
        result = self._marshaller.unmarshall_customer_id(self._raw_consignment)
        self.assertEqual(self._correct_consignment.customer_id, result)

    def test_should_unmarshall_delivery_address(self) -> None:
        result = self._marshaller.unmarshall_delivery_address(
            self._raw_consignment)

        self.assertEqual(self._correct_consignment.delivery_address, result)

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
            'ExtraService': None,
            'MainService': 'P',
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
            'PremiumService': None,
            'SpecialInstructions': 'Don\'t smash up this consignment.',
            'TailLift': None,
            'TotalWeight': 11000
        }

    def _set_up_correct_consignment(self):
        self._correct_consignment = NetworkConsignment()
        self._set_up_references()
        self._correct_consignment.depot_no = 75
        self._correct_consignment.customer_id = 4236
        self._correct_consignment.customer_paperwork_pages = 0
        self._set_up_delivery_address()

        """
        self._correct_consignment.total_weight = 11000
        self._correct_consignment.special_instructions = (
            "Don't smash up this consignment.")

        self._correct_consignment.customer_name = "GRAYLAW"
        self._correct_consignment.main_service = "P"
        self._correct_consignment.premium_service = None
        self._correct_consignment.tail_lift_required = None
        self._correct_consignment.additional_service = None

        self._correct_consignment.despatch_date = (
            datetime.datetime(2022, 10, 18, 0, 0))

        self._correct_consignment.delivery_datetime = (
            datetime.datetime(2022, 10, 18, 16, 30))

        """

    def _set_up_references(self) -> None:
        self._correct_consignment.references.consignment_no = "gr221004388"
        self._correct_consignment.references.customer_reference = "49632"
        self._correct_consignment.references.barcode = "W213359799C"

    def _set_up_delivery_address(self) -> None:
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


if __name__ == '__main__':
    unittest.main()
