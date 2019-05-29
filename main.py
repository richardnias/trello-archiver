import requests
import settings
from typing import Dict, List
from urllib.parse import urlencode


StrDict = Dict[str, str]
ListStrDict = List[StrDict]

TRELLO_URL = "https://api.trello.com"


def build_url(path: str, key: str, token: str, qs: StrDict = None) -> str:
    """
    >>> build_url('/1/members', 'abc', '123')
    'https://api.trello.com/1/members?key=abc&token=123'
    >>> build_url('/1/members', 'abc def', '123', {'fields': 'id'})
    'https://api.trello.com/1/members?fields=id&key=abc+def&token=123'
    """
    full_qs = {**(qs if qs else {}), "key": key, "token": token}
    return f"{TRELLO_URL}{path}?{urlencode(full_qs)}"


def get_cards(list_id: str, key: str, token: str) -> ListStrDict:
    url = build_url(f'/1/lists/{list_id}/cards', key, token, qs={'fields': 'id,name'})
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def construct_message(cards: ListStrDict) -> str:
    message_header = 'Your weekly release 🦑:'
    lines = [f'- {card["title"]}' for card in cards]
    message = [message_header, ''] + lines
    return '\n'.join(message)


def send_sms(number: str, message: str):
    pass
