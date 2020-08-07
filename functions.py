from flask import request

def extract(param):
    try:
        extracted_param = request.json[param]
    except Exception as e:
        return None
    return extracted_param