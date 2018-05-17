# NotifySamples

Samples Twilio Notify programs to create components and send notifications. 

## Program Files

|Program    | Description                                          |
|-----------|------------------------------------------------------|
|echoVars.py|Echo the environment variables to ensure they are set.|
|listServices.py|List Notify services |
|createBindings.py|Binding maintenance programs|
|listBindings.py| |
|deleteBindings.py| |
|sendToOne.py|Send a notification to a single SMS phone number |
|sendToList.py|Send notifications to a list of SMS phone number |
| | |
|echoVars.js|Node.js samples
|listServices.js
|listBindings.js
|deleteBindings.js
|sendToList.js

## Environment Variable Setup

In the following, replace the your_account_* with your account values.
And replace the your_phone_number with your mobile phone number.
Then run from command line:

    ACCOUNT_SID=your_account_SID
    AUTH_TOKEN=your_auth_token
    YOUR_PHONE_NUMBER=your_phone_number
    export ACCOUNT_SID
    export AUTH_TOKEN
    export YOUR_PHONE_NUMBER

When using the sendToList.py program, you also require the following variables.
Replace the your_test_phone_number_* with your test phone numbers. I use Twilio phone number for testing.

    PHONE_NUMBER_1=your_test_phone_number_1
    PHONE_NUMBER_2=your_test_phone_number_2
    PHONE_NUMBER_3=your_test_phone_number_3
    export PHONE_NUMBER_1
    export PHONE_NUMBER_2
    export PHONE_NUMBER_3

After creating your Notify service, add an environment variable for it.

    NOTIFY_SERVICE_SID=your_notify_service_SID
    export NOTIFY_SERVICE_SID

To confirm that the variables are set properly, run the *echoVars.py* program.

    $ python echoVars.py
    +++ Start echo variables.
    + account_sid = your_account_SID
    + auth_token = your_auth_token
    + notifyServiceSid = your_notify_service_SID
    + yourPhoneNumber = your_phone_number

    + The following are required when creating bindings and sending to a list:
    + phoneNumber1 = your_test_phone_number_1
    + phoneNumber2 = your_test_phone_number_2
    + phoneNumber3 = your_test_phone_number_3

    +++ Exit.

Cheers...
