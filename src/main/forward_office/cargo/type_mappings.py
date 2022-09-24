import dataclasses
import json
import copy

from src.main.file_system import runfiles, system_files
from src.main.freight.cargo.types import load_package_type, PackageType


class CargoTypeMapBuilder:
    def __init__(self):
        self._build_map()

    def _build_map(self):
        self._mappings = []
        self._parse_mappings()

    def _parse_mappings(self):
        for mapping_details in self._mapping_file_contents():
            self._add(mapping_details)

    def _add(self, mapping_details):
        short_code = mapping_details["short_code"]
        package_type = self._package_type_from_mapping_details(mapping_details)

        self._mappings.append([
            short_code,
            PackageType,
            dataclasses.field(default=package_type)
        ])

    @staticmethod
    def _package_type_from_mapping_details(mapping_details):
        mapping_info = mapping_details["maps_to"]

        package_type = load_package_type(mapping_info["name"])
        package_type.oversize_option = mapping_info["oversize_option"]

        return package_type

    def _mapping_file_contents(self):
        with open(self._file_path()) as json_file:
            return json.load(json_file)

    @staticmethod
    def _file_path():
        relative_path = system_files.load_path("FCL_CARGO_TYPE_MAPPINGS")

        return runfiles.load_path(relative_path)

    def mappings(self):
        return copy.copy(self._mappings)


FclCargoTypeMap = dataclasses.make_dataclass(
    cls_name="FclCargoTypeMap",
    fields=CargoTypeMapBuilder().mappings()
)
