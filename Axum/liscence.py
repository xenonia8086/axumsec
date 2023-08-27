import secrets
import hashlib


def generate_license_key(length=20):
    return secrets.token_hex(length)


def hash_key(key):
    return hashlib.sha256(key.encode()).hexdigest()


stored_key = hash_key(generate_license_key())

 
file_path = "key.txt" 

with open(file_path, "w") as file:
    file.write(stored_key)







