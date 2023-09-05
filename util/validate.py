import json
from util.log import logger


def validate_json(input_str):
    res = False
    try:
        json.loads(input_str)
        res = True
    except:
        pass
    # logger.info(f"input str: {input_str} res: {res}")
    return res
