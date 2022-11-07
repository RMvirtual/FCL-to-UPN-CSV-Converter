import dataclasses
import copy

from src.main.freight.cargo import package_types
from src.main.file_system.file_contents.forward_office import freight_mappings


class CargoTypeMapBuilder:
    def __init__(self):
        self._build_map()

    def _build_map(self):
        self._mappings = []
        self._deserialise_mappings()

    def _deserialise_mappings(self):
        for short_code_to_map in freight_mappings.cargo_type_mappings():
            self._add(short_code_to_map)

    def _add(self, short_code_to_map):
        short_code = short_code_to_map["short_code"]
        package_type = self._package_type_from_mapping_details(
            short_code_to_map)

        self._mappings.append([
            short_code,
            package_types.PackageType,
            dataclasses.field(default=package_type)
        ])

    @staticmethod
    def _package_type_from_mapping_details(short_code_to_map):
        mapping_info = short_code_to_map["maps_to"]

        result = package_types.load(mapping_info["name"])
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
