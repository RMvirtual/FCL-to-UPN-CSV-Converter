import dataclasses
import json

from src.main.file_system import system_files, runfiles


def _format_files():
    contents = _json_contents()
    fields = []

    for item in contents:
        fields.append([item, str, contents[item]])

    return fields


def _json_contents():
    dashboard_formats_file = system_files.load_path("FCL_DASHBOARD_FORMATS")
    full_path = runfiles.load_path(dashboard_formats_file)

    with open(full_path) as json_file:
        return json.load(json_file)


DashboardFormatFiles = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=_format_files()
)
