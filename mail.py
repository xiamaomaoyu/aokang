from threading import Thread
from config import app
from flask import render_template
from flask_mail import Mail, Message

mail = Mail(app)


def async_send_mail(app, msg):
    with app.app_context():
        mail.send(msg)


class EmailManager():
    def __init__(self):
        pass

    def send_mail(self, to, subject, template, **kwargs):
        msg = Message(subject, recipients=[to])
        msg.html = render_template(template + '.html', **kwargs)
        thr = Thread(target=async_send_mail, args=[app, msg])
        thr.start()
        return thr
