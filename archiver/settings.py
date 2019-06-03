import os
from typing import Optional


class ConfigError(Exception):
    pass


def _get_var(var_name: str) -> str:
    """
    >>> os.environ['foo'] = 'woo'
    >>> _get_var('foo')
    'woo'
    >>> _get_var('boo')
    Traceback (most recent call last):
    ...
    settings.ConfigError:
    """
    try:
        return os.environ[var_name]
    except KeyError:
        raise ConfigError(f"Misconfigured! {var_name} is not set.")


class SettingItem:
    """
    >>> os.environ['foo'] = 'woo'
    >>> item = SettingItem('foo')
    >>> print(item)
    woo
    >>> item.value
    'woo'
    >>> f'{item}'
    'woo'
    """

    def __init__(self, var_name: str):
        self.var_name = var_name
        self._value: Optional[str] = None

    @property
    def value(self) -> str:
        if self._value is None:
            self._value = _get_var(self.var_name)
        return self._value

    def __str__(self) -> str:
        return self.value


TRELLO_API_KEY = SettingItem("TRELLO_API_KEY")
TRELLO_TOKEN = SettingItem("TRELLO_TOKEN")
TRELLO_DONE_LIST = SettingItem("TRELLO_DONE_LIST")
RECIPIENT = SettingItem("RECIPIENT")
SENDER = SettingItem("SENDER")
AWS_REGION_NAME = SettingItem("AWS_REGION_NAME")
AWS_ACCESS_KEY_ID = SettingItem("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = SettingItem("AWS_SECRET_ACCESS_KEY")
