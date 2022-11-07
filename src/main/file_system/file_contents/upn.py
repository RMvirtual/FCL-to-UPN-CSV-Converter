import dataclasses
from src.main.file_system.file_readers import runfiles


@dataclasses.dataclass
class MappingValues:
    type: str = ""
    mapping: str = ""
    values: list = None


def network_consignment_contents():
    contents = runfiles.load_json_file(
        "resources/upn/api_structures/network_consignment.json")

    fields = []

    for field_name, mapping_values in list(contents.items()):
        field = [field_name, MappingValues, _mapping_values(mapping_values)]
        fields.append(field)

    return fields


def _mapping_values(values: dict):
    result = MappingValues()
    result.type = values["type"]
    result.mapping = values["mapping"]
    result.values = values["values"] if "values" in values else []

    return result


NetworkConsignment = dataclasses.make_dataclass(
    cls_name="NetworkConsignment",
    fields=network_consignment_contents()
)
