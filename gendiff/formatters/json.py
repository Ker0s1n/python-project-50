import json


def json_format(node):
    """
    Returns dictionary of changes in JSON format.
    """
    return json.dumps(node, indent=2)
