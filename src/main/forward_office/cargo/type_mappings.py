import dataclasses
import json
import copy

from src.main.file_system import runfiles, system_files
from src.main.freight.cargo.types import load_package_type, PackageType


class CargoTypeMappingLoader:
    def __init__(self):
        self._load()

    def _load(self):
        self._mappings = []
        self._parse_short_codes_to_package_types()
        # self._add_all()

    def _parse_short_codes_to_package_types(self):
        self._short_codes_to_package_types = {}

        for package_type in self._mapping_file_contents():
            self._parse_package(package_type)

    def _parse_package(self, package_type):
        short_code = package_type["short_code"]
        mapping_info = package_type["maps_to"]

        the_type = load_package_type(mapping_info["name"])
        the_type.oversize_option = mapping_info["oversize_option"]

        self._mappings.append([
            short_code,
            PackageType,
            dataclasses.field(default=the_type)
        ])

        self._short_codes_to_package_types[short_code] = the_type

    def _add_all(self):
        self._mappings = []

        for short_code in self._short_codes_to_package_types:
            self._add(short_code)

    def _add(self, short_code):
        mapping_details = self._short_codes_to_package_types[short_code]

        self._mappings.append([
            short_code,
            PackageType,
            dataclasses.field(default=mapping_details)
        ])

    def _mapping_file_contents(self):
        with open(self._file_path()) as json_file:
            contents = json.load(json_file)

        return contents

    @staticmethod
    def _file_path():
        relative_path = system_files.load_path("FCL_CARGO_TYPE_MAPPINGS")

        return runfiles.load_path(relative_path)

    def all(self):
        return copy.copy(self._mappings)


FclCargoTypeMap = dataclasses.make_dataclass(
    cls_name="FclCargoTypeMap",
    fields=CargoTypeMappingLoader().all()
)
