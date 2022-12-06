from src.main.companies.upn.interfaces.api.customer import CustomerDetails


class UPNCustomer(CustomerDetails):
    def __init__(self, customer_name: str, customer_id: int) -> None:
        self._name = customer_name
        self._id = customer_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> int:
        return self._id
