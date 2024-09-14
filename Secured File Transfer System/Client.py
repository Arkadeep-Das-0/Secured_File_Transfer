from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
import socket

def encrypt_data(raw_data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv + cipher.encrypt(pad(raw_data, AES.block_size))

client_socket = socket.socket()
host = 'localhost'
port = 12345

client_socket.connect((host, port))

# Simulated file content
file_content = b'This is a test file'

# Simulated key (must be securely exchanged in real applications)
key = b'sixteen byte key'

# Encrypt the file content
encrypted_file = encrypt_data(file_content, key)

# Hash the file content for integrity
file_hash = sha256(file_content).hexdigest().encode()

# Send encrypted file and hash
client_socket.send(encrypted_file)
client_socket.send(file_hash)

client_socket.close()
print('File sent successfully.')
