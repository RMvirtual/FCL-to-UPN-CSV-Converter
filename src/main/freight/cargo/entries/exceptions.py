class CargoEntryException(Exception):
    def __init__(self, message):
        super().__init__(message)


class QuantityInvalid(CargoEntryException):
    def __init__(self):
        msg = "Desired number of packages will exceed maximum average weight."
        super(QuantityInvalid, self).__init__(msg)


class PackageTypesInvalid(CargoEntryException):
    def __init__(self):
        msg = "Incorrect pallet types to combine."
        super(PackageTypesInvalid, self).__init__(msg)


class TotalsInvalid(CargoEntryException):
    def __init__(self):
        msg = "Totals exceed average maximum weight."
        super(TotalsInvalid, self).__init__(msg)


class TotalWeightInvalid(CargoEntryException):
    def __init__(self, total_weight, max_weight_per_package, total_quantity):
        msg = (
            f"Desired weight of {total_weight} will exceed average maximum "
            f"weight of {max_weight_per_package} spread across "
            f"{total_quantity} packages."
        )

        super(TotalWeightInvalid, self).__init__(msg)
