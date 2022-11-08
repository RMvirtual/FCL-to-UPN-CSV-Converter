import dataclasses
import datetime
import unittest
from src.main.upn.api.parser import UpnApiParser
from src.main.upn.api.structures import NetworkConsignment
from src.main.upn.api.structures import network_consignment_fields


class TestUpnApiParser(unittest.TestCase):
    @staticmethod
    def _set_up_network_consignment():
        return {
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
            'Despatchdate': datetime.datetime(2022, 10, 18, 0, 0),
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

    @staticmethod
    def _correct_output() -> NetworkConsignment:
        result = NetworkConsignment()
        result.consignment_no = "gr221004388"
        result.depot_no = 75
        result.customer_reference = "49632"
        result.despatch_date = datetime.datetime(2022, 10, 18, 0, 0),
        result.delivery_name = "GRAYLAW FREIGHT GROUP"
        result.delivery_address_1 = "GRAYLAW FREIGHT TERMINAL"
        result.delivery_address_2 = "GILLBRANDS ROAD"
        result.delivery_town = "SKELMERSDALE"
        result.delivery_county = "LANCS"
        result.delivery_post_code = "WN8  9TA"
        result.delivery_telephone_no = "0"
        result.total_weight = 11000
        result.special_instructions = "Don't smash up this consignment."
        result.customer_id = 4236
        result.delivery_contact_name = "Katherine   01695 729101"
        result.delivery_country = "UNITED KINGDOM"
        result.customer_paperwork_pages = 0
        result.main_service = "P"
        result.premium_service = None
        result.tail_lift_required = None
        result.additional_service = None
        result.delivery_datetime = datetime.datetime(2022, 10, 18, 16, 30)
        result.consignment_barcode_no = "W213359799C"

        return result

    def _validate(self, consignment: NetworkConsignment):
        self.assertEqual(self._correct_output(), consignment)

    def test_should_parse_network_consignment(self):
        #self._set_up_network_consignment()
        #parser = UpnApiParser()
        network_consignment_fields()
        #result = parser.network_consignment(
        # self._set_up_network_consignment())
        # self._validate(result)
        self.fail("DUMMY FAIL")

if __name__ == '__main__':
    unittest.main()
