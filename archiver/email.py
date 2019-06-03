import boto3
from . import settings


def _ses_get_client():
    return boto3.client(
        'ses',
        region_name=settings.AWS_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_access_key_secret=settings.AWS_ACCESS_KEY_SECRET,
    )


def _ses_send_email(recipient, subject, message):
    client = _ses_get_client()
    client.send_email(
        Destination={
            'ToAddresses': [recipient],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source='richardnias@gmail.com',
    )


def send_email(recipient, subject, message):
    print(f'sending mail to {recipient}')
    print(f'Subject: {subject}')
    print(f'Message: {message}')
    _ses_send_email(recipient, subject, message)
