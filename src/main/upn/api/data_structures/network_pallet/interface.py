import abc
from abc import ABC


class NetworkPallet(ABC):
    @property
    @abc.abstractmethod
    def barcode(self) -> str:
        """The pallet's barcode number (not the consignment)."""

    @abc.abstractmethod
    @barcode.setter
    def barcode(self, new_barcode_no: str) -> None:
        """Sets the pallet's barcode number (not the consignment)."""

    @property
    @abc.abstractmethod
    def consignment_barcode(self) -> str:
        """The parent consignment's barcode number (not the individual
        pallet's).
        """

    @abc.abstractmethod
    @consignment_barcode.setter
    def consignment_barcode(self, new_barcode_no: str) -> None:
        """Changes the parent consignment barcode number."""

    @property
    @abc.abstractmethod
    def size(self) -> str:
        """The pallet's size as a string."""

    @abc.abstractmethod
    @size.setter
    def size(self, new_size: str) -> None:
        """Sets a new pallet size."""

    @property
    @abc.abstractmethod
    def type(self) -> str:
        """The pallet's type"""

    @abc.abstractmethod
    @type.setter
    def type(self, new_type: str) -> None:
        """Sets the pallet's type."""
