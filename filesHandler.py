import json
import logging
from os import path


def read_json(file_path):
    """ Return json data or create a log file if no path to an existing file. """
    if path.isfile(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        logging.basicConfig(filename='json.log', level=logging.DEBUG)
        logging.debug(f'File {file_path} not found.')
        return {}


def write_json(file_path, data):
    """ Create json file with the data. """
    with open(file_path, "w", encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
