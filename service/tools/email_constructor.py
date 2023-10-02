from email.headerregistry import Address
from email.message import EmailMessage

from service.model import Message, Order


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


def order_constructor(item: Order):
    msg = EmailMessage()
    msg['Subject'] = "Новый заказ"
    products = ''
    for product in item.products:
        reformat = 'Модель: ' + product.productId + " Количество: " + str(product.productCount) + "<br/>"
        products += reformat

    msg.set_content("""\
    <html>
      <head></head>
      <body>
        <h2>Новый заказ</h2>
        <h4>Имя: {item.name}</h4>
        <h4>Фамилия: {item.surname}</h4>
        <h4>Телефон: {item.phone}</h4>
        <h4>Электронная почта: {item.mail}</h4>
        <h4>Заказ: <h5>{products}</h5></h4>
      </body>
    </html>
    """.format(item=item, products=products), subtype='html')
    return msg
