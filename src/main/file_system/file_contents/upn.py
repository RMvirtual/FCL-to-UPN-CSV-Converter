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

    for key, values in list(contents.items()):
        field = [key, MappingValues, MappingValues()]
        print(field)
        fields.append(field)

    return fields


NetworkConsignment = dataclasses.make_dataclass(
    cls_name="NetworkConsignment",
    fields=network_consignment_contents()
)
