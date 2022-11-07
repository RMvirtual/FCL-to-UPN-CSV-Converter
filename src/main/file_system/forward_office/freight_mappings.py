from src.main.file_system.file_readers import runfiles


def _forward_office_resource(relative_path: str) -> str:
    return "resources/forward_office/" + relative_path


def cargo_type_mappings():
    relative_path = _forward_office_resource(
        "package_types/cargo_type_mappings.json")

    return runfiles.load_json_file(relative_path)


def service_code_mappings():
    relative_path = _forward_office_resource("priority_codes/upn.json")

    return runfiles.load_json_file(relative_path)
