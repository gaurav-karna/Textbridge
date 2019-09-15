from twilio.rest import Client

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from Textbridge.secrets import *
app = Flask(__name__)


class SendRecTexts:
    account_sid = twilio_account_sid
    auth_token = twilio_auth_token
    def sendTexts(self,content,to_):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
                        .create(
                            body=content,
                            from_='+16476942333',
                            to=to_
                        )

        print(message.sid)

obj = SendRecTexts()
# obj.sendTexts("Send this to me","+16476716466")
