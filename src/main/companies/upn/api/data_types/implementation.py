import datetime
from src.main.companies.upn.api.data_types.interface import DataTypesContainer
from src.main.companies.upn.api.data_types.validation import DataTypesValidator


class APIDataTypes(DataTypesContainer):
    def __init__(self) -> None:
        self._primitives = {
            "string": str,
            "int": int,
            "datetime": datetime.datetime
        }

        self._containers = {
            "dictionary": dict,
            "array": list
        }

        self._validator = DataTypesValidator(self)

    def type(self, type_name: str) -> type:
        return self[type_name]

    def instance(self, type_name: str, value=None) -> any:
        result_type = self[type_name]

        return result_type(value) if value else result_type()

    def is_container(self, type_name: str) -> bool:
        return type_name in self._containers

    def is_primitive(self, type_name: str) -> bool:
        return type_name in self._primitives

    def _contains(self, data_type: str) -> bool:
        return data_type in self._primitives or data_type in self._containers

    def _get(self, data_type: str) -> type:
        self._validator.assert_data_type_is_valid(data_type)

        return (
            self._containers[data_type] if self.is_container(data_type)
            else self._primitives[data_type]
        )

    def __contains__(self, data_type: str) -> bool:
        return self._contains(data_type)

    def __getitem__(self, data_type: str) -> type:
        return self._get(data_type)
