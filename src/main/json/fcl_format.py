import json
from rules_python.python.runfiles import runfiles


class FclConsignmentFormat:
    def __init__(self, json_file_path: str):
        self._load_json_file(json_file_path)

    def __getitem__(self, item: str) -> int:
        return self._fields[item]

    def __len__(self) -> int:
        return len(self._fields)

    def _load_json_file(self, file_path: str):
        with open(file_path, "r") as json_file:
            self._fields = json.load(json_file)


class UpnEdiImp(FclConsignmentFormat):
    def __init__(self):
        super().__init__(
            json_file_path=self._json_file_path)

    @property
    def _json_file_path(self) -> str:
        r = runfiles.Create()

        return r.Rlocation(
            "fcl-to-upn-csv/resources/file_formats/upn_edi_imp.json")
