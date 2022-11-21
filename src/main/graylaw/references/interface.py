from abc import ABC, abstractmethod
from src.main.graylaw.references.consignment_reference \
    import ConsignmentReference


class References(ABC):
    @property
    @abstractmethod
    def consignment(self) -> ConsignmentReference:
        ...

    @consignment.setter
    @abstractmethod
    def consignment(self, new_reference: str) -> None:
        ...

    @property
    @abstractmethod
    def shipper(self) -> list[str]:
        ...

    @property
    @abstractmethod
    def consignee(self) -> list[str]:
        ...
