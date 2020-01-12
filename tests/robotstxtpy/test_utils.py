import robotstxtpy.utils as utils


def test_validate_url(mocker, example_valid_url, example_invalid_url):
    mocker.patch.object(utils, '__is_reachable_url',
                        return_value=True)
    assert utils.validate_url(example_valid_url)
    assert not utils.validate_url(example_invalid_url)

    # url is valid but not reachable
    mocker.patch.object(utils, '__is_reachable_url',
                        return_value=False)
    assert not utils.validate_url(example_valid_url)


def test_filter_out_path_from_url():
    assert 'google.ca' == utils.filter_out_path_from_url('https://google.ca')
    assert 'random/stuff.com' == utils.filter_out_path_from_url(
        'http://www.random/stuff.com')
    assert 'op.gg' == utils.filter_out_path_from_url('www.op.gg')
