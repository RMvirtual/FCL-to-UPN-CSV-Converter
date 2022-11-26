import dataclasses
from src.main.upn.api.interfaces.pallets.upn_pallet import UPNPalletInterface


@dataclasses.dataclass
class UPNCargo:
    total_weight: int = 0
    pallets: list[UPNPalletInterface] = dataclasses.field(default_factory=list)
