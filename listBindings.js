// -----------------------------------------------------------------------------
console.log("+++ List bindings.");

const accountSid = process.env.ACCOUNT_SID;
const authToken = process.env.AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

const notifyServiceSid = process.env.NOTIFY_SERVICE_SID;
client.notify.services(notifyServiceSid)
        .bindings
        .each({startDate: new Date(Date.UTC(2017, 4, 26))},
                bindings => {
                    console.log("+ " + bindings.sid + " " + bindings.tags + " " + bindings.identity + " " + bindings.bindingType + " " + bindings.address);
                }
        );

// {tag: 'one'}
// startDate: new Date(Date.UTC(2017, 4, 26))
// 
// -----------------------------------------------------------------------------
