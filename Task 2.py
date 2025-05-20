from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path="encrypted_image.jpg", key=50):
    try:
        img = Image.open(image_path).convert('RGB')
        img_arr = np.array(img).astype(np.int16)  # Convert to avoid overflow

        encrypted_arr = (img_arr + key) % 256     # Apply encryption logic
        encrypted_img = Image.fromarray(encrypted_arr.astype(np.uint8))  # Convert back

        encrypted_img.save(output_path)
        print(f"Encryption done. Saved as '{output_path}'")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(encrypted_path, output_path="decrypted_image.jpg", key=50):
    try:
        img = Image.open(encrypted_path).convert('RGB')
        img_arr = np.array(img).astype(np.int16)  # Convert to avoid underflow

        decrypted_arr = (img_arr - key) % 256     # Apply decryption logic
        decrypted_img = Image.fromarray(decrypted_arr.astype(np.uint8))  # Convert back

        decrypted_img.save(output_path)
        print(f"Decryption done. Saved as '{output_path}'")
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    original_image = "original_image.jpg"   # Ensure this image exists in the same folder
    encryption_key = 123

    encrypt_image(original_image, "encrypted_image.jpg", encryption_key)
    decrypt_image("encrypted_image.jpg", "decrypted_image.jpg", encryption_key)
