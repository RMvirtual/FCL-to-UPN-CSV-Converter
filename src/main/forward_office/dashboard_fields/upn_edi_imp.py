from src.main.json.single_object import FieldsToIndexes
from src.main.file_system.runfiles import load_path


class UpnEdiImp(FieldsToIndexes):
    def __init__(self):
        super().__init__(
            fields_to_indexes_json=self._json_file_path)

    @property
    def _json_file_path(self) -> str:
        return load_path("resources/file_formats/upn_edi_imp.json")
