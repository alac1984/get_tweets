import pytest
from unittest.mock import patch
from config import Config


@pytest.fixture
def envs_prod(monkeypatch):
    monkeypatch.setenv("ENVIRON_BASH", "True")
    monkeypatch.setenv("DB_USER", "prod_user")
    monkeypatch.setenv("DB_PASSWORD", "prod_pass")
    monkeypatch.setenv("DB_HOST", "prod_host")
    monkeypatch.setenv("DB_PORT", "prod_1234")
    monkeypatch.setenv("DB_DB", "prod_db")
    monkeypatch.setenv("TWITTER_TOKEN", "prod_abuble")


def test_config_prod(envs_prod):
    config = Config()

    assert config.DB_USER == "prod_user"


@patch("config.config.dotenv_values")
def test_config_devel(mock_dotenv):
    mock_dotenv.return_value = {
        "DB_USER": "dev_user",
        "DB_PASSWORD": "dev_pass",
        "DB_HOST": "dev_host",
        "DB_PORT": "dev_1234",
        "DB_DB": "dev_db",
        "TWITTER_TOKEN": "dev_abuble",
    }
    config = Config()

    assert config.DB_USER == "dev_user"
