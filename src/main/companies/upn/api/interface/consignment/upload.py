from abc import abstractmethod
from src.main.companies.upn.api.interface.cargo.pallets.upload \
    import UploadPallet
from src.main.companies.upn.api.interface.consignment.base \
    import BaseConsignment
from src.main.companies.upn.api.interface.references.upload \
    import ReferencesUpload


class ConsignmentUpload(BaseConsignment, ReferencesUpload):
    """Main interface for a consignment to upload to the UPN API."""
    @property
    @abstractmethod
    def paperwork_mode(self) -> int:
        ...

    @property
    @abstractmethod
    def short_description(self) -> str:
        ...

    @property
    @abstractmethod
    def pallets(self) -> list[UploadPallet]:
        ...

    @property
    @abstractmethod
    def delivery_email(self) -> str:
        ...
