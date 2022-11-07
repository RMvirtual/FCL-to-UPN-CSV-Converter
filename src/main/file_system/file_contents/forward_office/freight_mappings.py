from src.main.file_system.file_readers import runfiles
from src.main.file_system.file_contents import system_files


def cargo_type_mappings():
    relative_path = system_files.load_path("FCL_CARGO_TYPE_MAPPINGS")

    return runfiles.load_json_file(relative_path)


def service_code_mappings():
    relative_path = system_files.load_path("FCL_SERVICE_CODE_MAPPINGS")

    return runfiles.load_json_file(relative_path)
