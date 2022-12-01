from abc import ABC, abstractmethod


class OptionalService(ABC):
    @abstractmethod
    def is_required(self) -> bool:
        ...

    @abstractmethod
    def is_not_required(self) -> bool:
        ...

    @abstractmethod
    def __bool__(self) -> bool:
        ...
