import dataclasses
from src.main.companies.upn.api.data_types.marshalling \
    import UPNDataTypeMarshaller


@dataclasses.dataclass
class Constraints:
    type: str = ""
    constraints: list[any] = None


class ConstraintsMarshaller:
    def __init__(self):
        self._data_types = UPNDataTypeMarshaller()

    def unmarshal_constraint(self, candidate: dict[str, any]) -> Constraints:
        result = Constraints()

        result.type = self._data_types.unmarshall_type(candidate["type"])
        result.constraints = (
            candidate["constraints"] if "constraints" in candidate else [])

        return result

    def unmarshal_to_dataclass_fields(self, candidate: dict[str, dict]):
        return map(self._json_entry_to_field_values, candidate.items())

    def _json_entry_to_field_values(self, field) -> list[str, any, Constraints]:
        key, value = field

        return [key, Constraints, self.unmarshal_constraint(value)]
