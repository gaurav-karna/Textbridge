from twilio.rest import Client

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from secrets_twilio import *
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

    # @app.route("/sms", methods=['GET', 'POST'])
    # def recTexts(self):
    #     """Respond to incoming calls with a simple text message."""
    #     # Start our TwiML response
    #     resp = MessagingResponse()

    #     # Add a message
    #     resp.message("The Robots are coming! Head for the hills!")
    #     return str(resp)

# if __name__ == "__main__":
obj = SendRecTexts()
    # app.run(debug=True)

# obj.sendTexts("Send this to me","+16476716466")
