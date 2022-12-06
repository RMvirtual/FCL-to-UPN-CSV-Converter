from abc import ABC, abstractmethod


class UPNDatabaseConstraint(ABC):
    @property
    @abstractmethod
    def type_constraint(self) -> type:
        ...

    @property
    @abstractmethod
    def value_constraints(self) -> list[any]:
        ...
