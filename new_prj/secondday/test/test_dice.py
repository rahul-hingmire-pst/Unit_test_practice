
from unittest import mock

import pytest
import secondday.app.dice
from secondday.app.dice import guess_number,get_ip


@mock.patch("secondday.app.dice.rolldice")
def test_guess_number(mock_roll_dice):
    mock_roll_dice.return_value = 3
    assert guess_number(3) == "You Won the match"


@mock.patch("secondday.app.dice.requests.get")   
def test_getip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response",**{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}}) 
    result = get_ip()
    assert result == "0.0.0.0"

