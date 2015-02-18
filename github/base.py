import request
from .api import *


class GithubAPI(object):
    """
    Base Github Object
    """

    users = User()

    @staticmethod
    def zen():
        _api_method = 'zen'
        """
        Github Quotes
        :return:
        """
        return request.get(_api_method)