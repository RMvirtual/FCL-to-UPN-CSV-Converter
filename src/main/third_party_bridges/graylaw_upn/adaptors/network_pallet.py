from src.main.file_system.upn.api import data_structure_files
from src.main.freight.cargo.packages.oversize.interface import OversizeOptions
from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.graylaw.packages.types import database as graylaw_packages
from src.main.metrics.dimensions.implementation import Dimensions
from src.main.upn.api.interfaces.pallets.upn_pallet import UPNPalletInterface


class NetworkPalletAdaptor(PackageType):
    def __init__(self, network_pallet: UPNPalletInterface):
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
    def _convert_to_graylaw_package(pallet: UPNPalletInterface) -> PackageType:
        mapping = data_structure_files.package_type_mappings()

        package_name = mapping["types"][pallet.type]
        result = graylaw_packages.load(package_name)

        oversize_option = mapping["oversize_options"][pallet.size]
        result.oversize.select(oversize_option)

        return result
