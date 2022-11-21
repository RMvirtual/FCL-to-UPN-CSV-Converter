from src.main.file_system.graylaw import cargo_types
from src.main.graylaw.cargo.metrics.dimensions import DimensionsInMetres
from src.main.graylaw.cargo.packages.oversize import factory
from src.main.graylaw.cargo.packages.types.interface import PackageType
from src.main.graylaw.cargo.packages.types.builder import PackageTypeBuilder


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


def _deserialise(definitions: dict[str, str]) -> PackageType:
    builder = PackageTypeBuilder()

    builder.set_name(definitions["name"])
    builder.set_base_type(definitions["type"])

    options = factory.options_by_base_type(definitions["type"])
    builder.set_oversize_options(options)

    builder.set_max_dimensions(_deserialise_dimensions(definitions))
    builder.set_max_weight(definitions["maximum_weight"])
    builder.set_overrides(definitions["override_options"])

    return builder.build()


def _deserialise_dimensions(definitions: dict[str, str]) -> DimensionsInMetres:
    result = DimensionsInMetres()
    result.length = definitions["maximum_length"]
    result.width = definitions["maximum_width"]
    result.height = definitions["maximum_height"]

    return result
