# import required module
import os
from cryptography.fernet import Fernet




file_dir=[]

def list_files(start_path):

    # Walk through directory tree
    for root, dirs, files in os.walk(start_path):
        # Print current directory
        print(f"\nDirectory: {root}")

        # Print all files in current directory
        for file in files:
            # Create full file path
            full_path = os.path.join(root, file)
            file_dir.append(full_path)
def decrypt_files(filename):
    with open('encryptKey.pem', 'rb') as f:
        encryptKey = f.read()
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    fernet = Fernet(encryptKey)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename.split(".bimahoa")[0], "wb") as f:
        f.write(decrypted_data)

list_files("E:\\testEncryptFile")
for file in file_dir:
    if file.endswith(".bimahoa"):
        decrypt_files(file)
        print("Decrypted successfully")
        os.remove(file)


