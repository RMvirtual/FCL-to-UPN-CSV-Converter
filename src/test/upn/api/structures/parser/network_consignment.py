import datetime
import unittest
from src.main.upn.api.structures.network_consignment.structure \
    import NetworkConsignment

from src.main.upn.api.parser.network_consignment \
    import NetworkConsignmentParser


class TestNetworkConsignmentParser(unittest.TestCase):
    def setUp(self):
        self._parser = NetworkConsignmentParser()
        self._set_up_raw_network_consignment()
        self._set_up_correct_consignment()

    def _set_up_raw_network_consignment(self):
        self._consignment = self._raw_network_consignment()

    @staticmethod
    def _raw_network_consignment():
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
        self._correct_consignment = self._correct_output()

    @staticmethod
    def _correct_output() -> NetworkConsignment:
        result = NetworkConsignment()
        result.consignment_no = "gr221004388"
        result.depot_no = 75
        result.customer_reference = "49632"
        result.despatch_date = datetime.datetime(2022, 10, 18, 0, 0)
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
        result.customer_name = "GRAYLAW"
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

    def test_should_parse_barcode(self):
        self._parse_and_compare_equality(
            self._parser.consignment_barcode_no,
            self._correct_consignment.consignment_barcode_no
        )

    def test_should_parse_consignment_no(self):
        self._parse_and_compare_equality(
            self._parser.consignment_no,
            self._correct_consignment.consignment_no
        )

    def test_should_parse_customer_name(self):
        self._parse_and_compare_equality(
            self._parser.customer_name,
            self._correct_consignment.customer_name
        )

    def test_should_parse_customer_id(self):
        self._parse_and_compare_equality(
            self._parser.customer_id,
            self._correct_consignment.customer_id
        )

    def test_should_parse_depot_no(self):
        self._parse_and_compare_equality(
            self._parser.depot_no,
            self._correct_consignment.depot_no
        )

    def test_should_parse_despatch_date(self):
        self._parse_and_compare_equality(
            self._parser.despatch_date,
            self._correct_consignment.despatch_date
        )

    def test_should_parse_delivery_name(self):
        self._parse_and_compare_equality(
            self._parser.delivery_name,
            self._correct_consignment.delivery_name
        )

    def test_should_parse_delivery_address_1(self):
        self._parse_and_compare_equality(
            self._parser.delivery_address_1,
            self._correct_consignment.delivery_address_1
        )

    def test_should_parse_delivery_address_2(self):
        self._parse_and_compare_equality(
            self._parser.delivery_address_2,
            self._correct_consignment.delivery_address_2
        )

    def test_should_parse_delivery_town(self):
        self._parse_and_compare_equality(
            self._parser.delivery_town,
            self._correct_consignment.delivery_town
        )

    def test_should_parse_delivery_county(self):
        self._parse_and_compare_equality(
            self._parser.delivery_county,
            self._correct_consignment.delivery_county
        )

    def test_should_parse_delivery_post_code(self):
        self._parse_and_compare_equality(
            self._parser.delivery_post_code,
            self._correct_consignment.delivery_post_code
        )

    def test_should_parse_delivery_telephone_no(self):
        self._parse_and_compare_equality(
            self._parser.delivery_telephone_no,
            self._correct_consignment.delivery_telephone_no
        )

    def test_should_parse_total_weight(self):
        self._parse_and_compare_equality(
            self._parser.total_weight,
            self._correct_consignment.total_weight
        )

    def test_should_parse_special_instructions(self):
        self._parse_and_compare_equality(
            self._parser.special_instructions,
            self._correct_consignment.special_instructions
        )

    def test_should_parse_delivery_contact_name(self):
        self._parse_and_compare_equality(
            self._parser.delivery_contact_name,
            self._correct_consignment.delivery_contact_name
        )

    def test_should_parse_delivery_country(self):
        self._parse_and_compare_equality(
            self._parser.delivery_country,
            self._correct_consignment.delivery_country
        )

    def test_should_parse_customer_paperwork_pages(self):
        self._parse_and_compare_equality(
            self._parser.customer_paperwork_pages,
            self._correct_consignment.customer_paperwork_pages
        )

    def test_should_parse_main_service(self):
        self._parse_and_compare_equality(
            self._parser.main_service,
            self._correct_consignment.main_service
        )

    def test_should_parse_premium_service(self):
        self._parse_and_compare_equality(
            self._parser.premium_service,
            self._correct_consignment.premium_service
        )

    def test_should_parse_tail_lift_required(self):
        self._parse_and_compare_equality(
            self._parser.tail_lift_required,
            self._correct_consignment.tail_lift_required
        )

    def test_should_parse_additional_service(self):
        self._parse_and_compare_equality(
            self._parser.additional_service,
            self._correct_consignment.additional_service
        )

    def test_should_parse_delivery_datetime(self):
        self._parse_and_compare_equality(
            self._parser.delivery_datetime,
            self._correct_consignment.delivery_datetime
        )

    def test_should_parse_network_pallets(self):
        pallets = self._parser.pallets(self._consignment)

    def _parse_and_compare_equality(self, parser_callback, correct_value):
        self.assertEqual(parser_callback(self._consignment), correct_value)


if __name__ == '__main__':
    unittest.main()
