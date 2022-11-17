from __future__ import annotations
from src.main.freight.cargo.packages.oversize import interface


class OversizeOption(interface.OversizeOption):
    def __init__(self, name: str, multiplier: float):
        self._name = name
        self._multiplier = multiplier

    @property
    def name(self) -> str:
        return self._name

    @property
    def multiplier(self) -> float:
        return self._multiplier

