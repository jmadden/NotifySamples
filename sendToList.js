// -----------------------------------------------------------------------------
console.log("+++ Start sending notifications to a list.");

const accountSid = process.env.ACCOUNT_SID;
const authToken = process.env.ACCOUNT_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

const notifyServiceSid = process.env.NOTIFY_SERVICE_SID;
const phoneNumber1 = process.env.PHONE_NUMBER_1;
const phoneNumber2 = process.env.PHONE_NUMBER_2;
// Single:   toBinding: JSON.stringify({"binding_type": "sms", "address": yourPhoneNumber})
client.notify.services(notifyServiceSid).notifications.create({
    body: 'Hello there from Notify.',
    toBinding: [
        JSON.stringify({"binding_type": "sms", "address": phoneNumber1}),
        JSON.stringify({"binding_type": "sms", "address": phoneNumber2})
    ]
}).then(notification => console.log(notification.sid))
        .catch(error => console.log(error));
