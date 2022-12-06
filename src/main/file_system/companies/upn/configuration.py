from src.main.file_system.file_readers import runfiles


def upn_api() -> dict[str, str]:
    return runfiles.load_json_file("config/companies/upn/api.json")
