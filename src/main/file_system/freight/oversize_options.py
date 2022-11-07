from src.main.file_system.file_readers import runfiles


def _freight_resource(relative_path: str) -> str:
    return "resources/freight/" + relative_path


def contents() -> list[dict[str, str]]:
    return runfiles.load_json_file(
        _freight_resource("cargo_types/oversize_options.json"))
