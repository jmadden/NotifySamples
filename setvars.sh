echo "+++ Set variables."

# ------------------------------------------------------------------------------
ACCOUNT_SID=your_account_SID
AUTH_TOKEN=your_account_auth_token
ACCOUNT_PHONE_NUMBER=your_account_phone_number
export ACCOUNT_SID
export AUTH_TOKEN
export ACCOUNT_PHONE_NUMBER

NOTIFY_SERVICE_SID=your_notify_service_sid
export NOTIFY_SERVICE_SID

PHONE_NUMBER_1=your_test_phone_number_1
PHONE_NUMBER_2=your_test_phone_number_2
PHONE_NUMBER_3=your_test_phone_number_3
export PHONE_NUMBER_1
export PHONE_NUMBER_2
export PHONE_NUMBER_3

python echoVars.py

# ------------------------------------------------------------------------------
