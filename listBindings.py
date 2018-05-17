print "+++ List Bindings (SID, tag, identity, type, address:phone number)."
import os
from twilio.rest import Client
from datetime import date
# Documentation: https://www.twilio.com/docs/notify/api/bindings
# ------------------------------------------------------------------------------

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

notifyServiceSid = os.environ.get("NOTIFY_SERVICE_SID")
# .list(start_date=date(2015, 8, 25), tag="new user")
bindings = client.notify.services(notifyServiceSid).bindings \
    .list(start_date=date(2015, 8, 25))

for binding in bindings:
    print("+ " + binding.sid + " " + binding.tags[0] + " " + binding.identity + " " + binding.binding_type + " " + binding.address)

# ------------------------------------------------------------------------------
print "+++ Exit."