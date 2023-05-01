import os
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# os.system("clear")

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
while direction not in ['encode', 'decode']:
    # os.system("clear")
    direction = input("Invalid input. Type 'encode' or 'decode':\n").lower()

# os.system("clear")
text = input("Type your message:\n").lower()
while text == '' or text.isspace() or not all(chr.isalpha() or chr.isspace() for chr in text):
    # os.system("clear")
    text = input("Invalid input. Please enter a message with only letters and spaces:\n")

def get_shift():
    try:
        shift = int(input("Type the shift number:\n"))
        return shift
    except:
        os.system("clear")
        print("Invalid input. Please enter an integer.\n")
        return 0

# os.system("clear")
shift = get_shift()
while shift > 25 or shift < 1:
    # os.system("clear")
    print("Invalid input. Please enter an integer between 1 and 25.")
    shift = get_shift()

def encrypt(text, shift):
    # os.system("clear")
    encrypted_message = ''
    for letter in text:
        if letter.isspace():
            encrypted_message += ' '
        else:
            original_index = alphabet.index(letter)
            new_index = original_index + shift
            if new_index > 25:
                new_index -= 26
            encrypted_message += alphabet[new_index]
    return encrypted_message

def decrypt(text, shift):
    # os.system("clear")
    decrypted_message = ''
    for letter in text:
        if letter.isspace():
            decrypted_message += ' '
        else:
            original_index = alphabet.index(letter)
            new_index = original_index - shift
            if new_index < 0:
                new_index += 26
            decrypted_message += alphabet[new_index]
    return decrypted_message

if direction == "encode":
    result = encrypt(text, shift)
    print(f"{text} encoded with shift of {shift} becomes {result}.")
else:
    result = decrypt(text, shift)
    print(f"{text} decoded with shift of {shift} becomes {result}.")