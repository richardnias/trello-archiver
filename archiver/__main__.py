from archiver.lib import get_cards, construct_message, send_sms, close_cards
from archiver import settings


def main():
    key = settings.TRELLO_API_KEY
    token = settings.TRELLO_TOKEN
    list_id = settings.TRELLO_DONE_LIST
    number = settings.PHONE_NUMBER

    cards = get_cards(list_id, key, token)

    message = construct_message(cards)

    send_sms(number, message)

    close_cards(cards, key, token)


if __name__ == "__main__":
    main()
