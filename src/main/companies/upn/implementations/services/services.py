from src.main.companies.upn.interfaces.services.container \
    import UPNServices as UPNServicesProvider


class UPNServices(UPNServicesProvider):
    def __init__(self):
        ...

    @property
    def main_service(self) -> str:
        pass

    @property
    def premium_service(self) -> str:
        pass

    @property
    def tail_lift_required(self) -> str:
        pass

    @property
    def additional_service(self) -> str:
        pass

