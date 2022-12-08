from abc import abstractmethod

from src.main.companies.upn.api.interface.consignments.base \
    import BaseConsignment

from src.main.companies.upn.api.interface.pallets.download import DownloadPallet
from src.main.companies.upn.api.interface.references.upload \
    import ReferencesDownload


class ConsignmentDownload(BaseConsignment, ReferencesDownload):
    """Main interface for a consignment downloaded from the UPN API."""
    @property
    @abstractmethod
    def barcode(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_name(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_paperwork_pages(self) -> int:
        ...

    @property
    @abstractmethod
    def pallets(self) -> list[DownloadPallet]:
        ...
