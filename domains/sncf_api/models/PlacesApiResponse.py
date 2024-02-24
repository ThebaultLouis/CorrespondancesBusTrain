from domains.sncf_api.models.ApiResponse import FeedPublisher
from domains.sncf_api.models.Place import Place


class PlacesApiResponse:

    def __init__(self, feed_publishers, disruptions, places, **kwargs):
        self.feed_publishers = [
            FeedPublisher(**publisher) for publisher in feed_publishers
        ]
        self.disruptions = disruptions
        self.places = [Place(**place) for place in places]
