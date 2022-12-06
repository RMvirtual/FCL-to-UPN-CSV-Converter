import datetime
from src.main.companies.upn.api.data_types.abstract.implementation \
    import DataTypes


class UPNAPIPrimitives(DataTypes):
    def __init__(self):
        data_types = {
            "string": str,
            "int": int,
            "datetime": datetime.datetime
        }

        super(UPNAPIPrimitives, self).__init__(data_types)
