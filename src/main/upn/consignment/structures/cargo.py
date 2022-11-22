import dataclasses
from src.main.upn.api.data_structures.network_pallet.interface \
    import NetworkPallet


@dataclasses.dataclass
class UPNCargo:
    total_weight: int = 0
    pallets: list[NetworkPallet] = dataclasses.field(
        default_factory=list[NetworkPallet])
