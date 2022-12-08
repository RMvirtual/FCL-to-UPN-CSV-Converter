from abc import abstractmethod
from src.main.companies.upn.api.interface.references.upload \
    import ReferencesUpload


class ReferencesDownload(ReferencesUpload):
    @property
    @abstractmethod
    def barcode(self) -> str:
        ...
