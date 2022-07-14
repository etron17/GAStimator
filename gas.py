import requests
import json
from typing import Dict

# MVC pattern - model part
class Gas(object):

    def __init__(self) -> None:
        super().__init__()

    def get_prices(self) -> Dict:

        """
        Get gas prices for Canada
        :return: Dictionary of gas prices per province
        """

        url = "YOUR URL"

        headers = {
            "X-RapidAPI-Key": "YOUR KEY",
            "X-RapidAPI-Host": "YOUR HOST"
        }

        response = requests.request("GET", url, headers=headers)
        gas_dict = json.loads(response.text)
        return gas_dict["prices"]