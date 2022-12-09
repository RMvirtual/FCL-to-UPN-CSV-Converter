from src.main.companies.upn.api.interface.dates.dates import DatesProvider
from src.main.companies.upn.model.implementation.dates.dates import UPNDates

from src.main.companies.upn.api.marshalling.controller.unmarshaller \
    import UPNAPIUnmarshaller


class UPNDatesUnmarshaller(UPNAPIUnmarshaller):
    def __init__(self):
        super().__init__()

    def dates(self, candidate: dict[str, any]) -> DatesProvider:
        return UPNDates(
            despatch=self.unmarshall(candidate, "despatch_date"),
            delivery=self.unmarshall(candidate, "delivery_datetime")
        )
