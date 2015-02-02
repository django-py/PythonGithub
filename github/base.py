import logging
import collections
import requests
from .exceptions import GitHubRequestException


class GithubModel(object):
    """
    Wrapper Response Model
    """
    __attrs__ = [
        'response',
        'response_code',
        'rate_limit',
        'rate_limit_remaining'
    ]

    def __init__(self, response):
        self.response_code = response.status_code
        self.response = response._content
        self.rate_limit = response.headers['x-ratelimit-limit']
        self.rate_limit_remaining = response.headers['x-ratelimit-remaining']


class GithubRequest(object):
    """
    Github Request
    """
    _API_URL = 'https://api.github.com/'

    def __init__(self):
        self._response = {}
        self._endpoint = ''
        self.model = {}

    def _build_url(self, action):
        self._endpoint = self._API_URL + action
        return self._endpoint

    def request(self, action, **kwargs):
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
