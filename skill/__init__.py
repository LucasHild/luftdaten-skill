from . import db, intents
from .helpers import question


def on_session_started(session_started_request, session):
    print("on_session_started")
    return {}


def on_session_ended(session_ended_request, session):
    print("on_session_ended")
    return {}


def on_intent(request, session, context):
    intent_name = request["intent"]["name"]

    intent_mapper = {
        "SensorValueIntent": intents.sensor_value,
        "MySensorValueIntent": intents.my_sensor_value,
        "MyLocationValueIntent": intents.my_location_value,
        "SetupSensorIntent": intents.setup_sensor,
        "LocationValueIntent": intents.location_value,
        "AMAZON.CancelIntent": intents.stop,
        "AMAZON.HelpIntent": intents.help,
        "AMAZON.NavigateHomeIntent": intents.launch,
        "AMAZON.NoIntent": intents.stop,
        "AMAZON.StopIntent": intents.stop
    }

    return intent_mapper[intent_name](request, session, context)


def handler(event, context):
    print("IN:", event)

    # New user
    user = db.get_user(event["session"]["user"]["userId"])
    if not user:
        db.add_user(event["session"]["user"]["userId"])
        return question((
            "Willkommen zum Luftdaten Skill. Standardmäßig verwende ich die Position deines Echos, "
            "um Dir die Feinstaubbelastung anzugeben. "
            "Du kannst mich aber auch einfach nach einer anderen Stadt fragen. Falls Du einen eigenen Sensor hast, "
            "kannst Du diesen auch verwenden. Sage dafür einfach: Verwende meinen eigenen Feinstaubsensor."))

    if event["session"]["new"]:
        response = on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        response = intents.launch(event["request"], event["session"], event["context"])

    elif event["request"]["type"] == "IntentRequest":
        response = on_intent(event["request"], event["session"], event["context"])

    elif event["request"]["type"] == "SessionEndedRequest":
        response = on_session_ended({"requestId": event["request"]["requestId"]}, event["session"])

    print("OUT:", response)
    return response
