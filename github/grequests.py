import requests
from .models import GithubModel
from .exceptions import GitHubRequestException


class GithubRequest(object):
    """
    Github Request
    """
    _API_URL = ('https://api.github.com',)

    def __init__(self):
        self._response = {}
        self._endpoint = ''
        self.model = {}

    def _build_url(self, *args, **kwargs):
        args = self._API_URL + args
        values = kwargs.values()

        self._endpoint = '/'.join(args)
        l = len(values)
        self._endpoint += '/' if l == 1 else ''
        self._endpoint += '/'.join(values)

        return self._endpoint

    def request(self, *args, **kwargs):
        """
        call a API github method
        :param action:
        :param kwargs:
        :return:
        """
        url = self._build_url(*args, **kwargs)
        self._response = requests.get(url)
        response = self._response

        if response.status_code == 404:
            raise GitHubRequestException(
                self._endpoint,
                'API invalid github method, http response :',
                response.status_code
            )

        self.model = GithubModel(response)

        model = self.model

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