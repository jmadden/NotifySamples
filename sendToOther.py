print "+++ Send to a tag list."
import os
from twilio.rest import Client

# Documentation: https://www.twilio.com/notify/api
# Documentation: https://www.twilio.com/docs/notify/api/notifications
# ------------------------------------------------------------------------------

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

theTag = "other";
print("+ Send notifications to: " + theTag)
notify_service_sid = os.environ.get("NOTIFY_SERVICE_SID")
notification = client.notify.services(notify_service_sid).notifications.create(
    body='Hello all others',
    tag=theTag
  )

print(notification)

# ------------------------------------------------------------------------------
print ""
print "+++ Exit."
