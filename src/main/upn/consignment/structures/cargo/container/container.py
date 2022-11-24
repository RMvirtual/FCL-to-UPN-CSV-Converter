import dataclasses
from src.main.upn.consignment.structures.cargo.package.pallet.interface \
    import UPNPallet


@dataclasses.dataclass
class UPNCargo:
    total_weight: int = 0
    pallets: list[UPNPallet] = dataclasses.field(
        default_factory=list[UPNPallet])
