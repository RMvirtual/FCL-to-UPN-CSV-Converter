from src.main.file_system.upn.api.structures import package_type_mappings
from src.main.graylaw.cargo.packages.types.interface import PackageType
from src.main.graylaw.cargo.packages.oversize.interface import OversizeOptions
from src.main.metrics.dimensions.implementation import Dimensions
from src.main.graylaw.cargo.packages.types import factory as graylaw_packages
from src.main.upn.consignment.cargo.package.pallet.interface import UPNPallet


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
        mapping = package_type_mappings()

        package_name = mapping["types"][pallet.type]
        result = graylaw_packages.load(package_name)

        oversize_option = mapping["oversize_options"][pallet.size]
        result.oversize.select(oversize_option)

        return result