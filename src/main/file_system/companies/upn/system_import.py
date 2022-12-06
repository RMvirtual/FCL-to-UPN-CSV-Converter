from src.main.file_system.file_readers import runfiles


def service_mappings():
    return _sys_import_file_contents("service_mappings.json")


def package_type_mappings():
    return _sys_import_file_contents("package_type_mappings.json")


def _sys_import_file_contents(file_name: str):
    return runfiles.load_json_file(_sys_import_file_path(file_name))


def _sys_import_file_path(file_name: str) -> str:
    return "resources/companies/upn/system_import/" + file_name
