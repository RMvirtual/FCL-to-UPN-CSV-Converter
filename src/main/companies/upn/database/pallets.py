from src.main.file_system.companies.upn.api import data_structure_files
from src.main.companies.upn.interfaces.pallets import CustPallet, NetworkPallet
from src.main.companies.upn.implementations.pallets.network import factory


class UPNPalletsDatabase:
    def __init__(self):
        self._data_file = data_structure_files.network_pallet()

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
