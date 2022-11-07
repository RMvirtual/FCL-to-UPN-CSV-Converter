from src.main.file_system.file_readers import runfiles


def contents() -> list[dict[str, str]]:
    return runfiles.load_json_file(
        "resources/cargo_types/oversize_options.json")
