import os
import pytest
from config import Config
from unittest import mock


@pytest.fixture
def envs_devel(monkeypatch):
    monkeypatch.setenv("GET_TWEETS", "True")
    monkeypatch.setenv("DB_USER", "dev_user")
    monkeypatch.setenv("DB_PASSWORD", "dev_pass")
    monkeypatch.setenv("DB_HOST", "dev_host")
    monkeypatch.setenv("DB_PORT", "dev_1234")
    monkeypatch.setenv("DB_DB", "dev_db")
    monkeypatch.setenv("TWITTER_TOKEN", "dev_abuble")


@pytest.fixture
def envs_prod(monkeypatch):
    monkeypatch.setenv("GET_TWEETS", "True")
    monkeypatch.setenv("APP_STATE", "prod")
    monkeypatch.setenv("DB_USER", "prod_user")
    monkeypatch.setenv("DB_PASSWORD", "prod_pass")
    monkeypatch.setenv("DB_HOST", "prod_host")
    monkeypatch.setenv("DB_PORT", "prod_1234")
    monkeypatch.setenv("DB_DB", "prod_db")
    monkeypatch.setenv("TWITTER_TOKEN", "prod_abuble")


def test_config_prod(envs_prod):
    config = Config()

    assert config.DB_USER == "prod_user"


def test_config_devel(envs_devel):
    config = Config()

    assert config.DB_USER == "dev_user"
