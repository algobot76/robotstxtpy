from bs4 import BeautifulSoup 
import tests.utils as test_utils
from unittest import mock
from robotstxtpy.crawler import get_endpoints_from_url
import json
from mock import patch, Mock

class request:
    text = ""

    def __init__(self, text):
        self.text = text

class link:
    attrs = {}
    def __init__(self, attrs):
        self.attrs = attrs

def test_retrieve():
    empty_list = set()
    assert empty_list == get_endpoints_from_url("")   

@mock.patch('requests.get')
def test_requested_url(mocked_requests_get):
    response = request("random things")
    mocked_requests_get.return_value = response
    test_url = "http://random.gov"
    returned_urls = get_endpoints_from_url(test_url)
    assert returned_urls == set()

@patch.object(BeautifulSoup, 'find_all')
def test_urls_were_gotten(mocked_soup_find):
    test_url = "http://random.cc"
    link1 = link({'href': "/randomstuff"})
    link2 = link({'href': '/morerandomstuff'})
    link_list = [link1, link2]
    mocked_soup_find.return_value = link_list
    assert get_endpoints_from_url(test_url) == set([
        "http://random.cc/morerandomstuff", "http://random.cc/randomstuff"
    ])
    