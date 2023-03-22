import dataclasses
import time
from datetime import timedelta, date

from utils import GeographicalDistanceCalculator, parse_date_string


@dataclasses.dataclass(eq=True)
class MpkGraphNode:
    name: str
    time: timedelta
    lat: float
    lon: float
    hash: int = 0

    def __eq__(self, other):
        return self.name == other.name and self.time == other.time

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if self.hash == 0:
            self.hash = hash((self.name, self.time.total_seconds()))

        return self.hash


class MpkGraphEdge:
    def __init__(
            self,
            line,
            arrival_time,
            departure_time,
            end_stop,
            end_stop_lat,
            end_stop_lon,
            start_stop,
            start_stop_lat,
            start_stop_lon,
            **_
    ):
        self.line = line
        self.departure_time = parse_date_string(departure_time)
        self.arrival_time = parse_date_string(arrival_time)

        self.raw_arrival_time = arrival_time
        self.raw_departure_time = departure_time

        self.end_stop = end_stop
        self.end_stop_lat = float(end_stop_lat)
        self.end_stop_lon = float(end_stop_lon)

        self.start_stop = start_stop
        self.start_stop_lat = float(start_stop_lat)
        self.start_stop_lon = float(start_stop_lon)

    def distance(self):
        return GeographicalDistanceCalculator(
            self.start_stop_lat,
            self.start_stop_lon,
            self.end_stop_lat,
            self.end_stop_lon
        ).compute()

    def start_as_node(self) -> MpkGraphNode:
        return MpkGraphNode(
            name=self.start_stop,
            time=self.departure_time,
            lat=self.start_stop_lat,
            lon=self.start_stop_lon,
        )

    def end_as_node(self) -> MpkGraphNode:
        return MpkGraphNode(
            name=self.end_stop,
            time=self.arrival_time,
            lat=self.end_stop_lat,
            lon=self.end_stop_lon,
        )

    def __str__(self):
        return f"Node<{self.start_stop} - {self.end_stop}> {self.arrival_time}"
