from src.main.companies.upn.interfaces.pallets import CustPallet, NetworkPallet


class UPNPalletsDatabase:
    def __init__(self):
        ...

    def network_pallet(self) -> NetworkPallet:
        ...

    def customer_pallet(self) -> CustPallet:
        ...

