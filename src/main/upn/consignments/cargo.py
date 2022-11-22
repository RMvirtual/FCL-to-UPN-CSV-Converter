import dataclasses


@dataclasses.dataclass
class UPNCargo:
    total_weight: int = 0
    pallets: list = dataclasses.field(default_factory=list)
