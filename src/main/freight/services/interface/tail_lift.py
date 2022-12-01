from __future__ import annotations
from abc import abstractmethod
from src.main.freight.services.interface.optional import OptionalService


class TailLiftServiceInterface(OptionalService):
    @abstractmethod
    def __eq__(self, other: TailLiftServiceInterface) -> bool:
        ...

    def required(self) -> None:
        ...

    def clear(self) -> None:
        ...
