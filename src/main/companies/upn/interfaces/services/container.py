from abc import ABC, abstractmethod
from src.main.companies.upn.interfaces.services.service import UPNService


class UPNServices(ABC):
    @property
    @abstractmethod
    def main_service(self) -> UPNService:
        ...

    @property
    @abstractmethod
    def premium_service(self) -> UPNService:
        ...

    @property
    @abstractmethod
    def tail_lift_required(self) -> UPNService:
        ...

    @property
    @abstractmethod
    def additional_service(self) -> UPNService:
        ...
