# NotifySamples

Samples Twilio Notify programs to create components and send notifications. 

## Program Files

|Program    | Description                                          |
|-----------|------------------------------------------------------|
|setvars.sh |Shell script to environment variables.                |
|echoVars.py|Echo the environment variables to ensure they are set.|
| | |
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

In the shell script, setvars.sh, replace the your_account_* with your account values.
And replace the your_phone_number with your mobile phone number.
After creating your Notify service, add an environment variable for it.

When using the sendToList.py program, you also require the following variables.
In setvars.sh, replace the your_test_phone_number_* with your test phone numbers. I use Twilio phone number for testing.

Then run setvars.sh from command line:

    $ source setvars.sh
    ...

Cheers...
