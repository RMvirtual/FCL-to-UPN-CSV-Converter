from src.main.file_system.freight import cargo_types
from src.main.freight.cargo.metrics.dimensions import DimensionsInMetres
from src.main.freight.cargo.packages.oversize import factory
from src.main.freight.cargo.packages.types.package_types import (
    PackageType, PackageDefinitions)


def load(package_type_name: str) -> PackageType:
    matching_types = _matching_package_types(package_type_name)

    if not matching_types:
        raise ValueError("Package type does not exist.")

    return matching_types.pop()


def _matching_package_types(type_name: str) -> list[PackageType]:
    return list(filter(
        lambda package_type: package_type.name == type_name, _package_types()))


def _package_types() -> list[PackageType]:
    return list(map(_deserialise, cargo_types.base_packages_file()))


def _deserialise(package_definitions: dict[str, str]) -> PackageType:
    return PackageType(_deserialise_fields(package_definitions))


def _deserialise_fields(definitions: dict[str, str]) -> PackageDefinitions:
    result = PackageDefinitions()
    result.name = definitions["name"]
    result.base_type = definitions["type"]
    result.oversize_options = factory.options_by_base_type(result.base_type)
    result.max_dimensions = _deserialise_dimensions(definitions)
    result.maximum_weight = definitions["maximum_weight"]
    result.override_options = definitions["override_options"]

    return result


def _deserialise_dimensions(definitions: dict[str, str]) -> DimensionsInMetres:
    result = DimensionsInMetres()
    result.length = definitions["maximum_length"]
    result.width = definitions["maximum_width"]
    result.height = definitions["maximum_height"]

    return result
