from twilio.rest import Client

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import secrets
app = Flask(__name__)
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


class SendRecTexts:
    account_sid = secrets.twilio_account_sid
    auth_token = secrets.twilio_auth_token
    def sendTexts(self,content,to_):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
                        .create(
                            body=content,
                            from_='+16476942333',
                            to=to_
                        )

        print(message.sid)
    def RecText(self)
obj = SendRecTexts()
# obj.sendTexts("Send this to me","+16476716466")