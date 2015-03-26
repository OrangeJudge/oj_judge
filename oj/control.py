from oj import remote


__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


def tick():
    fetched = remote.fetch_solution()
    if fetched is None:
        return
    if fetched["status"] != 0:
        return
    print(fetched)

tick()
