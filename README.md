# NotifySamples

Samples Twilio Notify programs to create components and send notifications. 

## Program Files

|Program    | Description                                          |
|-----------|------------------------------------------------------|
|[setvars.sh](https://github.com/tigerfarm/NotifySamples/blob/master/setvars.sh) |Shell script set up environment variables.            |
|[echoVars.py](https://github.com/tigerfarm/NotifySamples/blob/master/echoVars.py)|Echo the environment variables to ensure they are set.|
| | |
|[listServices.py](https://github.com/tigerfarm/NotifySamples/blob/master/listServices.py)|List Notify services |
|[createBindings.py](https://github.com/tigerfarm/NotifySamples/blob/master/createBindings.py)|Binding maintenance programs|
|[listBindings.py](https://github.com/tigerfarm/NotifySamples/blob/master/listBindings.py)| |
|[deleteBindings.py](https://github.com/tigerfarm/NotifySamples/blob/master/deleteBindings.py)| |
| | |
|[sendToList1.py](https://github.com/tigerfarm/NotifySamples/blob/master/sendToList1.py)|Send notifications to one SMS phone number |
|[sendToList2.py](https://github.com/tigerfarm/NotifySamples/blob/master/sendToList2.py)|Send notifications to a list of 2 SMS phone number |
|[sendToPaul.py](https://github.com/tigerfarm/NotifySamples/blob/master/sendToPaul.py)|Send a notification to an identity SMS phone number |
|[sendToOne.py](https://github.com/tigerfarm/NotifySamples/blob/master/sendToOne.py)|Send a notification to the tag "one" |
|[sendToOther.py](https://github.com/tigerfarm/NotifySamples/blob/master/sendToOther.py)|Send a notification to the tag "other" |
| | |
|[echoVars.js](https://github.com/tigerfarm/NotifySamples/blob/master/echoVars.js)|Node.js samples
|[listServices.js](https://github.com/tigerfarm/NotifySamples/blob/master/listServices.js)
|[listBindings.js](https://github.com/tigerfarm/NotifySamples/blob/master/listBindings.js)
|[deleteBindings.js](https://github.com/tigerfarm/NotifySamples/blob/master/deleteBindings.js)
|[sendToList.js](https://github.com/tigerfarm/NotifySamples/blob/master/listServices.js)

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
