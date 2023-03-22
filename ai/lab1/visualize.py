import os
from pathlib import Path
from pprint import pprint

from requests import get


def visualize_path(points: list[tuple[float, float]]):
    key = os.environ.get("GOOGLE_MAPS_STATIC_API_KEY")

    if not key:
        return

    output_path = Path(__file__).parent / "data/vis.png"
    url = "https://maps.googleapis.com/maps/api/staticmap"

    points_as_str = "|".join([f"{lat},{lon}" for (lat, lon) in points])
    query_params = {
        "path": f"color:0xF72D93|weight:5|{points_as_str}",
        "size": "640x640",
        "key": key,
        "zoom": 12.5,
        "center": "51.109398, 17.009742"
    }

    response = get(url, query_params)
    open(output_path, "wb").write(response.content)
