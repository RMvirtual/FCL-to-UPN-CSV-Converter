import copy
from src.main.file_system.companies.forward_office import freight_mappings
from src.main.freight.service.container.interface import Services
from src.main.freight.service.container.implementation import ServiceOptions


class ServiceCodeMapBuilder:
    def __init__(self):
        self._build_map()

    def _build_map(self):
        self._mappings = {}
        self._service = ServiceOptions()
        self._parse_mappings()

    def _parse_mappings(self):
        for mapping in freight_mappings.service_code_mappings():
            self._add(mapping)

    def _add(self, service_mapping):
        priority_code = service_mapping["priority_code"]
        mapping_info = service_mapping["maps_to"]

        self._mappings[priority_code] = self._deserialise(mapping_info)

    def _deserialise(self, mapping_info) -> Services:
        self._service = Services()
        self._process_main_service(mapping_info["main_service"])
        self._process_premium_service(mapping_info["premium_service"])
        self._process_booked_service(mapping_info["booked_service"])
        # self._process_saturday_service(mapping_info["saturday_service"])

        return copy.copy(self._service)

    def _process_main_service(self, service_key: str):
        callbacks = {
            "PRIORITY": self._service.main().next_day,
            "ECONOMY": self._service.main().economy()
        }

        callbacks[service_key]()

    def _process_premium_service(self, service_key: str):
        self._set_premium_service(service_key) if service_key else ...

    def _set_premium_service(self, service_key: str):
        callbacks = {
            "AM": self._service.premium().am,
            "PRE-10AM": self._service.premium().pre_10am,
            "TIMED": self._service.premium().timed
        }

        callbacks[service_key]()

    def _process_booked_service(self, service_key: str):
        self._set_booked_service(service_key) if service_key else ...

    def _set_booked_service(self, service_key: str):
        callbacks = {
            "BOOK-IN": self._service.booked().book_in,
            "BOOKED": self._service.booked().booked
        }

        callbacks[service_key]()

    """
    def _process_saturday_service(self, service_key: str):
        self._service.saturday() if service_key else ...
    """

    def mappings(self):
        return copy.copy(self._mappings)


class FclServiceCodeMap:
    def __init__(self):
        self._map = ServiceCodeMapBuilder().mappings()

    def __getitem__(self, priority_code: int or str) -> Services:
        return copy.copy(self._map[self._normalise(priority_code)])

    def contains(self, priority_code: int or str):
        return self._normalise(priority_code) in self._map

    def __contains__(self, priority_code: int or str):
        return self.contains(self._normalise(priority_code))

    @staticmethod
    def _normalise(priority_code: str) -> int:
        if type(priority_code) is str and priority_code.isnumeric():
            return int(priority_code)

        elif type(priority_code) is int or float:
            return priority_code

        else:
            raise TypeError("Invalid priority code:", priority_code)
