import os
import subprocess

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


JUDGE_PATH = os.path.abspath(os.path.realpath(__file__) + "/../judge/")
SHARE_PATH = JUDGE_PATH + "/share"


def _write_solution(language, code):
    solution_path = SHARE_PATH + "/main.cc"
    with open(solution_path, "wb") as f:
        f.write(code)


def compile_solution(language, code):
    _write_solution(language, code)
    output = subprocess.call(["bash", JUDGE_PATH + "/compile_cpp.sh", SHARE_PATH])
    print(output)


def run_solution(language, test_data):
    pass
