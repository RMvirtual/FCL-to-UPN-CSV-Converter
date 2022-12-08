from abc import ABC, abstractmethod


class DataTypesContainer(ABC):
    @abstractmethod
    def __contains__(self, data_type: str) -> bool:
        ...

    @abstractmethod
    def __getitem__(self, data_type: str) -> type:
        ...
