import dataclasses
import datetime


@dataclasses.dataclass
class UPNAPIPrimitives:
    string: type = str
    int: type = int
    datetime: type = datetime.datetime

    def contains(self, mapping_name: str):
        return hasattr(self, mapping_name)

    def __contains__(self, mapping_name: str):
        return self.contains(mapping_name)

    def get(self, mapping_name: str) -> type:
        return getattr(self, mapping_name)

    def __getitem__(self, mapping_name: str) -> type:
        return self.get(mapping_name)
