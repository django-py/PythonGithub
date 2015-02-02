from . import GithubRequest

__all__ = [
    'zend',
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


def zend(**kwargs):
    """
    Return a random selection from github design philosophies
    :param kwargs:
    :return:
    """
    _method_api = 'zen'
    return request(_method_api, **kwargs)