from src.main.freight.services.types.interface.tail_lift import TailLiftService


class TailLiftOption(TailLiftService):
    def __init__(self):
        self._is_required = False

    def required(self) -> None:
        self._is_required = True

    def clear(self) -> None:
        self._is_required = False

    def is_required(self) -> bool:
        return self._is_required

    def is_not_required(self) -> bool:
        return not self._is_required

    def __bool__(self):
        return self.is_required()

    def __eq__(self, other: TailLiftService) -> bool:
        return self._is_required == other.is_required()
