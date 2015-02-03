import json
import logging
import collections
import requests
from .exceptions import GitHubRequestException


class GithubModel(object):
    """
    Wrapper Response Model
    """
    __attrs__ = [
        'objects',
        'response_code',
        'rate_limit',
        'rate_limit_remaining'
    ]

    def __init__(self, response):
        self.response_code = response.status_code

        #- namedtuplesss
        print response.__dict__
        print response._content.__dict__

        rp = json.dumps([response._content])


        obj = collections.namedtuple('Objects', rp.keys())
        self.objects = obj

        self.rate_limit = response.headers['x-ratelimit-limit']
        self.rate_limit_remaining = response.headers['x-ratelimit-remaining']

        print self.objects


class GithubRequest(object):
    """
    Github Request
    """
    _API_URL = 'https://api.github.com/'

    def __init__(self):
        self._response = {}
        self._endpoint = ''
        self.model = {}

    def _build_url(self, *args, **kwargs):
        print args
        print kwargs

        args = list[args]

        self._endpoint = self._API_URL.join(args)

        return self._endpoint

    def request(self, action, *args, **kwargs):
        """
        call a API github method
        :param action:
        :param kwargs:
        :return:
        """
        url = self._build_url(action)
        self._response = requests.get(url)
        response = self._response

        self.model = GithubModel(response)

        model = self.model

        if model.response_code == 404:
            raise GitHubRequestException(
                self._endpoint,
                'API invalid github method, http response :',
                model.response_code
            )

        return model


def request(*args, **kwargs):
    """
    Request buil method
    :param action:
    :param kwargs:
    :return:
    """
    gr = GithubRequest()

    return gr.request(*args, **kwargs)


class GithubUser(object):
    """
    Github User Model
    """
    _endpoint = 'users'

    def get(self, *args, **kwargs):
        """
        :param github_username:
        :return:
        """
        return request(self._endpoint, *args, **kwargs)


class Github(object):
    users = GithubUser()