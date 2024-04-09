import argparse
from co_encryption import encrypt, decrypt  # Asegúrate de importar tus funciones aquí


def main():
    parser = argparse.ArgumentParser(description="COE Encryption Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", metavar="TEXT", help="Text to encrypt.")
    group.add_argument("-d", "--decrypt", metavar="FILE", help="File containing text to decrypt.")
    parser.add_argument("-k", "--key", required=True, help="Encryption/Decryption key.")

    args = parser.parse_args()

    if args.encrypt:
        encrypted_text = encrypt(args.encrypt.replace(' ', ''), args.key)
        print(f"Encrypted Text:\n{encrypted_text}")
    elif args.decrypt:
        try:
            with open(args.decrypt, 'r') as file:
                encrypted_message = file.read().strip()
                decrypted_message = decrypt(encrypted_message, args.key)
                print(f"Decrypted Message:\n{decrypted_message}")
        except FileNotFoundError:
            print("Error: The specified file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
