import json


class FieldsToIndexes:
    def __init__(self, fields_to_indexes_json: str):
        self._load_json_file(fields_to_indexes_json)

    def __getitem__(self, item: str) -> int:
        return self._fields_to_indexes[item]

    def __len__(self) -> int:
        return len(self._fields_to_indexes)

    def _load_json_file(self, file_path: str):
        with open(file_path, "r") as json_file:
            self._fields_to_indexes = json.load(json_file)
