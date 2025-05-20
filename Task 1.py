def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encryption
encrypted_msg = encrypt(message, shift)
print("Encrypted message:", encrypted_msg)

# Decryption
decrypted_msg = decrypt(encrypted_msg, shift)
print("Decrypted message:", decrypted_msg)
