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


def recognize_re(s):
    if "[" in s and "]" in s:
        is_regex = True
    else:
        is_regex = False
    return is_regex
