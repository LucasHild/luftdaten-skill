from . import intents


def on_session_started(session_started_request, session):
    print("on_session_started")
    return {}


def on_session_ended(session_ended_request, session):
    print("on_session_ended")
    return {}


def on_intent(request, session):
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

    return intent_mapper[intent_name](request, session)


def handler(event, context):
    print("IN:", event["request"])

    if event["session"]["new"]:
        response = on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        response = intents.launch(event["request"], event["session"])

    elif event["request"]["type"] == "IntentRequest":
        response = on_intent(event["request"], event["session"])

    elif event["request"]["type"] == "SessionEndedRequest":
        response = on_session_ended({"requestId": event["request"]["requestId"]}, event["session"])

    print("OUT:", response)
    return response
