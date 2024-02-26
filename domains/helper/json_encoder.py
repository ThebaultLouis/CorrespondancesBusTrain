leaf_types = [int, float, str]


def convert_python_object_to_dict(value):
    for leaf_type in leaf_types:
        if isinstance(value, leaf_type):
            return value
    if isinstance(value, list):
        return [convert_python_object_to_dict(item) for item in value]
    if isinstance(value, dict):
        return {
            key: convert_python_object_to_dict(key_value)
            for key, key_value in value.items()
        }

    python_object: object = value
    python_object_to_dict = {}

    for key, value in python_object.__dict__.items():
        if value == None:
            continue
        python_object_to_dict[key] = convert_python_object_to_dict(value)

    return python_object_to_dict
