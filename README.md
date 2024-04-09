# COE Encryption Tool

## Install Requirements

```bash
pip install -r requirements.txt
```
This step assumes you have Python and pip already installed on your system. If not, please install Python 3.6 or later, which includes pip

## Usage

### Encrypting a Message

To encrypt a message, use the `-e` option followed by the message you want to encrypt, and specify the encryption key with `-k`. Enclose the message in quotes if it contains spaces.

```bash
python3 coe.py -e "Your message here" -k yourkey
```

This command prints the encrypted message to the console.

### Decrypting a Message

To decrypt a message, the encrypted content should be saved in a file. Then, use the -d option followed by the file path, and specify the decryption key with -k.

```bash
python3 coe.py -d path/to/your/file.txt -k yourkey
```
This command prints the decrypted message to the console.



Este `README.md` es directo y va al grano, cubriendo cómo instalar cualquier requisito necesario (en este caso, solo Python) y cómo usar el script para cifrar y descifrar mensajes.
