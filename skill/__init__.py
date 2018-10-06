from . import intents


def on_session_started(session_started_request, session):
    print("on_session_started")
    pass


def on_session_ended(session_ended_request, session):
    print("on_session_ended")
    pass


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
        "AMAZON.StopIntent": intents.stop
    }

    return intent_mapper[intent_name](request, session)


def handler(event, context):
    print(event["request"])

    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return intents.launch(event["request"], event["session"])

    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])

    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended({"requestId": event["request"]["requestId"]}, event["session"])
