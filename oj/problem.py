import os
import json
from oj import remote

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"

PROBLEM_BASE_PATH = os.path.abspath(os.path.realpath(__file__) + "/../../problems/")
STORE_FILE_PATH = PROBLEM_BASE_PATH + "problem_hash.json"


def _store_hash(problem_id, hash_code):
    problem_id = str(problem_id)
    if os.path.exists(STORE_FILE_PATH):
        json_dict = json.load(open(STORE_FILE_PATH))
    else:
        json_dict = dict()
    json_dict[problem_id] = hash_code
    with open(STORE_FILE_PATH, "wb") as f:
        f.writelines(json.dumps(json_dict))


def _read_hash(problem_id):
    problem_id = str(problem_id)
    if os.path.exists(STORE_FILE_PATH):
        json_dict = json.load(open(STORE_FILE_PATH))
        if problem_id in json_dict:
            return json_dict[problem_id]
    return None


def _read_problem_define(problem_id):
    problem_json_file = PROBLEM_BASE_PATH + "/" + str(problem_id) + "/problem.json"
    print problem_json_file
    if os.path.exists(problem_json_file):
        return json.load(open(problem_json_file))


def get_problem(problem_id, hash_code):
    original_hash = _read_hash(problem_id)
    if original_hash != hash_code:
        remote.fetch_problem(problem_id)
        _store_hash(problem_id, hash_code)
    return _read_problem_define(problem_id)

