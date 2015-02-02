import pytest
import github

@pytest.fixture
def githubdata():
    return {'status': 200}

@pytest.mark.usefixtures("githubdata")
class TestApi:
    """
    Test Github
    """
    def test_zend_quotes(self, githubdata):
        r = github.zend()