from __future__ import annotations
from src.main.graylaw.cargo.packages.oversize import interface


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

    def select(self, option_name: str) -> None:
        self._selected = self[option_name]

    def _contains_option_name(self, name: str) -> bool:
        return bool(self._options_by_name(name))

    def _options_by_name(self, name: str) -> list[interface.OversizeOption]:
        return list(filter(lambda option: option.name == name, self._values))

    def __contains__(self, option: interface.OversizeOption) -> bool:
        if not isinstance(option, interface.OversizeOption):
            raise TypeError("Incorrect oversize option type.")

        return option in self._values

    def __getitem__(self, name: str) -> interface.OversizeOption:
        if not self._contains_option_name(name):
            raise ValueError("Oversize option not found.")

        return self._options_by_name(name).pop()

    def __eq__(self, other: interface.OversizeOptions) -> bool:
        matching_selection = self.selected == other.selected
        matching_values = self.values == other.values

        return matching_selection and matching_values
