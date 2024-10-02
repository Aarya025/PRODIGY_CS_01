# image encryption tool using pixel manipulation.
from PIL import Image  # imports image file from Pillow library

def encrypt_image(image_path, key, save_format):
    with Image.open(image_path) as img:
        pixels = img.load()  # Load image pixels
        width, height = img.size

        # Check if the image is RGB, RGBA, or grayscale
        for i in range(width):
            for j in range(height):
                pixel_values = pixels[i, j]

                if isinstance(pixel_values, int):  # For grayscale images (a single int per pixel)
                    # Encrypt by adding the key and applying modulo
                    pixels[i, j] = (pixel_values + key) % 256

                elif len(pixel_values) == 3:  # RGB image (3 values per pixel)
                    r, g, b = pixel_values
                    pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

                elif len(pixel_values) == 4:  # RGBA image (r,g,b values are encrypted, alpha channel is left unchanged)
                    r, g, b, a = pixel_values
                    pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256, a)  # Keep alpha unchanged

        encrypted_image_path = f'encrypted_image.{save_format.lower()}'
        img.save(encrypted_image_path, format=save_format.upper())
        print(f"Image encrypted & saved as {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key, save_format):
    with Image.open(encrypted_image_path) as img:
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                pixel_values = pixels[i, j]

                if isinstance(pixel_values, int):  # For grayscale images
                    # Decrypt by subtracting the key and applying modulo
                    pixels[i, j] = (pixel_values - key) % 256

                elif len(pixel_values) == 3:  # RGB image
                    r, g, b = pixel_values
                    pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

                elif len(pixel_values) == 4:  # RGBA image (with alpha channel)
                    r, g, b, a = pixel_values
                    pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256, a)  # Keep alpha unchanged

        decrypted_image_path = f'decrypted_image.{save_format.lower()}'
        img.save(decrypted_image_path, format=save_format.upper())
        print(f"Image decrypted & saved as {decrypted_image_path}")

# Main function to handle user input
def main():
    print("Welcome to the Image Encryption/Decryption Tool!")

    # Ask the user for the image path
    image_path = input("Enter the path of the image file: ")

    # Ask the user for the encryption/decryption key
    key = int(input("Enter the encryption/decryption key (integer): "))

    # Ask the user for the desired image file format
    print("Choose the format to save the image:")
    print("1. PNG")
    print("2. JPEG")
    print("3. BMP")
    print("4. TIFF")
    format_choice = input("Enter the number corresponding to your choice (1-4): ")

    # Map user input to file format
    format_options = {
        '1': 'PNG',
        '2': 'JPEG',
        '3': 'BMP',
        '4': 'TIFF'
    }
    save_format = format_options.get(format_choice, 'PNG')  # Default to PNG if invalid choice

    # Ask the user whether to encrypt or decrypt
    operation = input("Do you want to (e)ncrypt or (d)ecrypt the image? Enter 'e' or 'd': ").lower()

    if operation == 'e':
        encrypt_image(image_path, key, save_format)
    elif operation == 'd':
        decrypt_image(image_path, key, save_format)
    else:
        print("Invalid option. Please choose 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
