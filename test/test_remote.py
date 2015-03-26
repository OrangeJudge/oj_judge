import unittest

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


class TestRemote(unittest.TestCase):

    def setUp(self):
        pass

    def test_download_zip(self):
        from oj import remote
        remote.fetch_problem(1)
        remote.fetch_problem(2)