from abc import abstractmethod

from src.main.graylaw.references.consignment.interface \
    import ConsignmentReference


class FclConsignmentReference(ConsignmentReference):
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
