import pytest

import tests.utils as test_utils
from robotstxtpy import RobotsTxt
from robotstxtpy import RobotsTxtException


def test_robotstxt():
    foo = RobotsTxt()
    assert foo.content == dict()

    foo.add_user_agent("Chrome")
    assert foo.content == {'Chrome': []}

    foo.add_endpoint('Chrome', 'Allow', '/foo')
    assert foo.content == {'Chrome': [('Allow', '/foo')]}

    with pytest.raises(RobotsTxtException):
        foo.add_endpoint('FireFox', 'Disallow', '/bar')
    foo.add_user_agent('FireFox')

    foo.add_endpoint('FireFox', 'Disallow', '/bar')
    assert foo.content == {'Chrome': [('Allow', '/foo')],
                           'FireFox': [('Disallow', '/bar')]}

    test_utils.assert_same_elements_in_lists(foo.user_agents(),
                                             ['Chrome', 'FireFox'])
    test_utils.assert_same_elements_in_lists(foo.rules(),
                                             [('Allow', '/foo'),
                                              ('Disallow', '/bar')])
    test_utils.assert_same_elements_in_lists(
        foo.rules(user_agent='Chrome'),
        [('Allow', '/foo')])
