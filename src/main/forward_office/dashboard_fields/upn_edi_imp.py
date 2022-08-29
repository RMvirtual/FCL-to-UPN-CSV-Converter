from src.main.json.single_object import FieldsToIndexes
from rules_python.python.runfiles import runfiles


class UpnEdiImp(FieldsToIndexes):
    def __init__(self):
        super().__init__(
            fields_to_indexes_json=self._json_file_path)

    @property
    def _json_file_path(self) -> str:
        r = runfiles.Create()

        return r.Rlocation(
            "fcl-to-upn-csv/resources/file_formats/upn_edi_imp.json")
