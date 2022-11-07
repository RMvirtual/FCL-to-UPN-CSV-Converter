import dataclasses
from src.main.file_system.file_readers import runfiles


@dataclasses.dataclass
class MappingValues:
    type: str = ""
    mapping: str = ""
    values: list = None


def network_consignment_contents():
    contents = runfiles.load_json_file(
        "resources/upn/network_consignment.json")

    for item in contents:
        entry = dataclasses.make_dataclass(
            cls_name=item,
            fields=[]
        )

NetworkConsignment = dataclasses.make_dataclass(
    cls_name="NetworkConsignment",
    fields=network_consignment_contents()
)

def cargo_type_mappings():
    relative_path = system_files.load_path("FCL_CARGO_TYPE_MAPPINGS")

    return runfiles.load_json_file(relative_path)


def service_code_mappings():
    relative_path = system_files.load_path("FCL_SERVICE_CODE_MAPPINGS")

    return runfiles.load_json_file(relative_path)


def _format_files():
    relative_path = system_files.load_path("FCL_DASHBOARD_FORMATS")
    contents = runfiles.load_json_file(relative_path)

    return [[item, str, contents[item]] for item in contents]


DashboardFormatFiles = dataclasses.make_dataclass(
    cls_name="DashboardFormatFiles",
    fields=_format_files()
)
