from abc import ABC, abstractmethod
from src.main.companies.upn.model.interface.constraints.data \
    import DataConstraint


class NetworkConsignmentConstraintsList(ABC):
    @property
    @abstractmethod
    def consignment_no(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def barcode(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def customer_reference(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def depot_no(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def despatch_date(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_datetime(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_name(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_address_1(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_address_2(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_town(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_county(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_post_code(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_country(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_contact_name(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def delivery_telephone_no(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def total_weight(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def special_instructions(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def customer_id(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def customer_name(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def customer_paperwork_pages(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def main_service(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def premium_service(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def tail_lift_required(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def additional_service(self) -> DataConstraint:
        ...

    @property
    @abstractmethod
    def pallets(self) -> DataConstraint:
        ...
