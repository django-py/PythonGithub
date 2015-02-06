import pytest
from github import api

@pytest.fixture
def githubdata():
    return {'status': 200}

@pytest.mark.usefixtures("githubdata")
class TestApi:
    """
    Test Github
    """
    def test_zen_quotes(self):
        """
        Test api.zen() method
        """
        r = api.zen()
        assert len(r) > 1

    def test_get_users_info(self):
        """
        Test get user info.
        api.users.get(username=nicchub)
        """
        user = api.users.get(username='nicchub')
        assert user.login == "nicchub"
        assert user.url == "https://api.github.com/users/nicchub"
        assert user.type == "User"
        assert user.created_at == "2014-11-27T10:14:53Z"
        assert user.received_events_url == "https://api.github.com/users/nicchub/received_events"