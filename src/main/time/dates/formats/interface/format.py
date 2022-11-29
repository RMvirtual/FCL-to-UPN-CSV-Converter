from abc import ABC, abstractmethod


class DateFormat(ABC):
    @property
    @abstractmethod
    def day(self) -> int:
        ...

    @property
    @abstractmethod
    def month(self) -> int:
        ...

    @property
    @abstractmethod
    def year(self) -> int:
        ...
