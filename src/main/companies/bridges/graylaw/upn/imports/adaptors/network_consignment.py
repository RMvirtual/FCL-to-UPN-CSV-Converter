from src.main.freight.consignment.interface import Consignment
from src.main.freight.references.interface import References
from src.main.freight.address.interface import Address
from src.main.freight.cargo.container.implementation import Cargo
from src.main.freight.service.container.interface import Services
from src.main.freight.shipment_dates.interface import ShipmentDatesInterface

from src.main.companies.upn.consignments.network_consignment.implementation \
    import NetworkConsignment

from src.main.companies.bridges.graylaw.upn.imports.adaptors.address \
    import UPNAddressAdaptor

from src.main.companies.bridges.graylaw.upn.imports.adaptors.references \
    import UPNReferencesAdaptor

from src.main.companies.bridges.graylaw.upn.imports.adaptors.dates \
    import UPNDatesInterfaceAdaptor


class NetworkConsignmentAdaptor(Consignment):
    """Adaptor for turning a UPN Network Consignment structure into
    a Graylaw Consignment.
    """
    def __init__(self, network_consignment: NetworkConsignment):
        self._network_consignment = network_consignment

    @property
    def references(self) -> References:
        return UPNReferencesAdaptor(self._network_consignment.references)

    @property
    def address(self) -> Address:
        return UPNAddressAdaptor(self._network_consignment.delivery_address)

    @property
    def cargo(self) -> Cargo:
        ...

    @property
    def service(self) -> Services:
        ...

    @property
    def delivery_instructions(self) -> list[str]:
        return [self._network_consignment.special_instructions]

    @property
    def client_name(self) -> str:
        return self._network_consignment.customer_name

    @property
    def shipment_dates(self) -> ShipmentDatesInterface:
        return UPNDatesInterfaceAdaptor(self._network_consignment.dates)
