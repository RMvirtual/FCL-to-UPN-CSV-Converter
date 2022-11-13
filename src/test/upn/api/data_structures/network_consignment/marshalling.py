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

    def _set_up_raw_network_consignment(self):
        self._raw_consignment = {
            'ConBarcode': 'W213359799C',
            'ConNo': 'gr221004388',
            'Consignor': 'GRAYLAW',
            'CustPaperwork': 0,
            'CustRef': '49632',
            'CustomerID': 4236,
            'DeliveryAdd1': 'GRAYLAW FREIGHT TERMINAL',
            'DeliveryAdd2': 'GILLBRANDS ROAD',
            'DeliveryCoName': 'GRAYLAW FREIGHT GROUP',
            'DeliveryContactName': 'Katherine   01695 729101',
            'DeliveryCountry': 'UNITED KINGDOM',
            'DeliveryCounty': 'LANCS',
            'DeliveryDateTime': datetime.datetime(2022, 10, 18, 16, 30),
            'DeliveryPhone': '0',
            'DeliveryPostcode': 'WN8  9TA',
            'DeliveryTown': 'SKELMERSDALE',
            'Depot': 75,
            'DespatchDate': datetime.datetime(2022, 10, 18, 0, 0),
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
        self._correct_consignment.customer_paperwork_pages = 0

        """
        self._correct_consignment.delivery_name = "GRAYLAW FREIGHT GROUP"
        self._correct_consignment.delivery_address_1 = (
            "GRAYLAW FREIGHT TERMINAL")

        self._correct_consignment.delivery_address_2 = "GILLBRANDS ROAD"
        self._correct_consignment.delivery_town = "SKELMERSDALE"
        self._correct_consignment.delivery_county = "LANCS"
        self._correct_consignment.delivery_post_code = "WN8  9TA"
        self._correct_consignment.delivery_telephone_no = "0"
        self._correct_consignment.total_weight = 11000
        self._correct_consignment.special_instructions = (
            "Don't smash up this consignment.")

        self._correct_consignment.customer_id = 4236
        self._correct_consignment.customer_name = "GRAYLAW"
        self._correct_consignment.delivery_contact_name = (
            "Katherine 01695 729101")
        self._correct_consignment.delivery_country = "UNITED KINGDOM"
        self._correct_consignment.main_service = "P"
        self._correct_consignment.premium_service = None
        self._correct_consignment.tail_lift_required = None
        self._correct_consignment.additional_service = None

        self._correct_consignment.despatch_date = (
            datetime.datetime(2022, 10, 18, 0, 0))

        self._correct_consignment.delivery_datetime = (
            datetime.datetime(2022, 10, 18, 16, 30))

        """

    def _set_up_references(self):
        self._correct_consignment.references.consignment_no = "gr221004388"
        self._correct_consignment.references.customer_reference = "49632"
        self._correct_consignment.references.barcode = "W213359799C"


if __name__ == '__main__':
    unittest.main()
