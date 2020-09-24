import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("skill")


def evaluate(payload: dict, context: dict) -> dict:
    request = payload['request']
    response = request.upper()
    return {'response': f'you wrote: {response}'}


def on_started(context):
    log.info("on_started triggered")
