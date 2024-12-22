import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected",
                         [
                             (100, 10, "Buy more cryptocurrency"),
                             (100, 90, "Sell all your cryptocurrency"),
                             (100, 102, "Do nothing")
                         ])
@patch("app.maim.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_prediction: MagicMock,
                               current_rate: float,
                               predicted_rate: float,
                               expected: str) -> None:
    mock_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
