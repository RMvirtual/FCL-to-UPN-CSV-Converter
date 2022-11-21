from src.main.graylaw.references import interface
from src.main.graylaw.references.references import References


def references(
        consignment_reference: str, shipper_references: list[str],
        consignee_references: list[str]
) -> interface.References:
    result = References(consignment_reference)
    result.shipper.append(shipper_references)
    result.consignee.append(consignee_references)

    return result
