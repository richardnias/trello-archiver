import requests
import settings
from typing import Dict
from urllib.parse import urlencode


URL = "https://api.trello.com"


def build_url(path: str, key: str, token: str, qs: Dict[str, str] = None) -> str:
    """
    >>> build_url('/1/members', 'abc', '123')
    'https://api.trello.com/1/members?key=abc&token=123'
    >>> build_url('/1/members', 'abc def', '123', {'fields': 'id'})
    'https://api.trello.com/1/members?fields=id&key=abc+def&token=123'
    """
    full_qs = {**(qs if qs else {}), "key": key, "token": token}
    return f"{URL}{path}?{urlencode(full_qs)}"


