import os
import requests

from domains.sncf_api.models.ApiResponses.Common import ApiResponseError
from domains.sncf_api.models.ApiResponses.JourneysApiResponse import JourneysApiResponse
from domains.sncf_api.models.ApiResponses.PlacesApiResponse import PlacesApiResponse


class SNCF_API_Client:

    def __init__(self):
        self.api_key = os.environ.get("SNCF_API_KEY")
        self.base_url = "https://api.sncf.com/v1/"
        self.headers = {"Authorization": self.api_key}

    def _make_request(self, endpoint, params: dict = None):
        url = self.base_url + endpoint

        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            if "error" in data:
                apiResponseError = ApiResponseError(**data["error"])
                raise Exception(str(apiResponseError))
            return data
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

    def _fetch_data(self, endpoint, params=None):
        return self._make_request(endpoint, params)

    def fetch_commercial_nodes(self):
        endpoint = "coverage/sncf/commercial_modes"
        return self._fetch_data(endpoint)

    def fetch_places(self, query):
        endpoint = "coverage/sncf/places"
        params = {"q": query}
        data = self._fetch_data(endpoint, params)

        return PlacesApiResponse(**data)

    def fetch_journeys(self, from_place_id, destination_place_id, datetime, count=5):
        endpoint = "coverage/sncf/journeys"
        # Parameters for the API request
        params = {
            "from": from_place_id,
            "to": destination_place_id,
            "datetime": datetime,  # Date and time of departure in ISO format e.g "2024-02-23T12:00:00"
            "count": count,  # Number of journeys to retrieve
        }
        data = self._fetch_data(endpoint, params)
        return JourneysApiResponse(**data)
