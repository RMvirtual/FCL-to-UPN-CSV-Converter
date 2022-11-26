import dataclasses
from src.main.upn.freight.cargo.pallet.interface import UPNPalletInterface


@dataclasses.dataclass
class UPNCargo:
    total_weight: int = 0
    pallets: list[UPNPalletInterface] = dataclasses.field(default_factory=list)
