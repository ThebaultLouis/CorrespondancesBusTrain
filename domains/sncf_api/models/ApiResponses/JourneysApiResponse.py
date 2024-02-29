from domains.sncf_api.models.ApiResponses.Common import (
    FeedPublisher,
    Link,
)
from domains.sncf_api.models.Journey import Journey


class JourneysApiResponse:

    def __init__(self, feed_publishers, links, journeys, **kwargs):
        self.feed_publishers: list[FeedPublisher] = [
            FeedPublisher(**publisher) for publisher in feed_publishers
        ]
        self.links = [Link(**link) for link in links]
        self.journeys = [Journey(**journey) for journey in journeys]

    def get_next_link_href(self):
        for link in self.links:
            if link.type == "next":
                return link.href
        return None

    def get_prev_link_href(self):
        for link in self.links:
            if link.type == "prev":
                return link.href
        return None
