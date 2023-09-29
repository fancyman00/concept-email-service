from email.mime.multipart import MIMEMultipart

from service.model import Message
from smtp.email import EmailService
from tools.email_constructor import message_constructor


class EmailController:
    def __init__(self, service: EmailService, from_email: str, to_email: str):
        self.__service = service
        self.__sender_email = from_email
        self.__receiver_email = to_email

    def send_message_email(self, item: Message):
        msg = message_constructor(item)
        self.__service.send_email(self.__sender_email, self.__receiver_email, msg.as_string())
