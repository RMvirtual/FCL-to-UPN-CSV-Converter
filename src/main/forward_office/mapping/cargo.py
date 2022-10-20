import dataclasses
import copy

from src.main.freight.cargo.types import load_package_type, PackageType
from src.main.file_system.file_contents import forward_office


class CargoTypeMapBuilder:
    def __init__(self):
        self._build_map()

    def _build_map(self):
        self._mappings = []
        self._parse_mappings()

    def _parse_mappings(self):
        for short_code_to_map in forward_office.cargo_type_mappings():
            self._add(short_code_to_map)

    def _add(self, short_code_to_map):
        short_code = short_code_to_map["short_code"]
        package_type = self._package_type_from_mapping_details(
            short_code_to_map)

        self._mappings.append([
            short_code,
            PackageType,
            dataclasses.field(default=package_type)
        ])

    @staticmethod
    def _package_type_from_mapping_details(short_code_to_map):
        mapping_info = short_code_to_map["maps_to"]

        result = load_package_type(mapping_info["name"])
        result.oversize_option = mapping_info["oversize_option"]

        return result

    def mappings(self):
        return copy.copy(self._mappings)


FclCargoTypeMap = dataclasses.make_dataclass(
    cls_name="FclCargoTypeMap",
    fields=CargoTypeMapBuilder().mappings(),
    namespace={
        "contains": lambda self, short_code: hasattr(self, short_code)
    }
)
