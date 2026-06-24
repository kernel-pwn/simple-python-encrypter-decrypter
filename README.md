# Simple Python Encrypter/Decrypter

This is a personal learning project that demonstrates a very simple substitution-based encrypter/decrypter written in Python. It's intended for learning and experimentation only.

## What this project does

- Builds a character set including punctuation, digits, letters, and the space character.
- Creates a randomized substitution key by shuffling that character set.
- Lets you encrypt a message by substituting each character using the generated key.
- Lets you decrypt a ciphertext in the same program run by reversing the substitution.

## Usage

1. Run the script:

   ```bash
   python3 encryption_program.py
   ```

2. When prompted, enter the text you want to encrypt. The program will print the original and encrypted text.
3. When prompted to decrypt, paste the encrypted text to see the original recovered (this only works if the program has the same key in memory — i.e., don't restart the script between encrypt and decrypt).

## Important notes and limitations

- This is not secure encryption. It is a basic substitution cipher (monoalphabetic) intended for learning purposes only.
- The key is generated randomly each time the script runs. If you restart the script you will get a new key and previously encrypted text cannot be decrypted by a new run.
- For any real security-sensitive needs, use a proven cryptographic library such as `cryptography` or `PyCrypto` and established algorithms.

## Files

- `encryption_program.py` — the simple encrypter/decrypter script.

## License

This repository is a personal learning project. Use at your own risk. If you'd like a formal license added, tell me which one (e.g., MIT, Apache-2.0) and I can add it.
