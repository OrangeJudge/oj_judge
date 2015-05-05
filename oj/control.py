import copy
import time
from oj import remote, problem, judge


__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


def start_judge():
    while True:
        if not tick():
            time.sleep(5)


def tick():
    fetched = remote.fetch_solution()
    print(fetched)
    if fetched is None:
        return False
    if fetched["status"] != 0:
        return False
    solution_data = fetched["data"]
    solution_id = solution_data["solution"]
    problem_data = problem.get_problem(solution_data["problem"], solution_data["problem_hash"])
    remote.update_status(solution_id, 100, "Compiling", None, None)
    compile_status, compile_error = judge.compile_solution(solution_data["language"],
                                                           solution_data["code"])
    print(compile_status, compile_error)
    if not compile_status:
        remote.update_status(solution_id, 400, "Compilation Error\n" + str(compile_error))
        return
    default_test = problem_data["default"]
    total_time = 0
    total_memory = 0
    all_pass = True
    for test in range(1, problem_data["numberOfTestCases"] + 1):
        # TODO: add special test cases.
        test_data = copy.copy(default_test)
        if "specialCases" in problem_data and str(test) in problem_data["specialCases"]:
            for key, value in problem_data["specialCases"][str(test)].iteritems():
                test_data[key] = value
        remote.update_status(solution_id, 100, "Running Test " + str(test))
        is_pass, time_usage, memory_usage, error_code, detail =\
            judge.run_solution(solution_data["language"], solution_data["problem"],
                               test, test_data)
        total_time += time_usage
        if memory_usage > total_memory:
            total_memory = memory_usage
        if "totalTimeLimit" in problem_data and total_time > problem_data["totalTimeLimit"]:
            remote.update_status(solution_id, 402, "Time Limit Exceed on Test " + str(test),
                                 total_time, total_memory)
            return
        if not is_pass:
            if error_code != 402:
                # Only return total time when error is Time Limit Exceed.
                total_time = None
            remote.update_status(solution_id, error_code, detail, total_time, total_memory)
            all_pass = False
            break
    if all_pass:
        remote.update_status(solution_id, 200, "Accepted", total_time, total_memory)
    return True
