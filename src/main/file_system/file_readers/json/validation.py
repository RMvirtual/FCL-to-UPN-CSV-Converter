def validate_json_monad(func):
    def _validate_file_path(file_path: str):
        validate_string_type_parameter(file_path)
        validate_file_extension(file_path)

        return func(file_path)

    return _validate_file_path


def validate_file_extension(file_path: str):
    if not file_path.lower().endswith(".json"):
        raise ValueError(
            "File must have a .json extension. Instead got" + file_path)


def validate_string_type_parameter(parameter: str):
    if not type(parameter) is str:
        raise TypeError("Must be a string type file path.")
