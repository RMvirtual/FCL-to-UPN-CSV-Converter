import dataclasses


@dataclasses.dataclass
class Cargo:
    total_weight: int = 0
    pallets: list = dataclasses.field(default_factory=list)
