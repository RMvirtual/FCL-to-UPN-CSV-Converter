import copy
import dataclasses
from src.main.file_system.file_readers import runfiles
from src.main.file_system.file_contents import system_files


def _format_files():
    relative_path = system_files.load_path("FCL_DASHBOARD_FORMATS")
    contents = runfiles.load_json_file(relative_path)

    return [[item, str, contents[item]] for item in contents]


DashboardFormatFiles = dataclasses.make_dataclass(
    cls_name="DashboardFormatFiles",
    fields=_format_files()
)


class FormatLoader:
    def __init__(self):
        self._initialise()
        self._load_formats()

    def _initialise(self) -> None:
        self._format_files = DashboardFormatFiles()
        self._formats = []

    def _load_formats(self) -> None:
        for format_file in dataclasses.fields(self._format_files):
            self._add(format_file)

    def _add(self, format_file) -> None:
        format_contents = runfiles.load_json_file(
            getattr(self._format_files, format_file.name))

        self._add_format(format_file.name, format_contents)

    def _add_format(self, name: str, contents: dict[str, int]) -> None:
        self._formats.append([
            name, dict[str, int],
            dataclasses.field(default_factory=lambda: contents)
        ])

    def all(self):
        return copy.copy(self._formats)


DashboardFormats = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=FormatLoader().all()
)
