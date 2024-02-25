from dotenv import load_dotenv
from domains.sncf_api.files import SNCF_API_FILES


def init():
    sncf_api_files = SNCF_API_FILES()
    # sncf_api_files.save_city_id_by_city_names_to_files()
    sncf_api_files.save_journeys_to_files()


def main():
    load_dotenv()
    init()


main()
