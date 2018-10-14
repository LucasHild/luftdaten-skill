from . import db, luftdaten_service, utils, alexa_service
from .helpers import answer, question, dialog_delegate, dialog_elicit


def launch(request, session, context):
    user = db.get_user(session["user"]["userId"])
    card = None

    if user.get("sensor_id"):
        sensor_id = int(user["sensor_id"])
        value = luftdaten_service.get_value(sensor_id)
        if value:
            speech = f"Die Feinstaubbelastung an deinem Sensor {sensor_id} liegt bei {value} Mikrogramm."
        else:
            speech = (f"Ich kann Deinen Sensor {sensor_id} aktuell leider nicht erreichen. "
                      "Bitte überprüfe, ob er eingeschaltet ist und Daten sendet.")

    else:
        location = alexa_service.get_user_location(context["System"])
        if location:
            sensor = utils.closest_sensor(location)
            value = luftdaten_service.get_value(sensor["id"])
            speech = f"Die Feinstaubbelastung in Deiner Umgebung liegt aktuell bei {value} Mikrogramm."
        else:
            card = {
                "type": "AskForPermissionsConsent",
                "permissions": [
                    "read::alexa:device:all:address"
                ]
            }
            speech = ("Bevor ich auf Deinen Standort zugreifen kann brauche ich Zugriff auf Deinen Standort. "
                      "Öffne dafür die Alexa App und gib dem Skill angefragte Berechtigung.")

    return question(f"{speech} Kann ich sonst noch etwas für Dich tun?", card=card)


def setup_sensor(request, session, context):
    if request["dialogState"] == "STARTED":
        return dialog_delegate()
    elif request["dialogState"] == "IN_PROGRESS":
        return dialog_delegate()

    # TODO Check sensor id

    try:
        sensor_id = int(request["intent"]["slots"]["SensorID"]["value"])
    except ValueError:
        return dialog_elicit(
            "SensorID",
            (f"Das ist keine gültige Sensor {utils.ssml_id}. Eine typische Sensor {utils.ssml_id} ist eine "
             f"Zahl zwischen 1 und 20 Tausend. Wie lautet deine Sensor {utils.ssml_id}?"),
            updated_intent={
                "name": "SetupSensorIntent",
                "confirmationStatus": "NONE",
                "slots": {
                    "SensorID": {
                        "name": "SensorID",
                        "confirmationStatus": "NONE"
                    }
                }
            })

    db.set_sensor_id(session["user"]["userId"], sensor_id)

    return answer(("Perfekt, ab jetzt gebe ich Dir standardmäßig die Feinstaubwerte von deinem Sensor mit der "
                   f"ID {sensor_id} zurück."))

    # Waiting for issue
    return answer((
        "<speak>Perfekt, ab jetzt gebe ich Dir standardmäßig die Feinstaubwerte von deinem Sensor mit der "
        f"{utils.ssml_id} {sensor_id} zurück.</speak>"), ssml=False)


def sensor_value(request, session, context):
    return question("Diese Funktion wird aktuell noch entwickelt. Sensor Value Intent")


def location_value(request, session, context):
    return question("Diese Funktion wird aktuell noch entwickelt. Location Value Intent")


def my_sensor_value(request, session, context):
    user = db.get_user(session["user"]["userId"])

    if user.get("sensor_id"):
        sensor_id = int(user["sensor_id"])
        value = luftdaten_service.get_value(sensor_id)
        if value:
            speech = f"Die Feinstaubbelastung an deinem Sensor {sensor_id} liegt bei {value} Mikrogramm."
        else:
            speech = (f"Ich kann Deinen Sensor {sensor_id} aktuell leider nicht erreichen. "
                      "Bitte überprüfe, ob er eingeschaltet ist und Daten sendet.")
    else:
        return question(("Du hast noch keinen Sensor eingerichtet. "
                         "Um das zu tun, sage einfach: Verwende meinen eigenen Feinstaubsensor."))

    return question(f"{speech} Kann ich sonst noch etwas für Dich tun?")


def my_location_value(request, session, context):
    return question("Diese Funktion wird aktuell noch entwickelt. My Location Value Intent")


def stop(request, session, context):
    return answer("Bis bald.")


def help(request, session, context):
    return question("Diese Funktion wird aktuell noch entwickelt.")
