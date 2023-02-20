#A silly cipher function to practice tranforming strings in python
#takes a user input, applies a caesar cipher (in this case ROT3)
#then encodes it to emojis for obfuscation, and then base64 encoding for a more general use, and light obfuscation
#Limitations: Currently does not support numeric characters or special characters

import base64

# Define the Caesar cipher function
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Define the emoji encoding function
def encode_emoji(text):
    emoji_map = {
        'a': '😀',
        'b': '😁',
        'c': '😂',
        'd': '🤣',
        'e': '😃',
        'f': '😄',
        'g': '😅',
        'h': '😆',
        'i': '😇',
        'j': '😈',
        'k': '😉',
        'l': '😊',
        'm': '😋',
        'n': '😌',
        'o': '😍',
        'p': '😎',
        'q': '😏',
        'r': '😐',
        's': '😑',
        't': '😒',
        'u': '😓',
        'v': '😔',
        'w': '😕',
        'x': '😖',
        'y': '😗',
        'z': '😘',
        ' ': '👀'
    }
    result = ""
    for char in text:
        if char.lower() in emoji_map:
            result += emoji_map[char.lower()]
    return result

# Get input from user
input_text = input("Enter a message to encode: ")

# Apply Caesar cipher
shift = 3
caesar_text = caesar_cipher(input_text, shift)

# Encode as emojis
emoji_text = encode_emoji(caesar_text)

# Encode as Base64
base64_text = base64.b64encode(emoji_text.encode('utf-8')).decode('utf-8')

# Print the result
print(base64_text)