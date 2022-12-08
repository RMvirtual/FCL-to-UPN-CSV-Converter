from abc import ABC, abstractmethod
from src.main.companies.upn.database.interface.constraints.constraint \
    import UPNDatabaseConstraint


class ServiceProvider(ABC):
    @abstractmethod
    def select(self, service_option: str) -> None:
        ...

    @property
    @abstractmethod
    def selection(self) -> str:
        ...

    @abstractmethod
    def constraints(self) -> UPNDatabaseConstraint:
        ...
