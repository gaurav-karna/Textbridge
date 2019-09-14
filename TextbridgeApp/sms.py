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

    @app.route("/sms", methods=['POST'])
    def sms_reply():
        """Respond to incoming calls with a simple text message."""

        # Use this data in your application logic
        from_number = request.form['From']
        to_number = request.form['To']
        body = request.form['Body']

        # Start our TwiML response
        resp = MessagingResponse()

        # Add a message
        resp.message("The Robots are coming! Head for the hills!")

        return str(resp)
obj = SendRecTexts()
# obj.sendTexts("Send this to me","+16476716466")