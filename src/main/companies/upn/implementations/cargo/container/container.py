import dataclasses
from src.main.companies.upn.interfaces.pallets import UPNPallet


@dataclasses.dataclass
class UPNCargo:
    total_weight: int = 0
    pallets: list[UPNPallet] = dataclasses.field(default_factory=list)
