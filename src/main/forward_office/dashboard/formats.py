import dataclasses
import json

from src.main.file_system import runfiles
from src.main.file_system.dashboard_format_files import DashboardFormatFiles

format_files = DashboardFormatFiles()
formats = []

for format_field in dataclasses.fields(format_files):
    full_format_path = runfiles.load_path(
        getattr(format_files, format_field.name))

    with open(full_format_path) as json_stream:
        format_contents = json.load(json_stream)

    formats.append([
        format_field.name,
        dict[str, int],
        dataclasses.field(default_factory=lambda: format_contents)
    ])

DashboardFormats = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=formats
)