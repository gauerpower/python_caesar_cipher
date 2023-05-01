alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
while direction not in ['encode', 'decode']:
    direction = input("Invalid input. Type 'encode' or 'decode':\n").lower()
text = input("Type your message:\n").lower()
while text == '' or text.isspace() or not all(chr.isalpha() or chr.isspace() for chr in text):
    text = input("Invalid input. Please enter a message with only letters and spaces:\n")

def get_shift():
    try:
        shift = int(input("Type the shift number:\n"))
        return shift
    except:
        print("Invalid input. Please enter an integer.\n")
        return 0
shift = get_shift()
while shift > 25 or shift < 1:
    print("Invalid input. Please enter an integer between 1 and 25.")
    shift = get_shift()

def caesar(direction, text, shift):
    message = ''
    for letter in text:
        if letter.isspace():
            message += ' '
        else:
            original_index = alphabet.index(letter)
            if direction == 'encode':
                new_index = original_index + shift
                if new_index > 25:
                    new_index -= 26
            else:
                new_index = original_index - shift
                if new_index < 0:
                    new_index += 26
            message += alphabet[new_index]
    return message

result = caesar(direction, text, shift)
print(f"{text} encoded with shift of {shift} becomes {result}.")