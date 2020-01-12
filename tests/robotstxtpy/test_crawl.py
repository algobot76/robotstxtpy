import unittest
from unittest import mock

from bs4 import BeautifulSoup
from mock import patch
from robotstxtpy.crawler import Crawler


class request:
    text = ''

    def __init__(self, text):
        self.text = text


class link:
    attrs = {}

    def __init__(self, attrs):
        self.attrs = attrs


class crawlerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_crawler = Crawler('http://random.cc')

    def test_retrieve(self) -> None:
        empty_list = set()
        assert empty_list == self.test_crawler.get_endpoints_from_url()

    @mock.patch('requests.get')
    def test_requested_url(self, mocked_requests_get) -> None:
        response = request('random things')
        mocked_requests_get.return_value = response
        returned_urls = self.test_crawler.get_endpoints_from_url()
        assert returned_urls == set()

    @patch.object(BeautifulSoup, 'find_all')
    def test_urls_were_gotten(self, mocked_soup_find) -> None:
        link1 = link({'href': '/randomstuff'})
        link2 = link({'href': '/morerandomstuff'})
        link_list = [link1, link2]
        mocked_soup_find.return_value = link_list
        assert self.test_crawler.get_endpoints_from_url() == set([
            'http://random.cc/morerandomstuff', 'http://random.cc/randomstuff'
        ])
