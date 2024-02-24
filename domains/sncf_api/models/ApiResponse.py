class FeedPublisher:
    def __init__(self, id, name, url, license):
        self.id = id
        self.name = name
        self.url = url
        self.license = license


class Link:
    def __init__(self, href, templated, rel, type):
        self.href = href
        self.templated = templated
        self.rel = rel
        self.type = type
