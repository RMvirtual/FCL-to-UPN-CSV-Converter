import dataclasses
import datetime


@dataclasses.dataclass
class UpnApiPrimitives:
    string: type = str
    int: type = int
    datetime: type = datetime.datetime
    array_of_network_pallet: type = list["NetworkPallet"]
