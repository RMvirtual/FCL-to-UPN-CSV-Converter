from abc import abstractmethod
from src.main.companies.upn.api.data_types.abstract.interface \
    import UPNAPIDataTypes

from src.main.companies.upn.api.data_types.abstract.validation \
    import DataTypesValidator


class DataTypes(UPNAPIDataTypes):
    @abstractmethod
    def __init__(self, names_to_types: dict[str, type]) -> None:
        self._data_types = names_to_types
        self._validator = DataTypesValidator(self)

    def contains(self, data_type: str) -> bool:
        return data_type in self._data_types

    def get(self, data_type: str) -> type:
        self._validator.assert_data_type_is_valid(data_type)

        return self._data_types[data_type]

    def __contains__(self, data_type: str) -> bool:
        return self.contains(data_type)

    def __getitem__(self, data_type: str) -> type:
        return self.get(data_type)
