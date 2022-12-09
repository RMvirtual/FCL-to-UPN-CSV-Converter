from abc import ABC, abstractmethod
from src.main.companies.upn.model.interface.services.specific \
    import ServiceProvider


class ServicesProvider(ABC):
    @property
    @abstractmethod
    def main_service(self) -> ServiceProvider:
        ...

    @property
    @abstractmethod
    def premium_service(self) -> ServiceProvider:
        ...

    @property
    @abstractmethod
    def tail_lift_required(self) -> ServiceProvider:
        ...

    @property
    @abstractmethod
    def additional_service(self) -> ServiceProvider:
        ...
