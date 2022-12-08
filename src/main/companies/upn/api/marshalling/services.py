from src.main.companies.upn.interfaces.databases.services.container \
    import ServicesProvider

from src.main.companies.upn.database.services.services import UPNServicesDatabase
from src.main.companies.upn.api.marshalling.unmarshaller \
    import UPNAPIUnmarshaller


class UPNServicesUnmarshaller(UPNAPIUnmarshaller):
    def __init__(self):
        super().__init__()

    def services(self, candidate: dict[str, any]) -> ServicesProvider:
        result = UPNServicesDatabase().all_services()
        result.main = self.unmarshall(candidate, "main_service")
        result.premium = self.unmarshall(candidate, "premium_service")
        result.tail_lift = self.unmarshall(candidate, "tail_lift_required")
        result.additional = self.unmarshall(candidate, "additional_service")

        return result
