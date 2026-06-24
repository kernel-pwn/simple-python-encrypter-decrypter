import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")

# encrypt
plain_text = input("Enter a test to encrypt: ")
cipher_tex =""

for letter in plain_text:
    index = chars.index(letter)
    cipher_tex += key[index]

print(f"original text: {plain_text}")
print(f"encrypted text: {cipher_tex}")



# decrypt
cipher_tex = input("Enter a test to decrypt: ")
plain_text = ""

for letter in cipher_tex:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted text: {cipher_tex}")
print(f"original text: {plain_text}")