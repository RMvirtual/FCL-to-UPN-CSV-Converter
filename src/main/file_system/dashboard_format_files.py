import dataclasses
import json

from src.main.file_system import system_paths, runfiles

dashboard_formats_file = system_paths.load_path("FCL_DASHBOARD_FORMATS")
full_path = runfiles.load_path(dashboard_formats_file)

with open(full_path) as json_file:
    contents = json.load(json_file)

fields = []

for item in contents:
    fields.append([item, str, contents[item]])

DashboardFormatFiles = dataclasses.make_dataclass(
    cls_name="DashboardFormats",
    fields=fields
)