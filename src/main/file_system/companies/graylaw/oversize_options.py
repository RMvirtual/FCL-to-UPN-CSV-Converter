from src.main.file_system.file_readers import runfiles


def _graylaw_resource(relative_path: str) -> str:
    return "resources/companies/graylaw/" + relative_path


def contents() -> list[dict[str, str]]:
    return runfiles.load_json_file(
        _graylaw_resource("cargo_types/oversize_options.json"))
