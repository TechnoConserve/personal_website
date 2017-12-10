from channels import Group


def ws_connect(message):
    print('Someone connected.')
    path = message['path']

    if path == b'/sensor/':
        print('Adding new user to sensor group.')
        Group('sensor').add(message.reply_channel)
        message.reply_channel.send({
            'text': "You're connected to the sensor group.",
        })
    else:
        print('Nope.')


def ws_message(message):
    print('Received!' + message['text'])


def ws_disconnect(message):
    print('Someone left us.')
    Group('sensor').discard(message.reply_channel)
