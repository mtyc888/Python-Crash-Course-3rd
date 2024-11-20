list = ['hello text 1', 'hello text 2', 'hello text 3']

def show_message(list):
    for text in list:
        print(f'{text}')

def send_message(message, sent_message):
    print("\n sending messages:")
    while message:
        current_message = message.pop()
        print(current_message)
        sent_message.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_message(messages)

send_messages = []
send_message(messages,send_messages)

print("\nfinal list:")

print(messages)
print(send_messages)