import dataclasses
import json
import copy

from src.main.file_system import runfiles, system_paths
from src.main.freight.cargo.types import load_package_type, PackageType

cargo_type_mappings_file = system_paths.load_path("FCL_CARGO_TYPE_MAPPINGS")
full_path = runfiles.load_path(cargo_type_mappings_file)

with open(full_path) as json_file:
    contents = json.load(json_file)

short_codes_to_package_types = {}

for package_type in contents:
    short_code = package_type["short_code"]
    mapping_info = package_type["maps_to"]

    the_type = load_package_type(mapping_info["name"])
    the_type.oversize_option = mapping_info["oversize_option"]

    short_codes_to_package_types[short_code] = the_type

field_interpretation = []

for short_code in short_codes_to_package_types:
    package_type = short_codes_to_package_types[short_code]

    field_interpretation.append([
        short_code,
        PackageType,
        dataclasses.field(default=package_type)
    ])

FclCargoTypeMap = dataclasses.make_dataclass(
    cls_name="FclCargoTypeMap",
    fields=field_interpretation
)
