print "+++ Send notifications."
import os
from twilio.rest import Client

# Documentation: https://www.twilio.com/notify/api
# Documentation: https://www.twilio.com/docs/notify/api/notifications
# ------------------------------------------------------------------------------

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

yourPhoneNumber = os.environ.get("YOUR_PHONE_NUMBER")
phoneNumber1 = os.environ.get("PHONE_NUMBER_1")
print("+ Send notifications to: " + yourPhoneNumber + " " + phoneNumber1 )
notify_service_sid = os.environ.get("NOTIFY_SERVICE_SID")
notification = client.notify.services(notify_service_sid).notifications.create(
    body='Hello List',
    to_binding=[
      "{\"binding_type\":\"sms\",\"address\":\"" + yourPhoneNumber +"\"}",
      "{\"binding_type\":\"sms\",\"address\":\"" + phoneNumber1 +"\"}"
    ]
  )

print(notification)

# ------------------------------------------------------------------------------
print ""
print "+++ Exit."
