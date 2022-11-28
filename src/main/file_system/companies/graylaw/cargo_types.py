from src.main.file_system.file_readers import runfiles


def _graylaw_resource(relative_path: str) -> str:
    return "resources/companies/graylaw/" + relative_path


def base_packages_file():
    return runfiles.load_json_file(
        _graylaw_resource("cargo_types/base_packages.json"))


def oversize_options():
    return runfiles.load_json_file(
        _graylaw_resource("cargo_types/oversize_options.json"))

