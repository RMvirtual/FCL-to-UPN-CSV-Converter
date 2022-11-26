from abc import abstractmethod

from src.main.freight.references.consignment.interface \
    import ConsignmentReference


class FCLConsignmentReference(ConsignmentReference):
    @property
    @abstractmethod
    def prefix(self) -> str:
        ...

    @property
    @abstractmethod
    def number(self) -> str:
        ...

    @number.setter
    @abstractmethod
    def number(self, new_number) -> None:
        ...
