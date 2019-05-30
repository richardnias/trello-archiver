from typing import Dict, List
from urllib.parse import urlencode

import requests

TRELLO_URL = "https://api.trello.com"

StrDict = Dict[str, str]


def build_url(path: str, key: str, token: str, qs: StrDict = None) -> str:
    """
    >>> build_url('/1/members', 'abc', '123')
    'https://api.trello.com/1/members?key=abc&token=123'
    >>> build_url('/1/members', 'abc def', '123', {'fields': 'id'})
    'https://api.trello.com/1/members?fields=id&key=abc+def&token=123'
    """
    full_qs = {**(qs if qs else {}), "key": key, "token": token}
    return f"{TRELLO_URL}{path}?{urlencode(full_qs)}"


ListStrDict = List[StrDict]


def get_cards(list_id: str, key: str, token: str) -> ListStrDict:
    url = build_url(f"/1/lists/{list_id}/cards", key, token, qs={"fields": "id,name"})
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def close_card(card_id: str, key: str, token: str):
    url = build_url(f"/1/cards/{card_id}/closed", key, token, {"value": "true"})
    response = requests.put(url)
    response.raise_for_status()


def close_cards(cards: ListStrDict, key: str, token: str):
    for card in cards:
        # close_card(card["id"], key, token)
        print(f'closing card {card}')


def construct_message(cards: ListStrDict) -> str:
    """
    >>> print(construct_message([{'name': 'woo'}, {'name': 'yeah'}]))
    Your weekly release 🦑:
    <BLANKLINE>
    - woo
    - yeah
    """
    message_header = "Your weekly release 🦑:"
    lines = [f'- {card["name"]}' for card in cards]
    message = [message_header, ""] + lines
    return "\n".join(message)
