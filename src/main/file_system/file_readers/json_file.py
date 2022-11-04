import json


def validate_json_monad(func):
    def _validate_file_path(file_path: str):
        if not type(file_path) is str:
            raise TypeError("Must be a string type file path.")

        if not file_path.lower().endswith(".json"):
            raise ValueError(
                "File must have a .json extension. Instead got" + file_path)

        return func(file_path)

    return _validate_file_path


@validate_json_monad
def deserialise(file_path: str):
    with open(file_path) as json_stream:
        return json.load(json_stream)
