from geopy.geocoders import Nominatim
from math import sqrt

from . import luftdaten_service

ssml_id = "<phoneme alphabet='ipa' ph='ˈaɪˈdi'>ID</phoneme>"


def closest_sensor(address):
    geolocator = Nominatim(user_agent="LuftdatenSkill on Alexa")
    # Create a string out of all values in dict
    user_location = geolocator.geocode(" ".join([address[key] for key in address.keys() if address[key]]))

    sensors = luftdaten_service.get_all_sensors()

    # Get the sensor with the smallest distance
    lowest_distance = float("inf")
    closest_sensor = {
        "id": None,
        "latitude": None,
        "longitude": None
    }

    for sensor in sensors:
        sensor = {
            "id": int(sensor["sensor"]["id"]),
            "latitude": float(sensor["location"]["latitude"]),
            "longitude": float(sensor["location"]["longitude"])
        }

        distance = sqrt(((user_location.latitude - sensor["latitude"]) ** 2) +
                        ((user_location.longitude - sensor["longitude"]) ** 2))

        if distance < lowest_distance:
            lowest_distance = distance
            closest_sensor = {
                "id": sensor["id"],
                "latitude": sensor["latitude"],
                "longitude": sensor["longitude"]
            }

    return closest_sensor
