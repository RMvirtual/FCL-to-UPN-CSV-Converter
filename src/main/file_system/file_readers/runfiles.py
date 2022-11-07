from rules_python.python.runfiles import runfiles
from src.main.file_system.file_readers.json import reader


class RunfileDoesNotExist(ValueError):
    def __init__(self, relative_runfile_path: str):
        self.invalid_runfile_path = relative_runfile_path

        fail_message = (
            "Runfile path of " + self.invalid_runfile_path + " does not work. "
            "Check it is correct or has been added to Bazel's export files."
        )

        super().__init__(fail_message)


def absolute_path(relative_runfile_path: str):
    """From the fcl-to-upn-csv bazel workspace, loads a file from the
    subdirectory.

    Must be exported as a file in bazel and be passed as a data item in
    the build file of the library that uses this function.
    """
    result = _absolute_runfile_path(relative_runfile_path)

    if not result:
        raise RunfileDoesNotExist(relative_runfile_path)

    return result


def _absolute_runfile_path(relative_path: str) -> str or None:
    return runfiles.Create().Rlocation("fcl-to-upn-csv/" + relative_path)


def load_json_file(relative_path: str) -> dict:
    return reader.deserialise(absolute_path(relative_path))
