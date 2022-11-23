from src.main.upn.consignment.structures.cargo.container.container \
    import UPNCargo

from src.main.upn.api.data_structures.network_pallet.implementation \
    import NetworkPallet


def single_entry_upn_cargo() -> UPNCargo:
    result = UPNCargo()
    result.total_weight = 3000
    network_pallet = NetworkPallet()
    network_pallet.consignment_barcode = "W123456789"
    network_pallet.barcode = "W987654321"
    network_pallet.size = "N"
    network_pallet.type = "FULL"

    for i in range(3):
        result.pallets.append(network_pallet)

    return result


