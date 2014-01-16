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
>> alerts={"sms": "Hello World"}
>> recipients=[{"name": {"first": "John", "last": "Doe"}, "mobile": "5551234567"}]
>> wr.simple(alerts, recipients)
```

### Sending an email alert
```console
$ python
>> import waitingroom
>> wr = waitingroom.WaitingRoom(api_key)
>> alerts={"email": {"subject": "Some Subject Here", "body": "<strong>Hello World</strong><p>This is a test...</p>"}}
>> recipients=[{"name": {"first": "John", "last": "Doe"}, "email": "john@example.com"}]
>> wr.simple(alerts, recipients)
```

### Sending a phone message alert
```console
$ python
>> import waitingroom
>> wr = waitingroom.WaitingRoom(api_key)
>> alerts={"audio": 79}
>> recipients=[{"name": {"first": "John", "last": "Doe"}, "mobile": "5551234567"}]
>> wr.simple(alerts, recipients)
```

### Sending multiple alerts
```console
$ python
>> import waitingroom
>> wr = waitingroom.WaitingRoom(api_key)
>> alerts={"sms": "Hello Mario, this is Peach!", "audio": 79, "email": {"subject": "Needed at castle", "body": "Please come to the castle right away!"}}
>> recipients=[{"name": {"first": "John", "last": "Doe"}, "mobile": "5551234567", "email": "john@example.com"}]
>> wr.simple(alerts, recipients)
```

### Sending an alert to multiple recipients
Recipients is an array of objects, just pass in the "name" object along with any additional/required objects (i.e. "mobile").
```console
>> recipients=[{"name": {"first": "John", "last": "Doe"}, "mobile": "5551234567"}, {"name": {"first": "Jane", "last": "Doe"}, "mobile": "5559876543"}]
>> wr.simple(alerts, recipients)
```

## Notes
You need to initialize the module with an API key as a string (i.e. “009e006beQ7aoPL1" instead of `api_key` in the examples), so be sure to grab one from http://developer.alertcaster.com/developer/apikey

Recipients first and last name need to be set for an alert to successfully be created and sent out
