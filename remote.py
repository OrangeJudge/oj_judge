import os
from urllib2 import urlopen, HTTPError, URLError
import zipfile

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


base_url = "http://localhost:9000/judge/"


def fetch_solution():
    pass


def fetch_problem(problem_id):
    resource_url = base_url + "problem/" + str(problem_id) + "/package.zip?secret=JUDGE_SECRET"
    local_path = "problems/" + str(problem_id) + ".zip"
    _download_zip(resource_url, local_path)
    _unzip(local_path, "problems/" + str(problem_id))
    os.remove(local_path)


def _download_zip(url, local_path):
    try:
        f = urlopen(url, data="")
        print "downloading " + url

        # Open our local file for writing
        with open(local_path, "wb") as local_file:
            local_file.write(f.read())

    # handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


def _unzip(local_path, target_path):
    zip_file = zipfile.ZipFile(local_path)
    for name in zip_file.namelist():
        zip_file.extract(name, target_path)


if __name__ == "__main__":
    fetch_problem(1)
