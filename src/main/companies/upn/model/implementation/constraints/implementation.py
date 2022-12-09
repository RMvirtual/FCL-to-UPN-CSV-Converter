import copy
from src.main.companies.upn.model.interface.constraints.data \
    import DataConstraint as ConstraintInterface


class DataConstraint(ConstraintInterface):
    def __init__(
            self, const_type: type, const_values: list[any] = None) -> None:
        self._type_constraint = const_type
        self._value_constraints = const_values if const_values else []
        self._assert_values_are_homogenous()

    @property
    def type(self) -> type:
        return self._type_constraint

    @property
    def values(self) -> list[any]:
        return copy.deepcopy(self._value_constraints)

    def _assert_values_are_homogenous(self) -> None:
        for value in self._value_constraints:
            self._assert_value_matches_type_constraint(value)

    def _assert_value_matches_type_constraint(self, value: any) -> None:
        if not isinstance(value, self._type_constraint):
            raise TypeError(f"Contained type for {value} is not valid.")
