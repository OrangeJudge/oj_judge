import os
import shutil
import subprocess
from problem import PROBLEM_BASE_PATH

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


RUN_SCRIPT = {
    10: "run_c.sh",
    20: "run_cpp.sh"
}



def _write_solution(language, code):
    if os.path.exists(SHARE_PATH):
        shutil.rmtree(SHARE_PATH)
    os.mkdir(SHARE_PATH)
    solution_path = SHARE_PATH + "/" + SOURCE_FILE[language]
    with open(solution_path, "wb") as f:
        f.write(code)


def _delete_solution(language):
    solution_path = SHARE_PATH + "/" + SOURCE_FILE[language]
    os.remove(solution_path)


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
    _delete_solution(language)
    if _check_compile(language):
        return True, None
    else:
        return False, _read_compile_error()


def _prepare_input(problem_id, input_file_name):
    subprocess.call(["bash", JUDGE_PATH + "/remove_temp.sh", SHARE_PATH])
    shutil.copyfile(PROBLEM_BASE_PATH + "/" + str(problem_id) + "/" + input_file_name, SHARE_PATH + "/std.in")


def _run_once(language, time_limit, memory_limit):
    output = subprocess.call(["bash", JUDGE_PATH + "/" + RUN_SCRIPT[language], SHARE_PATH,
                              str(time_limit / 1000 + 2), str(memory_limit)])
    print("RUN CODE:", output)


def _read_output():
    output_dict = dict()
    if os.path.exists(SHARE_PATH + "/std.err"):
        with open(SHARE_PATH + "/std.err") as f:
            output_dict["err"] = f.read()
    if os.path.exists(SHARE_PATH + "/std.out"):
        with open(SHARE_PATH + "/std.out") as f:
            output_dict["out"] = f.read()
    total_time = 0
    if os.path.exists(SHARE_PATH + "/time.txt"):
        with open(SHARE_PATH + "/time.txt") as f:
            time_string = f.read()
            for line in time_string.split("\n"):
                line_split = line.split("\t")
                if line_split[0] == "user" or line_split[0] == "sys":
                    time_split = line_split[1].split("m")
                    total_time += int(time_split[0]) * 60 * 1000 + int(float(time_split[1][:-1])*1000)
    output_dict["time"] =  total_time
    print(output_dict)


def run_solution(language, problem_id, test_id, test_data):
    _prepare_input(problem_id, str(test_id) + ".in")
    _run_once(language, test_data["timeLimit"], test_data["memoryLimit"])
    _read_output()
