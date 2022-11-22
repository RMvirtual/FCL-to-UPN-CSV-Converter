from src.main.graylaw.consignment.interface import Consignment
from src.main.graylaw.references.interface import References
from src.main.graylaw.address.interface import Address
from src.main.graylaw.cargo.model import Cargo
from src.main.graylaw.service.model import Service
from src.main.graylaw.shipment_dates.interface import ShipmentDates

from src.main.upn.api.data_structures.network_consignment.mapping \
    import NetworkConsignmentMapping

from src.main.upn.api.data_structures.network_consignment.implementation \
    import NetworkConsignment

from src.main.graylaw.references import factory as reference_factory
from src.main.upn.api.adaptors.address import UPNAddressAdaptor


class NetworkConsignmentAdaptor(Consignment):
    """Adaptor for turning a UPN Network Consignment structure into
    a Graylaw Consignment.
    """
    def __init__(self, network_consignment: NetworkConsignment):
        self._network_consignment = network_consignment

    @property
    def references(self) -> References:
        return reference_factory.references(
            consignment_reference=self._network_consignment.consignment_no,
            shipper_references=[self._network_consignment.customer_reference],
            consignee_references=[]
        )

    @references.setter
    def references(self, new_references: References) -> None:
        ...

    @property
    def address(self) -> Address:
        return UPNAddressAdaptor(self._network_consignment.delivery_address)

    @address.setter
    def address(self, new_address: Address) -> None:
        ...

    @property
    def cargo(self) -> Cargo:
        ...

    @cargo.setter
    def cargo(self, new_cargo: Cargo) -> None:
        ...

    @property
    def service(self) -> Service:
        ...

    @service.setter
    def service(self, new_service: Service) -> None:
        ...

    @property
    def delivery_instructions(self) -> list[str]:
        ...

    @delivery_instructions.setter
    def delivery_instructions(self, new_instructions: list[str]) -> None:
        ...

    @property
    def client_name(self) -> str:
        ...

    @client_name.setter
    def client_name(self, new_name: str) -> None:
        ...

    @property
    def shipment_dates(self) -> ShipmentDates:
        ...

    @shipment_dates.setter
    def shipment_dates(self, new_dates: ShipmentDates):
        ...
