from src.main.file_system.freight import oversize_options

from src.main.freight.cargo.packages.oversize.options import (
    OversizeOptions, OversizeOption)


def all_options() -> dict[str, OversizeOptions]:
    results = {}

    for package_type in oversize_options.contents():
        base_type = package_type["base_type"]
        results[base_type] = _deserialise_base_type(package_type)

    return results


def options_by_base_type(base_type_name: str) -> OversizeOptions:
    return all_options()[base_type_name]


def _deserialise_base_type(values: dict[str, any]) -> OversizeOptions:
    options = _deserialise_options(values)

    defaults = list(filter(
        lambda option: option.name == values["default"], options))

    return OversizeOptions(default=defaults[0], options=options)


def _deserialise_options(values: dict[str, any]) -> list[OversizeOption]:
    return [
        OversizeOption(name=option["name"], multiplier=option["multiplier"])
        for option in values["options"]
    ]
