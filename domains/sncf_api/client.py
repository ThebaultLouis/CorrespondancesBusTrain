from typing import List
import requests

from domains.sncf_api.model import Place, PlacesApiResponse


class SNCF_API_Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.sncf.com/v1/"
        self.headers = {"Authorization": self.api_key}

    def _make_request(self, endpoint, params=None):
        url = self.base_url + endpoint

        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

    def _fetch_data(self, endpoint, params=None):
        return self._make_request(endpoint, params)

    def fetch_commercial_nodes(self):
        endpoint = "coverage/sncf/commercial_modes"
        return self._fetch_data(endpoint)

    def fetch_places(self, query) -> PlacesApiResponse:
        endpoint = "coverage/sncf/places"
        params = {"q": query, "type": "administrative_region"}
        data = self._fetch_data(endpoint, params)

        return PlacesApiResponse(**data)

    def fetch_travels(self, origin, destination, count=5):
        endpoint = "itineraries"
        # Parameters for the API request
        params = {
            "from": origin,
            "to": destination,
            "datetime": "2024-02-23T12:00:00",  # Date and time of departure in ISO format
            "count": count,  # Number of journeys to retrieve
        }

        return self._fetch_data(endpoint, params)
