from abc import ABC, abstractmethod


class CustomerDetails(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...
