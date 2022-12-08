from src.main.file_system.file_readers.json import reader


class KeysWithConstraints:
    """File for reading and returning a structure containing
    a keys json file and a constraints json file.
    """
    def __init__(self, keys_path: str, constraints_path: str) -> None:
        self._keys = reader.deserialise(keys_path)
        self._constraints = reader.deserialise(constraints_path)

    @property
    def keys(self) -> dict[str, any]:
        return self._keys

    @property
    def constraints(self) -> dict[str, any]:
        return self._constraints
