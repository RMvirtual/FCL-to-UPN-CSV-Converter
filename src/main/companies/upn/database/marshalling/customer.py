from src.main.companies.upn.api.marshalling.controller.unmarshaller \
    import UPNAPIUnmarshaller
from src.main.companies.upn.model.implementation.customer.customer \
    import UPNCustomer
from src.main.companies.upn.model.interface.customer.customer \
    import CustomerDetails


class UPNCustomerUnmarshaller(UPNAPIUnmarshaller):
    def __init__(self):
        super().__init__()

    def customer(self, candidate: dict[str, any]) -> CustomerDetails:
        return UPNCustomer(
            customer_name=self.unmarshall(candidate, "customer_name"),
            customer_id=self.unmarshall(candidate, "customer_id")
        )
