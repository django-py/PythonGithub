from .grequests import request
from .api import *


class GithubAPI(object):
    """
    Base Github Object
    """

    users = GithubUserAPI()

    @staticmethod
    def zen():
        _endpoint = 'zen'
        """
        Github Quotes
        :return:
        """
        return request(_endpoint)