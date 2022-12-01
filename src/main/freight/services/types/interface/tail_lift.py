from __future__ import annotations
from abc import abstractmethod
from src.main.freight.services.types.interface.optional import OptionalService


class TailLiftService(OptionalService):
    @abstractmethod
    def __eq__(self, other: TailLiftService) -> bool:
        ...

    def required(self) -> None:
        ...

    def clear(self) -> None:
        ...
