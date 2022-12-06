from src.main.companies.upn.interfaces.address import UPNAddressable
from src.main.companies.upn.implementations.address.address import UPNAddress

from src.main.companies.upn.api.marshalling.unmarshaller \
    import UPNAPIUnmarshaller


class UPNDeliveryAddressUnmarshaller(UPNAPIUnmarshaller):
    def __init__(self):
        super().__init__()

    def delivery_address(
            self, candidate: dict[str, any]) -> UPNAddressable:
        result = UPNAddress()
        result.name = self.unmarshall(candidate, "delivery_name")
        result.line_1 = self.unmarshall(candidate, "delivery_address_1")
        result.line_2 = self.unmarshall(candidate, "delivery_address_2")
        result.town = self.unmarshall(candidate, "delivery_town")
        result.county = self.unmarshall(candidate, "delivery_county")
        result.post_code = self.unmarshall(candidate, "delivery_post_code")
        result.country = self.unmarshall(candidate, "delivery_country")

        result.contact_name = self.unmarshall(
            candidate, "delivery_contact_name")

        result.telephone_no = self.unmarshall(
            candidate, "delivery_telephone_no")

        return result
