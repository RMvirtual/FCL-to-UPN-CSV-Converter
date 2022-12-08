from src.main.companies.upn.api.data_types.implementation import APIDataTypes


class APIDataTypesFactory:
    def __init__(self):
        self._data_types = APIDataTypes()

    def type(self, type_name: str) -> type:
        return self._data_types[type_name]

    def instance(self, type_name: str, value=None) -> any:
        result_type = self._data_types[type_name]

        return result_type(value) if value else result_type()

