from src.main.file_system.file_readers import runfiles


def network_consignment():
    return _load_json_runfile_from_structures("network_consignment.json")


def network_pallet():
    return _load_json_runfile_from_structures("network_pallet.json")


def package_type_mappings():
    return _load_json_runfile_from_structures("package_type_mappings.json")


def primitives():
    return _load_json_runfile_from_structures("primitives.json")


def service_mappings():
    return _load_json_runfile_from_structures("service_mappings.json")


def _load_json_runfile_from_structures(file_name: str):
    return runfiles.load_json_file(_append_to_structures_path(file_name))


def _append_to_structures_path(file_name: str) -> str:
    return "resources/upn/api_structures/" + file_name
