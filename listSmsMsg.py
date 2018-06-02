print "+++ List incomming SMS messages."
print
import os
import sys
from datetime import date
from twilio.rest import Client
#
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
#
if len(sys.argv) > 1:
    parDate = sys.argv[1];
    print "+ Argument:", parDate; # Example: 2017-02-26
    messages = client.messages.list(date_sent=date(int(parDate[:4]), int(parDate[:7][5:]), int(parDate[:10][8:])));
else:
    messages = client.messages.list();
#
print "++ List received messages (Date/Time/From/To/Text):"
prevMsgDate = messages[0].date_sent.strftime('%Y-%m-%d');
for message in messages:
    curMsgDate = message.date_sent.strftime('%Y-%m-%d');
    if prevMsgDate != curMsgDate:
      print
      prevMsgDate = curMsgDate;
    print "+ " + message.date_sent.strftime('%Y-%m-%d %H:%M:%S') + " " + message.from_ + " " + message.to + " : " + message.body
    # print "+ " + message.date_sent.strftime('%Y-%m-%d %H:%M:%S') + " " + message.to + " " + message.from_ + " : " + message.body + " : " + message.sid
print "+ End of list."

