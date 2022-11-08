import dataclasses


@dataclasses.dataclass
class MappingValues:
    type: str = ""
    mapping: str = ""
    values: list = None


def _field_values(contents: dict[str, dict]):
    return map(_json_entry_to_field_values, contents.items())


def _json_entry_to_field_values(field) -> list[str, any, MappingValues]:
    key, value = field

    return [key, MappingValues, _to_mapping_values(value)]


def _to_mapping_values(values: dict[str, str or list[str]]) -> MappingValues:
    result = MappingValues()
    result.type = values["type"]
    result.mapping = values["mapping"]
    result.values = values["values"] if "values" in values else []

    return result
