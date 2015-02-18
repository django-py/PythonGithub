import httplib
from .exceptions import GitHubRequestException


class APIRequest(object):
    """
    Simple request
    """
    def __init__(self):
        self.host = 'api.github.com'

    def get(self, endpoint, params):
        link = httplib.HTTPS(self.host)
        link.putrequest('GET', endpoint)
        link.putheader('HOST', self.host)
        link.putheader('User-Agent', 'PythonGithub Lib')
        link.endheaders()
        status_code, r, httpmessage = link.getreply()
        response = link.getfile().read()
        link.close()

        return response

    def post(self, endpoint, params):
        pass


def get(endpoint, params={}):
    request = APIRequest()
    return request.get(endpoint, params)


def post(endpoint, params={}):
    request = APIRequest()
    return request.post(endpoint, params)
