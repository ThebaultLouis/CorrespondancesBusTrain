import json
import os

from dotenv import load_dotenv

from domains.sncf_api.client import SNCF_API_Client
from domains.sncf_api.resources import CityID
from domains.sncf_api.service import SNCF_API_SERVICE


def save_result_json_file(data, file_path="build/data.json"):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)


def main():
    load_dotenv()
    sncf_api_key = os.environ.get("SNCF_API_KEY")
    sncf_api_client = SNCF_API_Client(sncf_api_key)
    sncf_api_service = SNCF_API_SERVICE(sncf_api_client)

    # city_names = ["Grenoble", "Lyon", "Paris"]
    # print(sncf_api_service.fetch_city_id_by_city_names(city_names))

    travels = sncf_api_client.fetch_travels(
        from_place_id=CityID.Grenoble.value,
        destination_place_id=CityID.Lyon.value,
        datetime="2024-02-23T12:00:00",
    )
    save_result_json_file(travels)


main()
