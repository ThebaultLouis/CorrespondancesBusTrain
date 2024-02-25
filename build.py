import json
import os

from dotenv import load_dotenv

from domains.sncf_api.files import SNCF_API_FILES
from domains.sncf_api.service import SNCF_API_SERVICE


def build_enum_from_dict(enumDict: dict, enumClassName: str, file_path: str):
    with open(file_path, "w+") as py_file:
        # Write the Enum class definition
        py_file.write("from enum import Enum\n\n")
        py_file.write(f"class {enumClassName}(Enum):\n")
        # Write enum members
        for key, value in enumDict.items():
            py_file.write(f"    {key} = '{value}'\n")
        print(f"Enum class has been written to {file_path}")


def build_sncf_api_city_ids_enum():
    # sncf_api_files = SNCF_API_FILES()
    # city_id_by_city_names = sncf_api_files.read_city_id_by_city_names_from_files()
    sncf_api_service = SNCF_API_SERVICE()
    city_names = ["Grenoble", "Lyon", "Paris"]
    city_id_by_city_names = sncf_api_service.fetch_city_id_by_city_names(city_names)

    build_output_directory = "build/python/sncf_api/"
    os.makedirs(build_output_directory, exist_ok=True)
    file_name = "sncf_api_city_ids.py"
    file_path = os.path.join(build_output_directory, file_name)

    build_enum_from_dict(
        enumDict=city_id_by_city_names,
        enumClassName="SNCF_API_CITY_IDS",
        file_path=file_path,
    )


def main():
    load_dotenv()
    build_sncf_api_city_ids_enum()


main()
