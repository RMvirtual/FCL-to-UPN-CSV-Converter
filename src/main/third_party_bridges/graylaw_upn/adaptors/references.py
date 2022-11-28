import copy
from src.main.freight.references.consignment.interface \
    import ConsignmentReference as GraylawConsignmentReference

from src.main.freight.references.interface import References
from src.main.upn.freight.references.references import UPNReferences


class UPNReferencesAdaptor(References):
    """Class for adapting a UPN references structure into a Graylaw
    references structure.
    """
    def __init__(self, upn_references: UPNReferences):
        self._references = copy.deepcopy(upn_references)

    @property
    def consignment(self) -> GraylawConsignmentReference:
        return self._references.consignment_no

    @consignment.setter
    def consignment(self, new_reference: str) -> None:
        self._references.consignment_no = new_reference

    @property
    def shipper(self) -> list[str]:
        return [self._references.customer_reference]

    @property
    def consignee(self) -> list[str]:
        """Empty list as UPN does not appear to support consignee
        references.
        """
        return []
