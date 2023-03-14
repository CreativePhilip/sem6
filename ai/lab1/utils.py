from math import cos, sqrt


class GeographicalDistanceCalculator:
    """
    Equation from https://en.wikipedia.org/wiki/Geographical_distance#Ellipsoidal_Earth_projected_to_a_plane
    """

    def __init__(
            self,
            lat_1: float,
            lon_1: float,
            lat_2: float,
            lon_2: float
    ):
        self.lat_1 = lat_1
        self.lon_1 = lon_1
        self.lat_2 = lat_2
        self.lon_2 = lon_2

    def compute(self) -> float:
        p1 = (self.K_1() * self.delta_lat()) ** 2
        p2 = (self.K_2() * self.delta_lon()) ** 2

        return sqrt(p1 + p2)

    def delta_lat(self) -> float:
        return self.lat_1 - self.lat_2

    def mean_lat(self) -> float:
        return (self.lat_1 + self.lat_2) / 2

    def delta_lon(self) -> float:
        return self.lon_1 - self.lon_2

    def K_1(self):
        mean_lat = self.mean_lat()
        # TODO: Convert to radians
        return 111.13209 - (0.56605 * cos(2 * mean_lat)) + (0.00120 * cos(4 * mean_lat))

    def K_2(self):
        mean_lat = self.mean_lat()
        # TODO: convert to radians
        return (111.41513 * cos(mean_lat)) - (0.09455 * cos(3 * mean_lat)) + (0.00012 * cos(5 * mean_lat))
