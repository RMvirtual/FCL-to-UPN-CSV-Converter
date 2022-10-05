import json
import copy

from src.main.file_system import runfiles, system_files
from src.main.freight.service.model import Service


class ServiceCodeMapBuilder:
    def __init__(self):
        self._build_map()

    def _build_map(self):
        self._mappings = {}
        self._parse_mappings()
        self._service = Service()

    def _parse_mappings(self):
        for service_mapping in self._mapping_file_contents():
            self._add(service_mapping)

    def _add(self, service_mapping):
        priority_code = service_mapping["priority_code"]
        self._mappings[priority_code] = self._deserialise(service_mapping)

    def _deserialise(self, service_mapping):
        mapping_info = service_mapping["maps_to"]

        self._service = Service()
        self._parse_main_service(mapping_info)
        self._parse_premium_service(mapping_info)
        self._parse_booked_service(mapping_info)
        self._parse_saturday_service(mapping_info)

        return copy.copy(self._service)

    def _parse_main_service(self, mapping_info):
        _service_callbacks = {
            "PRIORITY": self._service.priority,
            "ECONOMY": self._service.economy
        }

        service_callback = mapping_info["main_service"]
        _service_callbacks[service_callback]()

    def _parse_premium_service(self, mapping_info):
        _service_callbacks = {
            "AM": self._service.am,
            "PRE-10AM": self._service.pre_10am,
            "TIMED": self._service.timed
        }

        if mapping_info["premium_service"]:
            service_callback = mapping_info["premium_service"]
            _service_callbacks[service_callback]()

    def _parse_booked_service(self, mapping_info):
        _service_callbacks = {
            "BOOK-IN": self._service.book_in,
            "BOOKED": self._service.booked
        }

        if mapping_info["booked_service"]:
            service_callback = mapping_info["booked_service"]
            _service_callbacks[service_callback]()

    def _parse_saturday_service(self, mapping_info):
        if mapping_info["saturday_service"]:
            self._service.saturday()

    def _mapping_file_contents(self):
        with open(self._file_path()) as json_file:
            return json.load(json_file)

    @staticmethod
    def _file_path():
        relative_path = system_files.load_path("FCL_SERVICE_CODE_MAPPINGS")

        return runfiles.load_path(relative_path)

    def mappings(self):
        return copy.copy(self._mappings)


class FclServiceCodeMap:
    def __init__(self):
        self._map = ServiceCodeMapBuilder().mappings()

    def __getitem__(self, priority_code: int or str) -> Service:
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
