from __future__ import annotations


class OversizeOption:
    def __init__(self):
        self._name: str = ""
        self._package_multipliers: dict[str, float] = {}

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_option: str) -> None:
        self._name = new_option

    @property
    def package_multipliers(self) -> dict[str, float]:
        return self._package_multipliers

    @package_multipliers.setter
    def package_multipliers(self, new_multipliers: dict[str, float]) -> None:
        self._package_multipliers = new_multipliers

    def __getitem__(self, option_name: str) -> float:
        return self._package_multipliers[option_name]

    def __eq__(self, other: OversizeOption) -> bool:
        return self._name == other.name
