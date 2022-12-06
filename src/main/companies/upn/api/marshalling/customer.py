from src.main.companies.upn.implementations.customer import UPNCustomer
from src.main.companies.upn.interfaces.api.customer import CustomerDetails

from src.main.companies.upn.api.marshalling.unmarshaller \
    import UPNAPIUnmarshaller


class UPNCustomerUnmarshaller(UPNAPIUnmarshaller):
    def __init__(self):
        super().__init__()

    def customer(self, candidate: dict[str, any]) -> CustomerDetails:
        return UPNCustomer(
            customer_name=self.unmarshall(candidate, "customer_name"),
            customer_id=self.unmarshall(candidate, "customer_id")
        )
