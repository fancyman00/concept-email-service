from email.headerregistry import Address
from email.message import EmailMessage

from service.model import Message


def message_constructor(item: Message):
    msg = EmailMessage()
    msg['Subject'] = "Новое обращение"
    msg.set_content("""\
    <html>
      <head></head>
      <body>
        <h2>Новое обращение</h2>
        <div><h4>Имя: </h4>{item.name}</div>
        <div><h4>Телефон: </h4>{item.phone}</div>
        <div><h4>Электронная почта: </h4>{item.email}</div>
        <div><h4>Сообщение: </h4>{item.message}</div>
      </body>
    </html>
    """.format(item=item), subtype='html')
    return msg