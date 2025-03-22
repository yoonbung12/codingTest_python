import string

from Python.Day8_functionReee.EncodeTest import shift

alphabet = list(string.ascii_lowercase)
# print(alphabet)

direction = input("Type ~~~Encode: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type Shift number: \n"))

# Todo1
# Todo2
def encrypt(orginal_text, shift_amount):
    cipher_text = ""

    for letter in orginal_text:
        shifted_position = alphabet.index(letter) + shift_amount # 7 -> 9
        cipher_text += alphabet[shifted_position] # j

        print(f"Here is the encoded result: {cipher_text}")


# Todo4
encrypt(orginal_text=text, shift_amount=shift)

