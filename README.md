WaitingRoom
===========

A Python module for using the AlertCaster API

http://developer.alertcaster.com/developer/apiguide

## Usage

`simple(alerts={}, recipients=[])`, runs through everything without you having to deal directly with the other functions.

* `simple(alerts={}, recipients=[])` - Runs through `createAlert`, `triggerAlert`, `deleteAlert`, and `deleteRecipientGroup` to create a custom alert, immediately send it out to recipients, and then clean up after itself.

The other functions of the WaitingRoom module can be used separately if given the correct parameters.

* `createAlert(alerts={}, recipients=[])` - Creates and stores a given alert, but does not deliver it
* `triggerAlert(triggerURL)` - Triggers the alert, sending it out to the recipients
* `deleteAlert(alertID)` - Deletes a stored alert
* `deleteRecipientGroup(groupID)` - Deletes the alert's recipient group

### Sending an SMS alert
```console
$ python
>> import waitingroom
>> wr = waitingroom.WaitingRoom(api_key)
>> alerts={"sms": "Hello World"};
>> recipients=[{"name": {"first": "John", "last": "Doe"}, "mobile": "5551234567"}];
>> wr.simple(alerts, recipients)
```

## Notes
Recipients first and last name need to be set for an alert to successfully be created and sent out
