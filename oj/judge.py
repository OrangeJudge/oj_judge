import os
import shutil
import subprocess

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


JUDGE_PATH = os.path.abspath(os.path.realpath(__file__) + "/../judge/")
SHARE_PATH = JUDGE_PATH + "/share"


SOURCE_FILE = {
    10: "main.c",
    20: "main.cc"
}


COMPILE_SCRIPT = {
    10: "compile_c.sh",
    20: "compile_cpp.sh"
}


COMPILED_FILE = {
    10: "main.out",
    20: "main.out"
}


def _write_solution(language, code):
    if os.path.exists(SHARE_PATH):
        shutil.rmtree(SHARE_PATH)
    os.mkdir(SHARE_PATH)
    solution_path = SHARE_PATH + "/" + SOURCE_FILE[language]
    with open(solution_path, "wb") as f:
        f.write(code)


def _check_compile(language):
    return os.path.exists(SHARE_PATH + "/" + COMPILED_FILE[language])


def _read_compile_error():
    if os.path.exists(SHARE_PATH + "/std.err"):
        with open(SHARE_PATH + "/std.err") as f:
            return f.read()


def compile_solution(language, code):
    _write_solution(language, code)
    output = subprocess.call(["bash", JUDGE_PATH + "/" + COMPILE_SCRIPT[language], SHARE_PATH])
    print("COMPILE CODE: ", output)
    if _check_compile(language):
        return True, None
    else:
        return False, _read_compile_error()


def run_solution(language, test_data):
    pass
