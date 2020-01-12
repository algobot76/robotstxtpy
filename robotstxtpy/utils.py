import re
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import urlopen


def __is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except ValueError:
        return False


def __is_reachable_url(url):
    try:
        urlopen(url)
        return True
    except URLError:
        return False


def validate_url(url):
    return __is_valid_url(url) and __is_reachable_url(url)

# removes https or http from URL string
# also removes www if it exists in url string


def filter_out_path_from_url(link) -> str:
    if(link.startswith('www')):
        return link.replace('www.', '')
    url = re.compile(r'https?://(www\.)?')
    new_url = url.sub('', link).strip().strip('/')
    return new_url
