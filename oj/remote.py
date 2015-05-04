import os
import shutil
import json
from urllib2 import urlopen, HTTPError, URLError, Request
import zipfile
from config import CONFIG

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


base_url = CONFIG["server"] + "/api/judge/"

judge_auth = "?judge=1&secret=JUDGE_SECRET"


def fetch_solution():
    supported_languages = [10, 20]
    language_url = "&language=".join([""] + [str(l) for l in supported_languages])
    fetch_url = base_url + "solution" + judge_auth + language_url
    return _fetch_json(fetch_url)


def fetch_problem(problem_id):
    resource_url = base_url + "problem/" + str(problem_id) + "/package.zip" + judge_auth
    local_path = "../problems/" + str(problem_id)
    local_path = os.path.join(os.path.dirname(__file__), local_path)
    local_path = os.path.abspath(local_path)
    zip_file = local_path + ".zip"
    print(local_path)
    _download_zip(resource_url, zip_file)
    _unzip(zip_file, local_path)
    os.remove(zip_file)


def _fetch_json(url, data=None):
    result = None
    try:
        request = Request(url, data, {
            "Content-type": "application/json"
        })
        response = urlopen(request)
        data = response.read()
        result = json.loads(data)
    # handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url
    return result


def _download_zip(url, local_path):
    try:
        f = urlopen(url)
        print "downloading " + url
        dir = os.path.dirname(local_path)
        print("dir ", dir)
        if not os.path.exists(dir):
            os.mkdir(dir)
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
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
        os.mkdir(target_path)
    else:
        os.mkdir(target_path)
    for name in zip_file.namelist():
        zip_file.extract(name, target_path)


def update_status(solution_id, result, detail, time_usage=None, memory_usage=None):
    update_package = {
        "result": result,
        "detail": detail,
        "time": time_usage,
        "memory": memory_usage
    }
    print(json.dumps(update_package))
    update_url = base_url + "solution/" + str(solution_id) + "/update" + judge_auth
    request = Request(update_url)
    request.add_header('Content-Type', 'application/json')
    response = urlopen(request, data=json.dumps(update_package))
    data = response.read()
    print(data)
