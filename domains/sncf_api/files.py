import json
import os
import shutil
from build_python.sncf_api.sncf_api_place_ids import SNCF_API_PLACE_IDS

from domains.helper.json_encoder import convert_python_object_to_dict
from domains.sncf_api.client import SNCF_API_Client
from domains.sncf_api.service import SNCF_API_SERVICE

CITIES_JSON_FILE_PATH = "cities.json"
JOURNEYS_DIRECTORY = "journeys"


class SNCF_API_FILES:

    def __init__(self, build_directory="build/sncf_api"):
        self.sncf_api_client = SNCF_API_Client()
        self.sncf_api_service = SNCF_API_SERVICE()
        self.build_directory = build_directory
        # self._cleanup()

    def _cleanup(self):
        if os.path.exists(self.build_directory):
            shutil.rmtree(self.build_directory)
        os.makedirs(self.build_directory)

    def _get_build_path(self, file_path):
        return f"{self.build_directory}/{file_path}"

    def save_object_to_json_file(self, python_object, file_path="data.json"):
        build_file_path = self._get_build_path(file_path)
        os.makedirs(os.path.dirname(build_file_path), exist_ok=True)
        with open(build_file_path, "w+") as json_file:
            json.dump(convert_python_object_to_dict(python_object), json_file, indent=2)

    def save_city_id_by_city_names_to_files(self):
        city_names = ["Grenoble", "Lyon", "Paris"]
        data = self.sncf_api_service.fetch_city_id_by_city_names(city_names)
        self.save_object_to_json_file(data, CITIES_JSON_FILE_PATH)

    def read_city_id_by_city_names_from_files(self):
        with open(self._get_build_path(CITIES_JSON_FILE_PATH), "r") as json_file:
            data: dict = json.load(json_file)
            return data

    def save_journeys_to_files(self):
        from_city_to_city_correspondances = [
            # (SNCF_API_PLACE_IDS.Grenoble, SNCF_API_PLACE_IDS.Paris),
            (
                SNCF_API_PLACE_IDS.GRENOBLE__GRENOBLE,
                SNCF_API_PLACE_IDS.LYON_PART_DIEU__LYON,
            ),
            # (SNCF_API_PLACE_IDS.Lyon, SNCF_API_PLACE_IDS.Paris),
        ]

        day = "2024-03-09"
        # datetime = "2024-03-09T00:00:00"
        datetime_journeys_path = os.path.join(JOURNEYS_DIRECTORY, day)
        os.makedirs(datetime_journeys_path, exist_ok=True)

        for from_city_to_city_correspondance in from_city_to_city_correspondances:
            from_city, destination_city = from_city_to_city_correspondance
            journeys = self.sncf_api_service.fetch_all_daily_journeys(
                from_place_id=from_city.value,
                destination_place_id=destination_city.value,
                day=day,
            )

            journeys_save_path = os.path.join(
                datetime_journeys_path, f"{from_city.name}-{destination_city.name}.json"
            )

            self.save_object_to_json_file(
                journeys,
                journeys_save_path,
            )

            print(f"Saved {len(journeys)} to {journeys_save_path}")
