import dataclasses
import json

from src.main.file_system import runfiles
from src.main.file_system.dashboard_format_files import DashboardFormatFiles


def _formats():
    format_files = DashboardFormatFiles()
    formats = []

    for file_name in dataclasses.fields(format_files):
        full_format_path = _get_file_path(file_name, format_files)

        with open(full_format_path) as json_stream:
            format_contents = json.load(json_stream)

        formats.append([
            file_name.name,
            dict[str, int],
            dataclasses.field(default_factory=lambda: format_contents)
        ])

    return formats


def _get_file_path(file_name: any, format_files: DashboardFormatFiles):
    return runfiles.load_path(getattr(format_files, file_name.name))


DashboardFormats = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=_formats()
)
