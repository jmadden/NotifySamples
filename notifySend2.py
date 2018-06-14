print("+++ Send notifications.")
import os
import json
from twilio.rest import Client

# Use your account SID and auth token from https://twilio.com/console.
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
# Use your Notification service SID.
notify_service_sid = os.environ.get("NOTIFY_SERVICE_SID")
# A phone number to send to.
phoneNumber1 = os.environ.get("PHONE_NUMBER_1")
phoneNumber2 = os.environ.get("PHONE_NUMBER_2")
phoneNumber3 = os.environ.get("PHONE_NUMBER_3")

client = Client(account_sid, auth_token)
notification = client.notify.services(notify_service_sid).notifications.create(
    body='Hello Paul',
    identity="paul"
)
print("+ Notification SID: " + notification.sid)

# ------------------------------------------------------------------------------
print("+++ Exit.")