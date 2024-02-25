from domains.sncf_api.client import SNCF_API_Client
from domains.sncf_api.models.Journey import Journey


class SNCF_API_SERVICE:

    def __init__(self):
        self.sncf_api_client = SNCF_API_Client()

    def fetch_administrative_region(self, city):
        placesResponse = self.sncf_api_client.fetch_places(city)
        for place in placesResponse.places:
            if hasattr(place, "administrative_region"):
                return place

    def fetch_cities_by_name(self, city_names):
        return [self.fetch_administrative_region(city_name) for city_name in city_names]

    def fetch_city_id_by_city_names(self, city_names):
        cities = self.fetch_cities_by_name(city_names)

        return {city.administrative_region.name: city.id for city in cities}

    def fetch_all_journeys(self, from_place_id, destination_place_id, datetime):
        journeys: list[Journey] = []
        self.sncf_api_client.fetch_journeys(
            from_place_id, destination_place_id, datetime
        )

        return journeys
