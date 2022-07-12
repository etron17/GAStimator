import requests
from typing import Tuple

# API key
api_key = "YOUR API KEY"

# Base URL
url = "YOUR URL"

def find_dest(departure, destination) -> Tuple[int, float]:
    """
    Get ETA between departure and destination
    :param departure: Departure point
    :param destination: Destination point
    :return: Tuple with time and distance between 2 points
    """

    # Get response
    r = requests.get(
        url + "orignins=" +departure + "&destinations=" + destination + "&key=" + api_key)

    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    distance = r.json()["rows"][0]["elements"][0]["distance"]["value"]

    return (time, distance)