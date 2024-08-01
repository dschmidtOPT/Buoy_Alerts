import os
from twilio.rest import Client

contacts = {'DS': '+12674811584',
            'AR': '+17322840759'}

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="This is the SWPB-01 Mio contacting reaching out to you, Anthony, using Twilio.  This can be used for alerts or other stuff like that on computer.",
    from_="+18778455679",
    to=contacts['DS'],
)

print(message.body)
