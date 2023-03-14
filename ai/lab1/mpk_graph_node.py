import time
from decimal import Decimal

from utils import GeographicalDistanceCalculator


class MpkGraphNode:
    line: str
    arrival_time: str
    departure_time: str

    raw_arrival_time: str
    raw_departure_time: str

    end_stop: str
    end_stop_lat: Decimal
    end_stop_lon: Decimal

    start_stop: str
    start_stop_lat: Decimal
    start_stop_lon: Decimal

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
        self.departure_time = time.strptime(departure_time, "%H:%M:%S")
        self.arrival_time = time.strptime(arrival_time, "%H:%M:%S")

        self.raw_arrival_time = arrival_time
        self.raw_departure_time = departure_time

        self.end_stop = end_stop
        self.end_stop_lat = Decimal(end_stop_lat)
        self.end_stop_lon = Decimal(end_stop_lon)

        self.start_stop = start_stop
        self.start_stop_lat = Decimal(start_stop_lat)
        self.start_stop_lon = Decimal(start_stop_lon)

    def distance(self):
        return GeographicalDistanceCalculator(
            self.start_stop_lat,
            self.start_stop_lon,
            self.end_stop_lat,
            self.end_stop_lon
        ).compute()

    def __str__(self):
        return f"Node<{self.start_stop} - {self.end_stop}> {self.raw_arrival_time}"
