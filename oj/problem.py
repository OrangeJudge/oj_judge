import os
import json


__author__ = 'xinzzhou'


store_file_path = os.path.abspath(os.path.dirname(__file__) + "/../problems/problem_hash.json")


def _store_hash(problem_id, hash_code):
    problem_id = str(problem_id)
    if os.path.exists(store_file_path):
        json_dict = json.load(open(store_file_path))
    else:
        json_dict = dict()
    json_dict[problem_id] = hash_code
    with open(store_file_path, "wb") as f:
        f.writelines(json.dumps(json_dict))


def _read_hash(problem_id):
    problem_id = str(problem_id)
    if os.path.exists(store_file_path):
        json_dict = json.load(open(store_file_path))
        if problem_id in json_dict:
            return json_dict[problem_id]
    return None
