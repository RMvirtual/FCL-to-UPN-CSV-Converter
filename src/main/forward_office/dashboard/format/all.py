import dataclasses
import json

from src.main.file_system import runfiles
from src.main.file_system.dashboard_format_files import DashboardFormatFiles


class FormatLoader:
    def __init__(self):
        self._initialise_formats()

    def all(self):
        return self._formats

    def _initialise_formats(self):
        format_files = DashboardFormatFiles()
        self._formats = []

        for file_entry in dataclasses.fields(format_files):
            full_format_path = self._file_path(file_entry, format_files)
            format_contents = self._load_contents_from_json(full_format_path)

            self._formats.append(
                self._create_dashboard_format(file_entry, format_contents))

    def _create_dashboard_format(self, file_name, contents):
        return [
            file_name.name,
            dict[str, int],
            dataclasses.field(default_factory=lambda: contents)
        ]

    def _file_path(self, file_entry: any, format_files: DashboardFormatFiles):
        return runfiles.load_path(getattr(format_files, file_entry.name))

    def _load_contents_from_json(self, file_path: str):
        with open(file_path) as json_stream:
            format_contents = json.load(json_stream)

        return format_contents


DashboardFormats = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=FormatLoader().all()
)
