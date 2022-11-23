from src.main.graylaw.cargo.entries.interface import CargoEntry


def assert_type_is_cargo_entry(entry: any) -> None:
    if not isinstance(entry, CargoEntry):
        raise TypeError("Type", type(entry), "is not a cargo entry.")
