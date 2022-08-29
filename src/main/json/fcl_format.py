import json
from rules_python.python.runfiles import runfiles


class FclConsignmentFormat:
    def __init__(self, json_file_path: str):
        self._file_path = json_file_path

    def __getitem__(self, item: str) -> int:
        return 0

    def __len__(self) -> int:
        return 0


class UpnEdiImp(FclConsignmentFormat):
    def __init__(self):
        super().__init__(
            json_file_path=self._json_file_path)

    @property
    def _json_file_path(self) -> str:
        r = runfiles.Create()

        return r.Rlocation(
            "fcl-to-upn-csv/resources/file_formats/upn_edi_imp.json")
