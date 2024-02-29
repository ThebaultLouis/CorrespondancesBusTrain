import os

from dotenv import load_dotenv
from domains.sncf_api.service import SNCF_API_SERVICE


def build_enum_from_dict(enumDict: dict, enumClassName: str, file_path: str):
    sortedEnumDict = dict(sorted(enumDict.items()))
    with open(file_path, "w+") as py_file:
        # Write the Enum class definition
        py_file.write("from enum import Enum\n\n")
        py_file.write(f"class {enumClassName}(Enum):\n")
        # Write enum members
        for key, value in sortedEnumDict.items():
            py_file.write(f"    {key} = '{value}'\n")
        print(f"Enum class has been written to {file_path}")


def create_init_files(path):
    os.makedirs(path, exist_ok=True)
    current_directory = path
    while current_directory:
        init_file = os.path.join(current_directory, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                pass  # Creating an empty __init__.py file
        current_directory = os.path.dirname(current_directory)


def convert_place_name_to_enum_id(place_name: str):
    unauthorized_enum_characters = {
        " ": "_",
        "-": "_",
        "(": "_",
        ")": "",
        "&": "and",
        "'": "",
    }
    enum_id = place_name.upper()
    for (
        unauthorized_enum_character,
        replace_by_character,
    ) in unauthorized_enum_characters.items():
        enum_id = enum_id.replace(unauthorized_enum_character, replace_by_character)
    return enum_id


def build_sncf_api_city_ids_enum():
    sncf_api_service = SNCF_API_SERVICE()
    city_names = ["Grenoble", "Lyon", "Paris"]
    places = sncf_api_service.fetch_cities_places(city_names)

    build_output_directory = os.path.join("build_python", "sncf_api")
    create_init_files(build_output_directory)
    file_name = "sncf_api_place_ids.py"
    file_path = os.path.join(build_output_directory, file_name)

    build_enum_from_dict(
        enumDict={
            convert_place_name_to_enum_id(place.name): place.id for place in places
        },
        enumClassName="SNCF_API_PLACE_IDS",
        file_path=file_path,
    )


def main():
    load_dotenv()
    build_sncf_api_city_ids_enum()


main()
