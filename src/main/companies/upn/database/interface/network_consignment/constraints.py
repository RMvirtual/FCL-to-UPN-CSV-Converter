from abc import ABC, abstractmethod
from src.main.companies.upn.api.interface_1.database.constraints.constraint \
    import UPNDatabaseConstraint


class NetworkConsignmentConstraintsList(ABC):
    @property
    @abstractmethod
    def consignment_no(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def barcode(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def customer_reference(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def depot_no(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def despatch_date(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_datetime(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_name(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_address_1(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_address_2(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_town(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_county(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_post_code(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_country(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_contact_name(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def delivery_telephone_no(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def total_weight(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def special_instructions(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def customer_id(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def customer_name(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def customer_paperwork_pages(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def main_service(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def premium_service(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def tail_lift_required(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def additional_service(self) -> UPNDatabaseConstraint:
        ...

    @property
    @abstractmethod
    def pallets(self) -> UPNDatabaseConstraint:
        ...
