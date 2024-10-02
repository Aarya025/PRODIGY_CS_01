# Caesar cipher encryption and decryption
def caesar_cipher(text, shift):
    result = ""

    # Traverse through the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():  # Correct method is isupper()
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():  # Correct method is islower()
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # If it's not a letter, leave it as it is
        else:
            result += char

    return result

# Caesar cipher decryption (reuse caesar_cipher by reversing the shift)
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher(text, -shift)  # Decrypt by using the negative of the shift

def main():
    print("Caesar Cipher Algorithm")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice, exiting...")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Call the appropriate function based on user choice
    if choice == 'd':
        result_message = caesar_cipher_decrypt(message, shift)
    else:
        result_message = caesar_cipher(message, shift)

    print(f"Resulting message: {result_message}")

if __name__ == "__main__":
    main()
