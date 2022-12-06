from src.main.companies.upn.api.data_types.abstract.implementation \
    import DataTypes


class UPNAPIContainers(DataTypes):
    def __init__(self):
        data_types = {
            "dictionary": dict,
            "array": list
        }

        super(UPNAPIContainers, self).__init__(data_types)
