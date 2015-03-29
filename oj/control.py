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
    compile_status, compile_error = judge.compile_solution(solution_data["language"], solution_data["code"])
    print(compile_status, compile_error)
    if not compile_status:
        _update_server(400, compile_error)
    default_test = problem_data["default"]
    for test in range(1, problem_data["numberOfTestCases"] + 1):
        # TODO: add special test cases.
        judge.run_solution(solution_data["language"], solution_data["problem"], test, default_test)



def _update_server(result, detail):
    print("Update", result, detail)

tick()
