from .grequests import request


class GithubUser(object):
    """
    Github User
    """
    _endpoint = 'users'

    def get(self, *args, **kwargs):
        """
        :param github_username:
        :return:
        """
        return request(self._endpoint, *args, **kwargs)


class Github(object):
    """
    Base Github Object
    """
    users = GithubUser()

    @staticmethod
    def zen():
        _endpoint = 'zen'
        """
        Github Quotes
        :return:
        """
        return request(_endpoint)