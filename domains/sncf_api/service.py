from typing import List
from domains.sncf_api.client import SNCF_API_Client
from domains.sncf_api.models.Journey import Journey
from domains.sncf_api.models.Place import Place


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

    def fetch_cities_places(self, city_names: List[str]):
        places: List[Place] = []
        for city_name in city_names:
            placesResponse = self.sncf_api_client.fetch_places(city_name)
            for place in placesResponse.places:
                places.append(place)
        return places

    def fetch_all_daily_journeys(self, from_place_id, destination_place_id, day):
        journeys: list[Journey] = []
        last_journey_datetime = f"{day}T00:00:00"
        has_tomorrow_journeys = False

        while not has_tomorrow_journeys:
            response = self.sncf_api_client.fetch_journeys(
                from_place_id, destination_place_id, last_journey_datetime, count=10
            )
            for journey in response.journeys:
                if day.replace("-", "") in journey.departure_date_time:
                    journeys.append(journey)
                else:
                    return journeys
            last_journey_datetime = journeys[-1].departure_date_time
