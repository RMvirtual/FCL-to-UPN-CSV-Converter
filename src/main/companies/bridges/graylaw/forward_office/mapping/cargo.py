import dataclasses
import copy

from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.companies.graylaw.packages.types import database
from src.main.file_system.companies.forward_office import freight_mappings


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
        package = self._deserialise_to_house_package(short_code_to_map)

        self._mappings.append([
            short_code,
            PackageType,
            dataclasses.field(default=package)
        ])

    @staticmethod
    def _deserialise_to_house_package(
            short_code_to_map: dict[str, any]) -> PackageType:
        mapping = short_code_to_map["maps_to"]

        result = database.load(mapping["name"])
        result.oversize.select(mapping["oversize_option"])

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
