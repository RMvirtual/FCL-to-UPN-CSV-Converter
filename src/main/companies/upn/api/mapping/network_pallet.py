import dataclasses
from src.main.file_system.companies.upn.api.pallets.network \
    import NetworkPalletFiles
from src.main.companies.upn.api.data_types.constraints import (
    Constraints, ConstraintsMarshaller)


@dataclasses.dataclass
class NetworkPalletConstraints:
    barcode: Constraints = None
    type: Constraints = None
    size: Constraints = None
    consignment_barcode: Constraints = None


def network_pallet_constraints() -> NetworkPalletConstraints:
    """Reliant on the network pallet UPN JSON file having the same
    fields as the NetworkPalletMapping dataclass.
    """
    marshaller = ConstraintsMarshaller()
    constraints_file = NetworkPalletFiles()
    result = NetworkPalletConstraints()

    for field in list(dataclasses.fields(NetworkPalletConstraints)):
        constraint = marshaller.unmarshal_constraint(
            constraints_file[field.name])

        setattr(result, field.name, constraint)

    return result
