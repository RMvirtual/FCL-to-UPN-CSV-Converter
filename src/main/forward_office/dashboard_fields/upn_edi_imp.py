import json
from src.main.file_system.runfiles import load_path


def upn_edi_imp_format():
    file_path = load_path("resources/file_formats/upn_edi_imp.json")

    with open(file_path, "r") as json_file:
        field_indexes = json.load(json_file)

    return field_indexes
