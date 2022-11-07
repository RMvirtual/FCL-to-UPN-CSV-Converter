from src.main.file_system.file_readers import runfiles


def _freight_resource(relative_path: str) -> str:
    return "resources/freight/" + relative_path


def base_packages_file():
    return runfiles.load_json_file(
        _freight_resource("cargo_types/base_packages.json"))


def oversize_options():
    return runfiles.load_json_file(
        _freight_resource("cargo_types/oversize_options.json"))

