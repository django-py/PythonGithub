import json
from .grequests import request
from .models import GithubUserModel


class GithubUserAPI(object):
    """
    Github User
    """
    _endpoint = 'users'

    def _get(self, *args, **kwargs):
        return request(self._endpoint, *args, **kwargs)

    def get(self, *args, **kwargs):
        """
        :param github_username:
        :return:
        """
        content = self._get(*args, **kwargs)

        return GithubUserModel(content)