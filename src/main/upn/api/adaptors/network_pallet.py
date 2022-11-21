from src.main.graylaw.cargo.packages.types.interface import PackageType
from src.main.graylaw.cargo.packages.oversize.interface import OversizeOptions
from src.main.graylaw.cargo.metrics.dimensions import Dimensions

from src.main.upn.api.data_structures.network_pallet.interface \
    import NetworkPallet

from src.main.graylaw.cargo.packages.types import factory as package_types
from src.main.graylaw.cargo.packages.oversize import factory \
    as oversize_options

from src.main.file_system.upn.api.structures import package_type_mappings


class NetworkPalletAdaptor(PackageType):
    def __init__(self, network_pallet: NetworkPallet):
        self._network_pallet = network_pallet
        self._mapping = package_type_mappings()

    @property
    def name(self) -> str:
        return self._mapping["types"][self._network_pallet.type]

    @property
    def base_type(self) -> str:
        return "pallet"

    @property
    def oversize(self) -> OversizeOptions:
        return None

    @property
    def maximum_dimensions(self) -> Dimensions:
        return None

    @property
    def maximum_weight(self) -> float:
        return 0

    @property
    def override_options(self) -> list:
        return None
