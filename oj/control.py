from oj import remote, problem, judge


__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


def tick():
    fetched = remote.fetch_solution()
    print(fetched)
    if fetched is None:
        return
    if fetched["status"] != 0:
        return
    solution_data = fetched["data"]
    problem_data = problem.get_problem(solution_data["problem"], solution_data["problem_hash"])
    _update_server(100, "Compiling", None, None)
    compile_status, compile_error = judge.compile_solution(solution_data["language"],
                                                           solution_data["code"])
    print(compile_status, compile_error)
    if not compile_status:
        _update_server(400, compile_error)
    default_test = problem_data["default"]
    total_time = 0
    total_memory = 0
    all_pass = True
    for test in range(1, problem_data["numberOfTestCases"] + 1):
        # TODO: add special test cases.
        _update_server(100, "Running Test " + str(test))
        is_pass, time_usage, memory_usage, error_code, detail =\
            judge.run_solution(solution_data["language"], solution_data["problem"],
                               test, default_test)
        total_time += time_usage
        if memory_usage > total_memory:
            total_memory = memory_usage
        if not is_pass:
            if error_code != 402:
                # Only return total time when error is Time Limit Exceed.
                total_time = None
            _update_server(error_code, detail, total_time, total_memory)
            all_pass = False
            break
    if all_pass:
        _update_server(200, "Accepted", total_time, total_memory)


def _update_server(result, detail, time_usage=None, memory_usage=None):
    print("Update", result, detail, time_usage, memory_usage)

tick()
