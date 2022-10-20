import dataclasses
import copy

from src.main.file_system.file_readers import runfiles
from src.main.file_system.file_readers import json_file

from src.main.file_system.file_contents.forward_office \
    import DashboardFormatFiles


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
        file_path = self._file_path(format_file)
        format_contents = json_file.deserialise(file_path)

        self._add_format(format_file.name, format_contents)

    def _file_path(self, format_file: dataclasses.dataclass) -> str:
        return runfiles.absolute_path(
            getattr(self._format_files, format_file.name))

    def _add_format(self, name: str, contents: dict[str, int]) -> None:
        new_format = [
            name,
            dict[str, int],
            dataclasses.field(default_factory=lambda: contents)
        ]

        self._formats.append(new_format)

    def all(self):
        return copy.copy(self._formats)


DashboardFormats = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=FormatLoader().all()
)
