from src.main.companies.upn.interfaces.database.constraint \
    import UPNDatabaseConstraint


class APIConstraint(UPNDatabaseConstraint):
    def __init__(
            self, type_constraint: type, value_constraints: list[any] = None):
        self._type_constraint = type_constraint
        self._value_constraints = value_constraints

    @property
    def type_constraint(self) -> type:
        return self._type_constraint

    @property
    def value_constraints(self) -> list[any]:
        return self._value_constraints
