import dataclasses
import json
import copy

from src.main.freight.cargo.types import PackageType


@dataclasses.dataclass
class UpnPackageTypeMap:
    type: int = 0
    size: int = 0


def map_to_upn_package(package_type: PackageType):
    result = UpnPackageTypeMap()
    result.type = 1
    result.size = 1

    return result

