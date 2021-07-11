"""Email functionalities,
Using fastapi-mail.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '11/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import BackgroundTasks
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema

# Own Imports
from . import settings

# Mail service configurations
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_ID,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_ID,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    TEMPLATE_FOLDER=settings.MAIL_TEMPLATES_PATH,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)


def send_welcome_email(background_tasks: BackgroundTasks, email_to: str, name: str) -> None:
    """Send welcome email in background.

    Arguments:
    ---------
        background_tasks: Background tasks for sending email.
        mail_to: Recipient's email id.
        name: Recipient's first name.

    Returns:
    ---------
        None
    """
    message = MessageSchema(
        subject='Welcome to CodeSpace',
        recipients=[email_to],
        body={'name': name},
        subtype='html',
    )
    fast_mail = FastMail(conf)
    background_tasks.add_task(fast_mail.send_message, message, template_name='welcome.html')
