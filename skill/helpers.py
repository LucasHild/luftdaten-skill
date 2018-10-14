def build_response(output_speech, reprompt, should_end_session, session_attributes, card=None):
    if card:
        card_dict = {"card": card}
    else:
        card_dict = {}

    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": {
            "outputSpeech": output_speech,
            **card_dict,
            "reprompt": reprompt,
            "shouldEndSession": should_end_session
        }
    }


def answer(output, reprompt=None, session_attributes={}, card=None, ssml=False):
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
        session_attributes=session_attributes,
        card=card
    )


def question(output, reprompt=None, ssml=False, session_attributes={}, card=None):
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
        session_attributes=session_attributes,
        card=card
    )


def dialog_delegate(updated_intent={}, card=None):
    if updated_intent:
        updated_intent_dict = {"updatedIntent": updated_intent}
    else:
        updated_intent_dict = {}

    if card:
        card_dict = {"card": card}
    else:
        card_dict = {}

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
            **card_dict,
            "shouldEndSession": False
        }
    }


def dialog_elicit(slot_to_elicit, speech, updated_intent={}, card=None, ssml=False):
    if updated_intent:
        updated_intent_dict = {"updatedIntent": updated_intent}
    else:
        updated_intent_dict = {}

    if card:
        card_dict = {"card": card}
    else:
        card_dict = {}

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
            **card_dict,
            "shouldEndSession": False
        }
    }
