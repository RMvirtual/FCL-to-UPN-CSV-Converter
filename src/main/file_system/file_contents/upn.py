import dataclasses
from src.main.file_system.file_readers import runfiles


@dataclasses.dataclass
class MappingValues:
    type: str = ""
    mapping: str = ""
    values: list = None


def network_consignment_contents():
    return extract_network_consignment_fields(
        _network_consignment_file_contents())


def extract_network_consignment_fields(contents: dict[str, dict]):
    return [_extract_item(field) for field in list(contents.items())]


def _extract_item(field):
    key, value = field

    return [key, MappingValues, _to_mapping_values(value)]


def _to_mapping_values(values: dict):
    result = MappingValues()
    result.type = values["type"]
    result.mapping = values["mapping"]
    result.values = values["values"] if "values" in values else []

    return result


def _network_consignment_file_contents():
    return runfiles.load_json_file(
        "resources/upn/api_structures/network_consignment.json")


NetworkConsignment = dataclasses.make_dataclass(
    cls_name="NetworkConsignment",
    fields=network_consignment_contents()
)
