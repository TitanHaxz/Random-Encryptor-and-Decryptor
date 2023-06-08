import base64

def encrypt(text):
    encrypted_text = base64.b64encode(text.encode()).decode()
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = base64.b64decode(encrypted_text.encode()).decode()
    return decrypted_text

def main():
    choice = input("Enter 'e' to encrypt a message, 'd' to decrypt an encrypted message: ")
    
    if choice == 'e':
        text = input("Enter the text: ")
        encrypted_text = encrypt(text)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        encrypted_text = input("Enter the encrypted text: ")
        decrypted_text = decrypt(encrypted_text)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
