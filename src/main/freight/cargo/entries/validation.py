import dataclasses


# noinspection PyClassHasNoInit
@dataclasses.dataclass
class CargoErrors:
    blank_line: bool = False
    blank_package_type: bool = False
    weight_incorrect: bool = False
    invalid_quantity: bool = False
    invalid_package_type: bool = False

    def __bool__(self):
        return any(self._error_values())

    def __len__(self):
        return sum(self._error_values())

    def reset(self):
        for error in self._error_types():
            setattr(self, error.name, False)

    def _error_types(self):
        return dataclasses.fields(self)

    def _error_values(self) -> tuple[bool]:
        return (getattr(self, error.name) for error in self._error_types())

    def are_critical(self) -> bool:
        return bool(self) and not self.blank_line


class CargoValidationStrategy:
    def __init__(self):
        pass

    def validate(self, quantity, package_type, weight) -> bool:
        return(
            self.validate_package_type(package_type)
            and self.validate_weight(weight)
            and self.validate_quantity(quantity)
        )

    def validate_package_type(self, package_type) -> bool:
        return bool(package_type)

    def validate_quantity(self, quantity) -> bool:
        return bool(quantity)

    def validate_weight(self, weight) -> bool:
        return bool(weight)
