import json
import os
import shutil

from dotenv import load_dotenv

from domains.sncf_api.client import SNCF_API_Client
from domains.sncf_api.resources import CityID
from domains.sncf_api.service import SNCF_API_SERVICE


BUILD_DIRECTORY = "build"
CITIES_JSON_FILE_PATH = "cities.json"
JOURNEYS_DIRECTORY = "journeys"


def save_result_json_file(data, file_path="data.json"):
    with open(f"{BUILD_DIRECTORY}/{file_path}", "w+") as json_file:
        json.dump(data, json_file, indent=2)


def save_cities_id(sncf_api_service: SNCF_API_SERVICE):
    city_names = ["Grenoble", "Lyon", "Paris"]
    data = sncf_api_service.fetch_city_id_by_city_names(city_names)
    save_result_json_file(data, CITIES_JSON_FILE_PATH)


def save_journeys(sncf_api_client: SNCF_API_Client):
    from_city_to_city_correspondances = [
        (CityID.Grenoble, CityID.Paris),
        # (CityID.Grenoble, CityID.Lyon),
        # (CityID.Lyon, CityID.Paris),
    ]

    datetime = "2024-02-23T12:00:00"
    datetime_journeys_path = f"{JOURNEYS_DIRECTORY}/{datetime}"

    build_datetime_journeys_path = f"{BUILD_DIRECTORY}/{datetime_journeys_path}"
    if os.path.exists(build_datetime_journeys_path):
        shutil.rmtree(build_datetime_journeys_path)
    os.makedirs(build_datetime_journeys_path)

    for from_city_to_city_correspondance in from_city_to_city_correspondances:
        from_city = from_city_to_city_correspondance[0]
        destination_city = from_city_to_city_correspondance[1]
        journeys = sncf_api_client.fetch_journeys(
            from_place_id=from_city.value,
            destination_place_id=destination_city.value,
            datetime=datetime,
        )
        save_result_json_file(
            journeys,
            f"{datetime_journeys_path}/{from_city.name}-{destination_city.name}",
        )


def main():
    load_dotenv()
    sncf_api_key = os.environ.get("SNCF_API_KEY")
    sncf_api_client = SNCF_API_Client(sncf_api_key)
    sncf_api_service = SNCF_API_SERVICE(sncf_api_client)

    save_cities_id(sncf_api_service)
    save_journeys(sncf_api_client)


main()
