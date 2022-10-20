from src.main.file_system.file_readers import runfiles, system_files


def base_packages_file():
    return runfiles.load_json_file(cargo_types_file())


def cargo_types_file():
    return system_files.load_path("CARGO_TYPES")
