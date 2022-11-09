import dataclasses
import datetime


@dataclasses.dataclass
class UpnApiPrimitives:
    string: type = str
    int: type = int
    datetime: type = datetime.datetime


def get_primitive(mapping_name: str):
    primitives = UpnApiPrimitives()

    return getattr(primitives, mapping_name)


def is_primitive(mapping_name: str):
    primitives = UpnApiPrimitives()

    return hasattr(UpnApiPrimitives, mapping_name)
