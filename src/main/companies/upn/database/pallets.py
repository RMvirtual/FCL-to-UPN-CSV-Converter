from src.main.file_system.companies.upn import api
from src.main.companies.upn.interfaces.api.pallets \
    import CustPallet, NetworkPallet
from src.main.companies.upn.implementations.pallets.network import factory


class UPNPalletsDatabase:
    """Factory for loading pallet types from UPN system configuration."""
    def __init__(self):
        self._data_file = api.network_pallet_constraints()

    def network_pallet(self) -> NetworkPallet:
        return self._deserialise_network_pallet()

    def customer_pallet(self) -> CustPallet:
        ...

    def _deserialise_network_pallet(self) -> NetworkPallet:
        return factory.network_pallet(
            type_name="FULL", size_name="N",
            type_constraints=self._data_file["type"]["values"],
            size_constraints=self._data_file["size"]["values"],
        )
