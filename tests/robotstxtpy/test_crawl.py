import tests.utils as test_utils
from unittest.mock import MagicMock
from robotstxtpy.crawler import get_endpoints_from_url

def test_retrieve():
    empty_list = set()
    assert empty_list == get_endpoints_from_url("")

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse("<h1>Stuff</h1>", 200)

@mock.patch('requests.get', side_effect=mocked_requests_get)
def test_requested_url():
    test_url = "http://random.gov"
    expected_urls = set([test_url])
    assert expected_urls == get_endpoints_from_url(test_url)