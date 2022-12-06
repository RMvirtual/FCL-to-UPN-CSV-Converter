from abc import ABC, abstractmethod


class UPNAPIDataTypes(ABC):
    @abstractmethod
    def contains(self, data_type: str) -> bool:
        ...

    @abstractmethod
    def get(self, data_type: str) -> type:
        ...

    @abstractmethod
    def __contains__(self, data_type: str) -> bool:
        ...

    @abstractmethod
    def __getitem__(self, data_type: str) -> type:
        ...
