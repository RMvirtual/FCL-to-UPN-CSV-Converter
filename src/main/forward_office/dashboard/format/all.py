import dataclasses
import json

from src.main.file_system import runfiles
from src.main.file_system.dashboard_format_files import DashboardFormatFiles


def _formats():
    format_files = DashboardFormatFiles()
    formats = []

    for file_name in dataclasses.fields(format_files):
        full_format_path = _get_file_path(file_name, format_files)
        format_contents = _load_contents_from_json(full_format_path)

        formats.append(_create_dashboard_format(file_name, format_contents))

    return formats


def _create_dashboard_format(file_name, contents):
    return [
        file_name.name,
        dict[str, int],
        dataclasses.field(default_factory=lambda: contents)
    ]


def _get_file_path(file_name: any, format_files: DashboardFormatFiles):
    return runfiles.load_path(getattr(format_files, file_name.name))


def _load_contents_from_json(file_path: str):
    with open(file_path) as json_stream:
        format_contents = json.load(json_stream)

    return format_contents


DashboardFormats = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=_formats()
)
