print "+++ Echo environment variables."
import os

# ------------------------------------------------------------------------------
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
print "+ ACCOUNT_SID =", account_sid
print "+ AUTH_TOKEN =", auth_token
accountPhoneNumber = os.environ.get("ACCOUNT_PHONE_NUMBER")
print "+ ACCOUNT_PHONE_NUMBER =", accountPhoneNumber

notifyServiceSid = os.environ.get("NOTIFY_SERVICE_SID")
print "+ NOTIFY_SERVICE_SID =", notifyServiceSid
yourPhoneNumber = os.environ.get("YOUR_PHONE_NUMBER")
print "+ YOUR_PHONE_NUMBER =", yourPhoneNumber

print ""
print "+ The following are required when creating bindings:"
phoneNumber1 = os.environ.get("PHONE_NUMBER_1")
phoneNumber2 = os.environ.get("PHONE_NUMBER_2")
phoneNumber3 = os.environ.get("PHONE_NUMBER_3")
print "+ PHONE_NUMBER_1 =", phoneNumber1
print "+ PHONE_NUMBER_2 =", phoneNumber2
print "+ PHONE_NUMBER_3 =", phoneNumber3

# ------------------------------------------------------------------------------
print ""
print "+++ Exit."

