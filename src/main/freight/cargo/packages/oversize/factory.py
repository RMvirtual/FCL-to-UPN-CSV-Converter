from src.main.file_system.freight import oversize_options
from src.main.freight.cargo.packages.oversize.options import OversizeOption


def all_options() -> dict[str, list[OversizeOption]]:
    results = {}

    for entry in oversize_options.contents():
        base_type_name = entry["base_type"]
        results[base_type_name] = _deserialise_options(entry)

    return results


def options_by_base_type(base_type_name: str) -> list[OversizeOption]:
    result = None
    options = all_options()

    for option in options:
        if option == base_type_name:
            result = options[base_type_name]
            break

    return result


def _deserialise_options(values: dict[str, any]) -> list[OversizeOption]:
    return [
        OversizeOption(name=option["name"], multiplier=option["multiplier"])
        for option in values["options"]
    ]
