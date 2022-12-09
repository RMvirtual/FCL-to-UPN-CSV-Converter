from src.main.file_system.companies.upn import system_import
from src.main.freight.cargo.packages.oversize.interface import OversizeOptions
from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.companies.graylaw.packages.types import database
from src.main.metrics.dimensions.implementation import Dimensions
from src.main.companies.upn.api.interface.cargo.pallets.base import UPNPallet


class NetworkPalletAdaptor(PackageType):
    def __init__(self, network_pallet: UPNPallet):
        self._pallet = self._convert_to_graylaw_package(network_pallet)

    @property
    def name(self) -> str:
        return self._pallet.name

    @property
    def base_type(self) -> str:
        return self._pallet.base_type

    @property
    def oversize(self) -> OversizeOptions:
        return self._pallet.oversize

    @property
    def maximum_dimensions(self) -> Dimensions:
        return self._pallet.maximum_dimensions

    @property
    def maximum_weight(self) -> float:
        return self._pallet.maximum_weight

    @property
    def override_options(self) -> list:
        return self._pallet.override_options

    @staticmethod
    def _convert_to_graylaw_package(pallet: UPNPallet) -> PackageType:
        mapping = system_import.package_type_mappings()

        package_name = mapping["types"][pallet.type]
        result = database.load(package_name)

        oversize_option = mapping["oversize_options"][pallet.size]
        result.oversize.select(oversize_option)

        return result
