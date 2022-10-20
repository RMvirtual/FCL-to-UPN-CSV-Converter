import dataclasses
import json
import copy

from src.main.file_system import runfiles
from src.main.file_system.dashboard_format_files import DashboardFormatFiles


class FormatLoader:
    def __init__(self):
        self._initialise()
        self._load_formats()

    def _initialise(self):
        self._format_files = DashboardFormatFiles()
        self._formats = []

    def _load_formats(self):
        for format_file in dataclasses.fields(self._format_files):
            self._add(format_file)

    def _add(self, format_file):
        file_path = self._file_path(format_file)
        print("Super Path:", file_path)

        format_contents = self._json_contents(file_path)

        self._add_format(format_file.name, format_contents)

    def _file_path(self, format_file: dataclasses.dataclass):
        return runfiles.load_path(
            getattr(self._format_files, format_file.name))

    def _add_format(self, format_name: str, format_contents):
        new_format = [
            format_name,
            dict[str, int],
            dataclasses.field(default_factory=lambda: format_contents)
        ]

        self._formats.append(new_format)

    @staticmethod
    def _json_contents(file_path: str):
        with open(file_path) as json_stream:
            format_contents = json.load(json_stream)

        return format_contents

    def all(self):
        return copy.copy(self._formats)


DashboardFormats = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=FormatLoader().all()
)
