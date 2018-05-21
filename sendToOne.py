print "+++ Send one notification."
import os
import json
from twilio.rest import Client

# Documentation: https://www.twilio.com/notify/api
# Documentation: https://www.twilio.com/docs/notify/api/notifications
# ------------------------------------------------------------------------------

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

yourPhoneNumber = os.environ.get("YOUR_PHONE_NUMBER")
#
print("+ Send notifications to: " + yourPhoneNumber)
notify_service_sid = os.environ.get("NOTIFY_SERVICE_SID")

notification = client.notify.services(notify_service_sid).notifications.create(
    body='Hello One',
    to_binding= json.dumps({"binding_type":"sms", "address": yourPhoneNumber})
  )

print(notification)

# ------------------------------------------------------------------------------
print ""
print "+++ Exit."
