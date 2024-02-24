from domains.sncf_api.models.ApiResponse import FeedPublisher, Link
from domains.sncf_api.models.Journey import Journey


class JourneysApiResponse:

    def __init__(self, feed_publishers, links, journeys, **kwargs):
        self.feed_publishers = [
            FeedPublisher(**publisher) for publisher in feed_publishers
        ]
        self.links = [Link(**link) for link in links]
        self.journeys = [Journey(**journey) for journey in journeys]
