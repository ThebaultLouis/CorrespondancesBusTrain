from domains.sncf_api.models.ApiResponses.Common import Link


class Journey:

    def __init__(
        self,
        duration,
        nb_transfers,
        departure_date_time,
        arrival_date_time,
        requested_date_time,
        type,
        status,
        tags,
        co2_emission,
        air_pollutants,
        durations,
        distances,
        fare,
        calendars,
        sections,
        links,
        **kwargs
    ):
        self.duration = duration
        self.nb_transfers = nb_transfers
        self.departure_date_time = departure_date_time
        self.arrival_date_time = arrival_date_time
        self.requested_date_time = requested_date_time
        self.type = type
        self.status = status
        self.tags = tags
        self.co2_emission = co2_emission
        self.air_pollutants = air_pollutants
        self.durations = durations
        self.distances = distances
        self.fare = fare
        self.calendars = [Calendar(**calendar) for calendar in calendars]
        self.sections = [Section(**section) for section in sections]
        self.links = [Link(**link) for link in links]


class Calendar:

    def __init__(self, week_pattern, active_periods):
        self.week_pattern = week_pattern
        self.active_periods = active_periods


class Section:

    def __init__(
        self,
        id,
        duration=0,
        co2_emission=None,
        departure_date_time=None,
        arrival_date_time=None,
        base_departure_date_time=None,
        base_arrival_date_time=None,
        data_freshness=None,
        from_=None,
        additional_informations=None,
        geojson=None,
        mode=None,
        type=None,
        links=None,
        display_informations=None,
        stop_date_times=None,
        **kwargs
    ):
        self.id = id
        self.duration = duration
        self.co2_emission = co2_emission
        self.departure_date_time = departure_date_time
        self.arrival_date_time = arrival_date_time
        self.base_departure_date_time = base_departure_date_time
        self.base_arrival_date_time = base_arrival_date_time
        self.data_freshness = data_freshness
        self.from_ = from_
        self.additional_informations = additional_informations
        self.geojson = geojson
        self.mode = mode
        self.type = type
        self.display_informations = display_informations
        self.stop_date_times = stop_date_times
        self.links = [SectionLink(**link) for link in links]


class SectionLink:
    def __init__(self, id, type):
        self.id = id
        self.type = type


class StopDateTime:
    def __init__(
        self,
        departure_date_time,
        base_departure_date_time,
        arrival_date_time,
        base_arrival_date_time,
        stop_point,
        additional_informations,
        links,
    ):
        self.departure_date_time = departure_date_time
        self.base_departure_date_time = base_departure_date_time
        self.arrival_date_time = arrival_date_time
        self.base_arrival_date_time = base_arrival_date_time
        self.stop_point = stop_point
        self.additional_informations = additional_informations
        self.links = [Link(**link) for link in links]
