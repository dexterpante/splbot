import requests
from unittest.mock import Mock, patch

from src.bot import actions


@patch('src.bot.actions.http.post')
def test_queue_battle_success(mock_post):
    response = Mock()
    response.json.return_value = {'status': 'success'}
    response.raise_for_status = Mock()
    mock_post.return_value = response

    assert actions.queue_battle({'foo': 'bar'}) is True
    mock_post.assert_called_once()


@patch('src.bot.actions.http.post')
def test_queue_battle_http_error(mock_post):
    mock_post.side_effect = requests.exceptions.HTTPError('fail')

    assert actions.queue_battle({'foo': 'bar'}) is False


@patch('src.bot.actions.http.post')
def test_submit_team_success(mock_post):
    response = Mock()
    response.json.return_value = {'status': 'success'}
    response.raise_for_status = Mock()
    mock_post.return_value = response

    assert actions.submit_team({'foo': 'bar'}) is True


@patch('src.bot.actions.http.post')
def test_claim_rewards_failure(mock_post):
    response = Mock()
    response.json.return_value = {'status': 'error'}
    response.raise_for_status = Mock()
    mock_post.return_value = response

    assert actions.claim_rewards({'foo': 'bar'}) is False


@patch('src.bot.actions.http.post')
def test_submit_team_http_error(mock_post):
    mock_post.side_effect = requests.exceptions.Timeout('oops')
    assert actions.submit_team({'foo': 'bar'}) is False


@patch('src.bot.actions.http.post')
def test_claim_rewards_success(mock_post):
    response = Mock()
    response.json.return_value = {'status': 'success'}
    response.raise_for_status = Mock()
    mock_post.return_value = response
    assert actions.claim_rewards({'foo': 'bar'}) is True
