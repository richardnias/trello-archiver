from archiver.email import send_email
from archiver.trello import get_cards, close_cards, construct_message
from archiver import settings
from datetime import datetime


def main():
    key = settings.TRELLO_API_KEY
    token = settings.TRELLO_TOKEN
    list_id = settings.TRELLO_DONE_LIST
    recipient = settings.RECIPIENT.value

    cards = get_cards(list_id, key, token)

    message = construct_message(cards)

    send_email(
        recipient, f'[weekly release] {datetime.today().strftime("%d.%m.%y")}', message
    )

    close_cards(cards, key, token)


if __name__ == "__main__":
    main()
