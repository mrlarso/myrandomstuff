"""
def decode(message):
alphabet = 'abcdefghijklmnopqrstuvwxyz'
    backalpha = alphabet[::-1]
    decoded = ""
    for l in message:
        if l in alphabet:
            decoded += (backalpha[alphabet.index(l)])
        else:
            decoded += " "
    return decoded
"""
def decode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return "".join([alphabet[-(alphabet.index(l)+1)] if l in alphabet else " " for l in message])

print decode("hi")
