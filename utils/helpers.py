import json
from typing import List


def json_parser(json_path: str) -> List[List[str]]:
    """
    @param json_path: path to the JSON file containing lyrics
    @return: JSON file parsed into a list of lists containing lines
    """
    with open(json_path) as json_file:
        data = json.load(json_file)
    return data
