from src.main.companies.upn.api.interface.cargo.pallets.download \
    import DownloadPallet
from src.main.companies.upn.model.implementation.cargo.pallets.download \
    .builder import NetworkPalletBuilder


def network_pallet(
        type_name: str, size_name: str,
        type_constraints: list[str] = None, size_constraints: list[str] = None
) -> DownloadPallet:
    builder = NetworkPalletBuilder()
    builder.set_type(type_name)
    builder.set_size(size_name)

    if type_constraints:
        builder.set_type_constraints(type_constraints)

    if size_constraints:
        builder.set_size_constraints(size_constraints)

    return builder.build()
