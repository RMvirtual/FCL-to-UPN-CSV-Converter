import copy


class ItemConstraint:
    def __init__(self, type_of: type, const_values: list[any] = None) -> None:
        self._type_constraint = type_of
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
            if not isinstance(value, self._type_constraint):
                raise TypeError(f"Contained type for {value} is not valid.")
