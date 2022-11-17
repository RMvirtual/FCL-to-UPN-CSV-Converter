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

    def __eq__(self, other: OversizeOption) -> bool:
        return (
            self._name == other.name and self._multiplier == other.multiplier)


class OversizeOptions(interface.OversizeOptions):
    def __init__(
            self, default: OversizeOption, options: list[OversizeOption]
    ) -> None:
        self._default = default
        self._values = options
        self._selected = self._default

    @property
    def default(self) -> OversizeOption:
        return self._default

    @property
    def values(self) -> list[OversizeOption]:
        return self._values

    @property
    def selected(self) -> OversizeOption:
        return self._selected

    @selected.setter
    def selected(self, option: OversizeOption) -> None:
        if option not in self:
            raise ValueError("Oversize Option not found.")

        self._selected = option

    def __contains__(self, option: interface.OversizeOption) -> bool:
        if type(option) is not OversizeOption:
            raise TypeError("Incorrect oversize option type.")

        return option in self._values
