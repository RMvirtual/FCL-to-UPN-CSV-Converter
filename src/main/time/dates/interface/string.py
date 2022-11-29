from abc import ABC, abstractmethod


class StringDateInterface(ABC):
    @property
    @abstractmethod
    def day(self) -> str:
        ...

    @property
    @abstractmethod
    def month(self) -> str:
        ...

    @property
    @abstractmethod
    def year(self) -> str:
        ...
