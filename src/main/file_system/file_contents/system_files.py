from src.main.file_system.file_readers import runfiles


def load_path(file_name: str):
    sys_files = runfiles.load_json_file("resources/file_system.json")
    result = None

    for file in sys_files:
        if file == file_name:
            result = sys_files[file]
            break

    if result is None:
        raise ValueError("No file found matching", file_name)

    return result
