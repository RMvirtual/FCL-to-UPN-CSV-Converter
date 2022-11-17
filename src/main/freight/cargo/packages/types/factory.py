from src.main.file_system.freight import cargo_types
from src.main.freight.cargo.metrics.dimensions import DimensionsInMetres
from src.main.freight.cargo.packages.oversize import factory
from src.main.freight.cargo.packages.types.package_types import PackageType


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


def _deserialise(package_type_definitions: dict[str, str]) -> PackageType:
    result = PackageType()
    result.name = package_type_definitions["name"]
    result.base_type = package_type_definitions["type"]

    result.all_oversize_options = factory.options_by_base_type(
        result.base_type)

    result.maximum_dimensions = DimensionsInMetres()
    result.maximum_dimensions.length = package_type_definitions[
        "maximum_length"]

    result.maximum_dimensions.width = package_type_definitions["maximum_width"]
    result.maximum_dimensions.height = package_type_definitions[
        "maximum_height"]

    result.maximum_weight = package_type_definitions["maximum_weight"]
    result.override_options = package_type_definitions["override_options"]

    return result
