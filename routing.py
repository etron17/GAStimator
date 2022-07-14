import requests
from typing import Tuple


# MVC pattern - model part
class Routing(object):
    @staticmethod
    def find_dest(departure, destination) -> Tuple[int, float]:
        """
        Find destination between 2 points
        :param departure: Departure point
        :param destination: Destination point
        :return: Tuple with time and km between 2 points
        """
        # API key
        api_key = "YOUR API KEY"

        # Base URL
        url = "YOUR URL"

        # get response
        r = requests.get(
            url + "origins=" + departure + "&destinations=" + destination + "&key=" + api_key)

        time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
        distance = r.json()["rows"][0]["elements"][0]["distance"]["value"]

        return (time, distance)