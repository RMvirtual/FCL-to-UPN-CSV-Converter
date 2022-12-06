import copy
from src.main.companies.upn.interfaces.services.service \
    import UPNService as UPNServiceProvider


class UPNService(UPNServiceProvider):
    def __init__(
            self, constraints: list[str], default_value: str = None) -> None:
        if default_value is not None and default_value not in constraints:
            raise ValueError(
                f"Default value {default_value} not found in {constraints}")

        if default_value is None:
            self._selection = constraints[0]

        else:
            self._selection = default_value

        self._constraints = constraints

    def select(self, service_option: str) -> None:
        if service_option not in self._constraints:
            raise ValueError(
                f"Value {service_option} not found in {self._constraints}")

        self._selection = service_option

    @property
    def selection(self) -> str:
        return self._selection

    def constraints(self) -> list[str]:
        return copy.deepcopy(self._constraints)
