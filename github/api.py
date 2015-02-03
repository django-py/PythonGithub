from . import GithubRequest

__all__ = [
    'zen',
    'users',
]


def request(action, **kwargs):
    """
    Request buil method
    :param action:
    :param kwargs:
    :return:
    """
    gr = GithubRequest()

    return gr.request(action, **kwargs)


def zen(**kwargs):
    """
    Return a random selection from github design philosophies
    :param kwargs:
    :return:
    """
    _method_api = 'zen'
    return request(_method_api, **kwargs)


def users(**kwargs):
    """
    Return information a specific username
    :param username:
    :return:
    """
    _method_api = 'users'
    return request(_method_api, **kwargs)
