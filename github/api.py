import json
import request
from .models import GithubUserModel


class User(object):
    """
    Github User
    """
    _api_method = 'users'

    def get(self, *args, **kwargs):
        """
        :param github_username:
        :return:
        """
        content = request.get(self._api_method, **kwargs)

        return GithubUserModel(content)