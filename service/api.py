from service.controller import EmailController

from service.model import Message
from tools.decorators import error_wrapper


class EmailApi:
    def __init__(self, app, controller: EmailController):
        self.app = app
        self.service = controller

        @self.app.get("/")
        def read_root():
            return {"Hello": "World"}

        @self.app.put("/send")
        @error_wrapper
        def send_mail(data: Message):
            print("Send email to: " + data.email)
            controller.send_message_email(data)