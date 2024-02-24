from domains.sncf_api.client import SNCF_API_Client


class SNCF_API_SERVICE:

    def __init__(self, sncf_api_client: SNCF_API_Client):
        self.sncf_api_client = sncf_api_client

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
