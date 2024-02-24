class Coord:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat


class AdministrativeRegion:
    def __init__(self, id, name, level, zip_code, label, insee, coord):
        self.id = id
        self.name = name
        self.level = level
        self.zip_code = zip_code
        self.label = label
        self.insee = insee
        self.coord = Coord(**coord)


class Codes:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class StopArea:
    def __init__(
        self, id, name, codes, timezone, label, coord, links, administrative_regions
    ):
        self.id = id
        self.name = name
        self.codes = [Codes(**code) for code in codes]
        self.timezone = timezone
        self.label = label
        self.coord = Coord(**coord)
        self.links = links
        self.administrative_regions = [
            AdministrativeRegion(**admin) for admin in administrative_regions
        ]


class Place:
    def __init__(
        self,
        id,
        name,
        quality,
        embedded_type,
        stop_area=None,
        administrative_region=None,
    ):
        self.id = id
        self.name = name
        self.quality = quality
        self.embedded_type = embedded_type
        if embedded_type == "stop_area":
            self.stop_area = StopArea(**stop_area)
        elif embedded_type == "administrative_region":
            self.administrative_region = AdministrativeRegion(**administrative_region)


class FeedPublisher:
    def __init__(self, id, name, url, license):
        self.id = id
        self.name = name
        self.url = url
        self.license = license


class PlacesApiResponse:

    def __init__(self, feed_publishers, disruptions, places, **kwargs):
        self.feed_publishers = [
            FeedPublisher(**publisher) for publisher in feed_publishers
        ]
        self.disruptions = disruptions
        self.places = [Place(**place) for place in places]
