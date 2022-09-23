import dataclasses
import json

from src.main.file_system import runfiles, system_paths
from src.main.freight.cargo.types import load_package_type, PackageType

cargo_type_mappings_file = system_paths.load_path("FCL_CARGO_TYPE_MAPPINGS")
full_path = runfiles.load_path(cargo_type_mappings_file)

with open(full_path) as json_file:
    contents = json.load(json_file)

packages = {}

for package_type in contents:
    the_type = load_package_type(package_type["maps_to"]["name"])
    packages[package_type["short_code"]] = the_type

field_interpretation = []

for package_type in packages:
    field_interpretation.append([
        package_type,
        PackageType,
        dataclasses.field(default_factory=lambda: packages[package_type])
    ])

FclCargoTypeMappings = dataclasses.make_dataclass(
    cls_name="FclCargoTypeMappings",
    fields=field_interpretation
)

"""
format_files = DashboardFormatFiles()
formats = []

for format_field in dataclasses.fields(format_files):
    full_format_path = runfiles.load_path(
        getattr(format_files, format_field.name))

    with open(full_format_path) as json_stream:
        format_contents = json.load(json_stream)

    formats.append([
        format_field.name,
        dict[str, int],
        dataclasses.field(default_factory=lambda: format_contents)
    ])

FclCargoTypeMappings = dataclasses.make_dataclass(
    cls_name="FclCargoTypeMappings",
    fields=formats
)
"""