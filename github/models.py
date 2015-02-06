from abc import ABCMeta, abstractmethod

__all__ = ['GithubUserModel',]


class GithubAbstractModel:
    """
    Model Descriptor
    """
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        for dct in args:
            for key in dct:
                setattr(self, key, dct[key])

        for key in kwargs:
            setattr(self, key, kwargs[key])


class GithubUserModel(GithubAbstractModel):
    """
    Github User
    """
    pass