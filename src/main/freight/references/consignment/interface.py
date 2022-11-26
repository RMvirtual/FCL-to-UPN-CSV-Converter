from abc import ABC, abstractmethod


class ConsignmentReference(ABC):
    @abstractmethod
    def __str__(self):
        ...

