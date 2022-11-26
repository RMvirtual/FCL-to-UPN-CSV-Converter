from src.main.upn.consignment.cargo.package.network_pallet.builder \
    import NetworkPalletBuilder

from src.main.upn.consignment.cargo.package.network_pallet.interface \
    import NetworkPallet as NetworkPalletInterface


def network_pallet(
        type_name: str, size_name: str,
        type_constraints: list[str] = None, size_constraints: list[str] = None
) -> NetworkPalletInterface:
    builder = NetworkPalletBuilder()
    builder.set_type(type_name)
    builder.set_size(size_name)

    if type_constraints:
        builder.set_type_constraints(type_constraints)

    if size_constraints:
        builder.set_size_constraints(size_constraints)

    return builder.build()