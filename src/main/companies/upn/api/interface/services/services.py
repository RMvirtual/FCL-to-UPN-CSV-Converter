from abc import ABC, abstractmethod


class ServicesProvider(ABC):
    @property
    @abstractmethod
    def main_service(self) -> str:
        ...

    @property
    @abstractmethod
    def premium_service(self) -> str:
        ...

    @property
    @abstractmethod
    def tail_lift_required(self) -> str:
        ...

    @property
    @abstractmethod
    def additional_service(self) -> str:
        ...
