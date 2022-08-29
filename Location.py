#Use this class to get the coordinates of a specified place
import os
import requests
from dotenv import load_dotenv
class Location:
    def __init__(self, address, **location):
        load_dotenv("env.env")
        self.address = address
        self.city = location.get("city")
    def get_latitude_longitude(self):
        params = {
            "access_key": os.getenv("GEOPOS_API_KEY"),
            # Use ternary condition operator
            "query": {self.address} if self.address != "" else "",
            "region": {self.city} if self.city != "" else "",
            "limit": 1,
            "output": "json",
        }
        data = requests.get(url="http://api.positionstack.com/v1/forward", params=params).json()
        return (data['data'][0]['latitude'],data['data'][0]['longitude'])






