def build_response(output_speech, reprompt, should_end_session, session_attributes):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": {
            "outputSpeech": output_speech,
            "reprompt": reprompt,
            "shouldEndSession": should_end_session
        }
    }


def answer(output, reprompt=None, session_attributes={}, ssml=False):
    if reprompt:
        return build_response(
            output_speech={
                "type": "SSML" if ssml else "PlainText",
                "text": output
            },
            reprompt={
                "outputSpeech": {
                    "type": "SSML" if ssml else "PlainText",
                    "text": reprompt
                }
            },
            should_end_session=True,
            session_attributes=session_attributes
        )
    else:
        return build_response(
            output_speech={
                "type": "SSML" if ssml else "PlainText",
                "text": output
            },
            reprompt=None,
            should_end_session=True,
            session_attributes=session_attributes
        )


def question(output, reprompt=None, ssml=False, session_attributes={}):
    if reprompt:
        reprompt_dict = {
            "outputSpeech": {
                "type": "SSML" if ssml else "PlainText",
                "text": reprompt
            }
        }
    else:
        reprompt_dict = None

    return build_response(
        output_speech={
            "type": "SSML" if ssml else "PlainText",
            "text": output
        },
        reprompt=reprompt_dict,
        should_end_session=False,
        session_attributes=session_attributes
    )


def dialog_delegate(updated_intent={}):
    if updated_intent:
        updated_intent_dict = {"updatedIntent": updated_intent}
    else:
        updated_intent_dict = {}

    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "Dialog.Delegate",
                    **updated_intent_dict
                }
            ],
            "shouldEndSession": False
        }
    }


def dialog_elicit(slot_to_elicit, speech, updated_intent={}, ssml=False):
    if updated_intent:
        updated_intent_dict = {"updatedIntent": updated_intent}
    else:
        updated_intent_dict = {}

    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "SSML" if ssml else "PlainText",
                "text": speech,
            },
            "directives": [
                {
                    "type": "Dialog.ElicitSlot",
                    "slotToElicit": slot_to_elicit,
                    **updated_intent_dict
                }
            ],
            "shouldEndSession": False
        }
    }
