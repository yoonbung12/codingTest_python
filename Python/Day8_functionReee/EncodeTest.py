alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encryto, type 'decode' to decrypt: \n").lower()
text = input("Type your messages: \n").lower()
shift = int(input("Type shift numver: \n"))

# Todo1: Create a function called 'encrypt()' that takes original_text and shift_amount as 2 inputs.
def encrypt(original_text , shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position = shifted_position % len(alphabet) # 0 ~ 25
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text= text, shift_amount= shift)


# Todo2: Inside the~~~