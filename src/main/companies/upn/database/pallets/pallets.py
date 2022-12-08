from src.main.companies.upn.api.interface.pallets.upload import UploadPallet
from src.main.companies.upn.api.interface.pallets.download import DownloadPallet
from src.main.companies.upn.api.implementation.pallets.download import factory
from src.main.file_system.companies.upn.api.pallets.network \
    import NetworkPalletFiles


class UPNPalletsDatabase:
    """Factory for loading pallet types from UPN system configuration."""
    def __init__(self):
        self._data_file = NetworkPalletFiles()

    def network_pallet(self) -> DownloadPallet:
        return self._deserialise_network_pallet()

    def customer_pallet(self) -> UploadPallet:
        ...

    def _deserialise_network_pallet(self) -> DownloadPallet:
        constraints = self._data_file.constraints
        keys = self._data_file.keys

        return factory.network_pallet(
            type_name="FULL", size_name="N",
            type_constraints=constraints[keys["type"]]["values"],
            size_constraints=constraints[keys["size"]]["values"],
        )
