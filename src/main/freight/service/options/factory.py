from src.main.freight.service.options.interface.main import MainService
from src.main.freight.service.options.interface.premium import PremiumService
from src.main.freight.service.options.interface.booked import BookedService
from src.main.freight.service.options.interface.tail_lift \
    import TailLiftService

from src.main.freight.service.options.implementation.main import MainOption
from src.main.freight.service.options.implementation.premium \
    import PremiumOption

from src.main.freight.service.options.implementation.booked \
    import BookedOption

from src.main.freight.service.options.implementation.tail_lift \
    import TailLiftOption


def main_service() -> MainService:
    return MainOption()


def premium_service() -> PremiumService:
    return PremiumOption()


def booked_service() -> BookedService:
    return BookedOption()


def tail_lift_service() -> TailLiftService():
    return TailLiftOption()
