import re


def is_array(mapping_name: str):
    return bool(re.match("array_of", mapping_name))


def extract_array_object_name(mapping_name: str) -> str:
    return re.sub("array_of_", "", mapping_name)
