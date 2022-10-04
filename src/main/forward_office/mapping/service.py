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

    def _parse_mappings(self):
        for service_mapping in self._mapping_file_contents():
            self._add(service_mapping)

    def _add(self, service_mapping):
        priority_code = service_mapping["priority_code"]
        service = self._deserialise(service_mapping)

        self._mappings[priority_code] = service

    @staticmethod
    def _deserialise(service_mapping):
        mapping_info = service_mapping["maps_to"]

        result = Service()

        result.priority() if mapping_info["main_service"] == "PRIORITY" else \
            result.economy()

        if mapping_info["premium_service"]:
            if mapping_info["premium_service"] == "AM":
                result.am()

            elif mapping_info["premium_service"] == "PRE-10AM":
                result.pre_10am()

            elif mapping_info["premium_service"] == "TIMED":
                result.timed()

        if mapping_info["booked_service"]:
            if mapping_info["booked_service"] == "BOOK-IN":
                result.book_in()

            elif mapping_info["booked_service"] == "BOOKED":
                result.booked()

        if mapping_info["saturday_service"]:
            result.saturday()

        return result

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
            raise TypeError("Incorrect priority code index.")
