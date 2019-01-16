#TEST_MESSAGE = input()
import string
substitution = [['a', '4'], ['e', '3'], ['l', '1'], ['o', '0'], ['t', '7']]
def encode_message(message, substitution):
    for s in substitution:
        old = s[0]
        new = s[1]
        converted = message.replace(old, new)
        message = converted
        print("converted text = "+converted)
        print(s)
    return converted
message = input("Type the message to be encoded here: ")
converted_text = encode_message(message, substitution)
print("started with "+message)
print("Converted to "+converted_text)


