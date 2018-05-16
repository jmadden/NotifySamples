print "+++ Start echo variables."
import os

# ------------------------------------------------------------------------------
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
print "+ account_sid =", account_sid
print "+ auth_token =", auth_token

notifyServiceSid = os.environ.get("NOTIFY_SERVICE_SID")
print "+ notifyServiceSid =", notifyServiceSid
yourPhoneNumber = os.environ.get("YOUR_PHONE_NUMBER")
print "+ yourPhoneNumber =", yourPhoneNumber

print ""
print "+ The following are required when creating bindings and sending to a list:"
phoneNumber1 = os.environ.get("PHONE_NUMBER_1")
phoneNumber2 = os.environ.get("PHONE_NUMBER_2")
phoneNumber3 = os.environ.get("PHONE_NUMBER_3")
print "+ phoneNumber1 =", phoneNumber1
print "+ phoneNumber2 =", phoneNumber2
print "+ phoneNumber3 =", phoneNumber3

# ------------------------------------------------------------------------------
print ""
print "+++ Exit."

