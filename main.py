import os

from dotenv import load_dotenv

from domains.sncf_api.client import SNCF_API_Client
from domains.sncf_api.service import SNCF_API_SERVICE


def main():
    load_dotenv()
    sncf_api_key = os.environ.get("SNCF_API_KEY")
    sncf_api_client = SNCF_API_Client(sncf_api_key)
    sncf_api_service = SNCF_API_SERVICE(sncf_api_client)
    city_names = ["Grenoble", "Lyon", "Paris"]
    print(sncf_api_service.fetch_city_id_by_city_names(city_names))


main()
