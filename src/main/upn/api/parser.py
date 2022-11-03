from src.main.upn.api.consignment import UpnSoapApi
from src.main.freight.consignment.model import Consignment
from src.main.freight.cargo import package_types


class UpnApiParser:
    def __init__(self):
        self._api = UpnSoapApi()

        self._type_map = {
            "Full": "full",
            "Euro": "euro",
            "Half": "half",
            "Quarter": "quarter",
            "Micro": "micro"
        }

        self._size_map = {
            "N": "full",
            "O": "oversize",
            "2": "double",
            "3": "triple"
        }

    def network_input(self, date: str) -> list[Consignment]:
        raw_consignment = self._api.get_network_input(date)

        consignment = Consignment()
        consignment.reference = raw_consignment["ConNo"]

        depot = raw_consignment["Depot"]
        customer_reference = raw_consignment["CustRef"]
        despatch_date = raw_consignment["DespatchDate"]
        delivery_name = raw_consignment["DeliveryCoName"]
        delivery_address_1 = raw_consignment["DeliveryAdd1"]
        delivery_address_2 = raw_consignment["DeliveryAdd2"]
        delivery_town = raw_consignment["DeliveryTown"]
        delivery_county = raw_consignment["DeliveryCounty"]
        delivery_post_code = raw_consignment["DeliveryPostcode"]
        delivery_phone = raw_consignment["DeliveryPhone"]
        total_weight = raw_consignment["TotalWeight"]
        special_instructions = raw_consignment["SpecialInstructions"]
        customer_id = raw_consignment["CustomerID"]
        delivery_contact_name = raw_consignment["DeliveryContactName"]
        delivery_country = raw_consignment["DeliveryCountry"]
        customer_paperwork = raw_consignment["CustPaperwork"]
        main_service = raw_consignment["MainService"]
        premium_service = raw_consignment["PremiumService"]
        tail_lift = raw_consignment["TailLift"]
        extra_service = raw_consignment["ExtraService"]
        delivery_date_time = raw_consignment["DeliveryDateTime"]
        consignment_barcode_no = raw_consignment["ConBarcode"]
        parsed_pallets = self.parse_pallets(raw_consignment)

        return []

    def parse_pallets(self, raw_consignment: dict):
        return [
            self.parse_pallet(pallet) for pallet in raw_consignment["Pallets"]]

    def parse_pallet(self, pallet: dict) -> package_types.PackageType:
        pallet_type = self._type_map[pallet["PalletType"]]
        package_type = package_types.load(pallet_type)
        package_type.oversize_option = self._size_map[pallet["PalletSize"]]

        # Keeping other extract here for reference.
        consignment_barcode = pallet["ConBarcode"]
        barcode_no = pallet["PltBarcode"]

        return package_type
