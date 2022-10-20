from rules_python.python.runfiles import runfiles
from src.main.file_system.file_readers import json_file


def absolute_path(relative_path: str):
    """From the fcl-to-upn-csv bazel workspace, loads a file from the
    subdirectory.

    Must be exported as a file in bazel and be passed as a data item in
    the build file of the library that uses this function.
    """
    r = runfiles.Create()
    result = r.Rlocation("fcl-to-upn-csv/" + relative_path)

    if not result:
        raise ValueError(
            "Relative path of " + relative_path + " does not work. Check it "
            "is correct or has been added to Bazel's export files."
        )

    return result


def load_json_file(relative_path: str) -> dict:
    file_path = absolute_path(relative_path)

    return json_file.deserialise(file_path)
