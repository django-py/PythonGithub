from collections import namedtuple
from .exceptions import GithubDecodeError


class GithubModel(object):
    """
    Wrapper Response Model
    """
    __attrs__ = [
        'objects',
        'rate_limit',
        'rate_limit_remaining'
    ]

    def __init__(self, response):
        self.rate_limit = response.headers['x-ratelimit-limit']
        self.rate_limit_remaining = response.headers['x-ratelimit-remaining']

        #todo bad design
        try:
            objects = response.json()
            self.objects = namedtuple('Data', objects.keys())._make(objects.values())
        except:
            self.objects = namedtuple('Data', 'content')._make([response._content,])