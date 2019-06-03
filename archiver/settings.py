import os


class ConfigError(Exception):
    pass


def _get_var(var_name) -> str:
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
    def __init__(self, var_name: str):
        self.var_name = var_name
        self.value = None

    def __str__(self):
        if self.value is None:
            self.value = _get_var(self.var_name)
        return self.value


TRELLO_API_KEY = SettingItem("TRELLO_API_KEY")
TRELLO_TOKEN = SettingItem("TRELLO_TOKEN")
TRELLO_DONE_LIST = SettingItem("TRELLO_DONE_LIST")
RECIPIENT = SettingItem("RECIPIENT")
AWS_REGION_NAME = SettingItem("AWS_REGION_NAME")
AWS_ACCESS_KEY_ID = SettingItem("AWS_ACCESS_KEY_ID")
AWS_ACCESS_KEY_SECRET = SettingItem("AWS_ACCESS_KEY_SECRET")
