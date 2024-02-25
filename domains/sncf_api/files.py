import json
import os
import shutil

from build.python.sncf_api.sncf_api_city_ids import SNCF_API_CITY_IDS
from domains.sncf_api.client import SNCF_API_Client
from domains.sncf_api.service import SNCF_API_SERVICE

CITIES_JSON_FILE_PATH = "cities.json"
JOURNEYS_DIRECTORY = "journeys"


class SNCF_API_FILES:

    def __init__(self, build_directory="build/sncf_api"):
        self.sncf_api_client = SNCF_API_Client()
        self.sncf_api_service = SNCF_API_SERVICE(self.sncf_api_client)
        self.build_directory = build_directory
        # self._cleanup()

    def _cleanup(self):
        if os.path.exists(self.build_directory):
            shutil.rmtree(self.build_directory)
        os.makedirs(self.build_directory)

    def _get_build_path(self, file_path):
        return f"{self.build_directory}/{file_path}"

    def save_result_json_file(self, data, file_path="data.json"):
        with open(self._get_build_path(file_path), "w+") as json_file:
            json.dump(data, json_file, indent=2)

    def save_city_id_by_city_names_to_files(self):
        city_names = ["Grenoble", "Lyon", "Paris"]
        data = self.sncf_api_service.fetch_city_id_by_city_names(city_names)
        self.save_result_json_file(data, CITIES_JSON_FILE_PATH)

    def read_city_id_by_city_names_from_files(self):
        with open(self._get_build_path(CITIES_JSON_FILE_PATH), "r") as json_file:
            data: dict = json.load(json_file)
            return data

    def save_journeys_to_files(self):
        from_city_to_city_correspondances = [
            # (SNCF_API_CITY_IDS.Grenoble, SNCF_API_CITY_IDS.Paris),
            (SNCF_API_CITY_IDS.Grenoble, SNCF_API_CITY_IDS.Lyon),
            # (SNCF_API_CITY_IDS.Lyon, SNCF_API_CITY_IDS.Paris),
        ]

        datetime = "2024-02-23T12:00:00"
        datetime_journeys_path = os.path.join(JOURNEYS_DIRECTORY, datetime)

        for from_city_to_city_correspondance in from_city_to_city_correspondances:
            from_city, destination_city = from_city_to_city_correspondance
            journeys = self.sncf_api_service.fetch_all_journeys(
                from_place_id=from_city.value,
                destination_place_id=destination_city.value,
                datetime=datetime,
            )
            journeys_save_path = os.path.join(
                datetime_journeys_path, f"{from_city.name}-{destination_city.name}"
            )

            self.save_result_json_file(
                journeys,
                journeys_save_path,
            )
