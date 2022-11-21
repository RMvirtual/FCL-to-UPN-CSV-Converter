from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.freight.cargo.packages.oversize.interface import OversizeOptions
from src.main.freight.cargo.metrics.dimensions import Dimensions

from src.main.upn.api.data_structures.network_pallet.interface \
    import NetworkPallet


class NetworkPalletAdaptor(PackageType):
    def __init__(self, network_pallet: NetworkPallet):
        self._network_pallet = network_pallet

    @property
    def name(self) -> str:
        return ""

    @property
    def base_type(self) -> str:
        return ""

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
