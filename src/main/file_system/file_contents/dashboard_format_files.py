import dataclasses
import json

from src.main.file_system.file_readers import runfiles, system_files


def _format_files():
    contents = _json_contents()

    return [[item, str, contents[item]] for item in contents]


def _json_contents():
    with open(_file_path()) as json_file:
        return json.load(json_file)


def _file_path():
    dashboard_formats_file = system_files.load_path("FCL_DASHBOARD_FORMATS")

    return runfiles.absolute_path(dashboard_formats_file)


DashboardFormatFiles = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=_format_files()
)
