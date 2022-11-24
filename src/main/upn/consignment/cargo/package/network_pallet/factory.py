from src.main.upn.consignment.cargo.package.network_pallet.implementation import NetworkPalletFields, NetworkPallet

from src.main.upn.consignment.cargo.package.network_pallet.interface import NetworkPallet as NetworkPalletInterface

from src.main.upn.api.data_structures.network_pallet import mapping


def network_pallet(type_name: str, size_name: str) -> NetworkPalletInterface:
    fields = NetworkPalletFields()
    fields.type = type_name
    fields.size = size_name

    constraints = mapping.network_pallet()

    fields.type_constraints = constraints.type.values
    fields.size_constraints = constraints.size.values

    return NetworkPallet(fields)
