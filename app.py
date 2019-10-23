# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from flask import Flask, request
from os import getenv


from flask_mail import Mail, Message

app = Flask(__name__)

# Port es 465 para SSL y 587 para TSL

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=getenv("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER=getenv("MAIL_USERNAME")
    )

mail = Mail(app)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = getenv("TWILIO_KEY")
auth_token = getenv("TWILIO_AUTH")
origin_phone = getenv("TWILIO_PHONE_NUMBER")

# print(account_sid, auth_token)

client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/send', methods=["GET", "POST"])
def sendMail():
    email = request.args.get('email')
    token = request.args.get('body')

    msg = Message("Hello",
                  recipients=[email])
    msg.body(body)
    mail.send(msg)
    return f"Sending to {email}..."

@app.route('/sms/<string:target>/')
def sms(target):
    # try:
    #     message = client.messages.create(
    #                                 body='Hello there!',
    #                                 # from_=f'+14155238886',
    #                                 from_=f'{origin_phone}',
    #                                 to='+56976677688'
    #                             )
    #     print(message)
    # except Exception as err:
    #     print(err)
    return "Nos Supported Yet"