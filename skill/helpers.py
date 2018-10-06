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


def answer(output, reprompt=None, session_attributes={}):
    if reprompt:
        return build_response(
            output_speech={
                "type": "PlainText",
                "text": output
            },
            reprompt={
                "outputSpeech": {
                    "type": "PlainText",
                    "text": reprompt
                }
            },
            should_end_session=True,
            session_attributes=session_attributes
        )
    else:
        return build_response(
            output_speech={
                "type": "PlainText",
                "text": output
            },
            reprompt=None,
            should_end_session=True,
            session_attributes=session_attributes
        )


def question(output, reprompt=None, session_attributes={}):
    if reprompt:
        return build_response(
            output_speech={
                "type": "PlainText",
                "text": output
            },
            reprompt={
                "outputSpeech": {
                    "type": "PlainText",
                    "text": reprompt
                }
            },
            should_end_session=False,
            session_attributes=session_attributes
        )
    else:
        return build_response(
            output_speech={
                "type": "PlainText",
                "text": output
            },
            reprompt=None,
            should_end_session=False,
            session_attributes=session_attributes
        )
