# Encryption/Decryption

This is a simple Python program that allows you to encrypt and decrypt messages using base64 encoding.

## Requirements

- Python 3.x
- No additional Python packages are required. The program uses the built-in `base64` module.

## Usage

1. Clone the repository or download the `main.py` file.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the program by executing the following command: `python main.py`.
4. Enter 'e' to encrypt a message or 'd' to decrypt an encrypted message.
5. Follow the prompts and provide the necessary inputs.
6. The program will display the encrypted or decrypted text accordingly.

## Example
```
$ python main.py
Enter 'e' to encrypt a message, 'd' to decrypt an encrypted message: e
Enter the text: Hello, World!
Encrypted text: SGVsbG8sIFdvcmxkIQ==
```
```
$ python main.py
Enter 'e' to encrypt a message, 'd' to decrypt an encrypted message: d
Enter the encrypted text: SGVsbG8sIFdvcmxkIQ==
Decrypted text: Hello, World!
```

## License

This project is licensed under the MIT License.