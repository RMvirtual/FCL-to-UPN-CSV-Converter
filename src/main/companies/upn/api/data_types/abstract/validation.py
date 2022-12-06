from src.main.companies.upn.api.data_types.abstract.interface \
    import UPNAPIDataTypes


class InvalidUPNDataType(ValueError):
    def __init__(self, data_type: str):
        super().__init__(f"Type {data_type} is invalid UPN data type.")


class DataTypesValidator:
    def __init__(self, data_types: UPNAPIDataTypes) -> None:
        self._data_types = data_types

    def assert_data_type_is_valid(self, data_type: str) -> None:
        if data_type not in self._data_types:
            raise InvalidUPNDataType(data_type)
