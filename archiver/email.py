import boto3
from . import settings


def _ses_get_client():
    return boto3.client(
        "ses",
        region_name=settings.AWS_REGION_NAME.value,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID.value,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY.value,
    )


def _ses_send_email(recipient, sender, subject, message):
    client = _ses_get_client()
    client.send_email(
        Destination={"ToAddresses": [recipient]},
        Message={
            "Body": {"Text": {"Charset": "UTF-8", "Data": message}},
            "Subject": {"Charset": "UTF-8", "Data": subject},
        },
        Source=sender,
    )


def send_email(recipient, sender, subject, message):
    print(f"sending mail to {recipient}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")
    _ses_send_email(recipient, sender, subject, message)
