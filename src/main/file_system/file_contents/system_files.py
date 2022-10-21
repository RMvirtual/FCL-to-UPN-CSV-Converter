from src.main.file_system.file_readers import runfiles


def load_path(file_name: str):
    sys_files = runfiles.load_json_file("resources/file_system.json")

    if file_name not in sys_files:
        raise ValueError(
            "No system file found with name of " + file_name + ".")

    return sys_files[file_name]
