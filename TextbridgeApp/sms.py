from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


class SendRecTexts:
    account_sid = 'ACeb788af8b4a0ca95b03fd72fef99f208'
    auth_token = '06c29d9d5b21a77984b44d8065285f17'
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