import json
import re


def validate_json(input_str):
    res = False
    try:
        json.loads(input_str)
        res = True
    except:
        pass
    # logger.info(f"input str: {input_str} res: {res}")
    return res


def validate_re(pattern):
    res = False
    try:
        re.compile(pattern)
        is_regex = True
    except re.error:
        is_regex = False
    return res
