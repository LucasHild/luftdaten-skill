from .helpers import answer, question
from . import luftdaten_service


def launch(request, session):
    location = "Stuttgart"

    first_usage = True

    value = luftdaten_service.get_value(924)

    speech = f"Die Feinstaubbelastung in {location} liegt aktuell bei {value} Mikrogramm."

    if first_usage:
        return question((
            f"Willkommen zum Luftdaten Skill. {speech} Standardmäßig verwende ich die Position deines Echos, "
            "um Dir die Feinstaubbelastung anzugeben. "
            "Du kannst mich aber auch einfach nach einer anderen Stadt fragen. Falls Du einen eigenen Sensor hast, "
            "kannst Du diesen auch verwenden. Sage dafür einfach: Verwende meinen eigenen Feinstaubsensor."))

    return speech


def setup_sensor(request, session):
    return question("Diese Funktion wird aktuell noch entwickelt. Setup Sensor Intent")


def sensor_value(request, session):
    return question("Diese Funktion wird aktuell noch entwickelt. Sensor Value Intent")


def location_value(request, session):
    return question("Diese Funktion wird aktuell noch entwickelt. Location Value Intent")


def my_sensor_value(request, session):
    return question("Diese Funktion wird aktuell noch entwickelt. My Sensor Value Intent")


def my_location_value(request, session):
    return question("Diese Funktion wird aktuell noch entwickelt. My Location Value Intent")


def stop(request, session):
    return answer("Bis bald.")


def help(request, session):
    return question("Diese Funktion wird aktuell noch entwickelt.")
