import dataclasses
import json

from src.main.file_system import system_files, runfiles


def _format_files():
    dashboard_formats_file = system_files.load_path("FCL_DASHBOARD_FORMATS")
    full_path = runfiles.load_path(dashboard_formats_file)

    with open(full_path) as json_file:
        contents = json.load(json_file)

    fields = []

    for item in contents:
        fields.append([item, str, contents[item]])

    return fields


DashboardFormatFiles = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=_format_files()
)
