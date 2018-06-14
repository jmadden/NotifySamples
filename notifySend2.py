print("+++ Send notifications.")
import os
from twilio.rest import Client

# Use your account SID and auth token from https://twilio.com/console.
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
notify_service_sid = os.environ.get("NOTIFY_SERVICE_SID")
client = Client(account_sid, auth_token)
notification = client.notify.services(notify_service_sid).notifications.create(
    body='Hello one tag.',
    identity="paul"
)
print("+ Notification SID: " + notification.sid)

# ------------------------------------------------------------------------------
print("+++ Exit.")