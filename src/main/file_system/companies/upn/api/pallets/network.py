from src.main.file_system.file_readers import runfiles
from src.main.file_system.companies.upn.api.pallets.keys_with_constraints \
    import KeysWithConstraints


class NetworkPalletFiles(KeysWithConstraints):
    def __init__(self):
        super().__init__(self._keys_path(), self._constraints_path())

    def _keys_path(self) -> str:
        return self._absolute_path("pallets/network/keys.json")

    def _constraints_path(self):
        return self._absolute_path("pallets/network/constraints.json")

    def _absolute_path(self, file_name: str):
        return runfiles.absolute_path(self._api_file_path(file_name))

    @staticmethod
    def _api_file_path(file_name: str) -> str:
        return "resources/companies/upn/api/" + file_name

