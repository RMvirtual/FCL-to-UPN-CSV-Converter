from src.main.upn.consignment.network_consignment.implementation \
    import NetworkConsignment

from src.main.upn.consignment.cargo.package.network_pallet.implementation \
    import NetworkPallet


def get_data_structure(mapping_name: str):
    structures = {
        "network_pallet": NetworkPallet,
        "network_consignment": NetworkConsignment
    }

    return structures[mapping_name]


def is_data_structure(mapping_name: str):
    return mapping_name in ("network_pallet", "network_consignment")
