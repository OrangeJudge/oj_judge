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

tick()
