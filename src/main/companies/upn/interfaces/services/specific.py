from abc import ABC, abstractmethod


class ServiceProvider(ABC):
    @abstractmethod
    def select(self, service_option: str) -> None:
        ...

    @property
    @abstractmethod
    def selection(self) -> str:
        ...

    @abstractmethod
    def constraints(self) -> list[str]:
        ...
