


def send_messages(msgs, s_msgs):
    """prints messages to be sent"""
    while msgs:
        messages_to_send = msgs.pop()
        print(f"Sending the message: {messages_to_send}")
        s_msgs.append(messages_to_send)

def sent_messages(messages_sent):
    """print messages that have been sent"""
    for message in messages_sent:
        print(message)
    print(send_msgs)
    print(sent_msgs)


send_msgs = ['Hi Programmer', 'Hi Engineer', 'Hi Architect']
sent_msgs = []

send_messages(send_msgs[:], sent_msgs)
sent_messages(sent_msgs)



