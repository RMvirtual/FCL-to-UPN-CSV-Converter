import dataclasses
import json
import copy

from src.main.file_system import runfiles
from src.main.file_system.dashboard_format_files import DashboardFormatFiles


class FormatLoader:
    def __init__(self):
        self._load_formats()

    def _load_formats(self):
        self._format_files = DashboardFormatFiles()
        self._formats = []

        for file_entry in dataclasses.fields(self._format_files):
            self.add_format_entry(file_entry)

    def add_format_entry(self, format_entry):
        full_format_path = self._file_path(format_entry)
        format_contents = self._json_contents(full_format_path)
        self._add_format(format_entry, format_contents)

    def _add_format(self, file_name, contents):
        new_format = [
            file_name.name,
            dict[str, int],
            dataclasses.field(default_factory=lambda: contents)
        ]

        self._formats.append(new_format)

    def _file_path(self, file_entry: any):
        return runfiles.load_path(getattr(self._format_files, file_entry.name))

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
