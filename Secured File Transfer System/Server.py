from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from hashlib import sha256
import socket

def decrypt_data(encrypted_message, key):
    iv = encrypted_message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    original_data = unpad(cipher.decrypt(encrypted_message[AES.block_size:]), AES.block_size)
    return original_data

server_socket = socket.socket()
host = 'localhost'
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)
print('Waiting for a connection...')
connection, addr = server_socket.accept()

# Receive the encrypted file and hash
encrypted_file = connection.recv(1024)
received_hash = connection.recv(64)

# Simulated key (must be securely exchanged in real applications)
key = b'sixteen byte key'

# Decrypt the data
decrypted_file = decrypt_data(encrypted_file, key)

# Compute hash to verify integrity
assert sha256(decrypted_file).hexdigest() == received_hash.decode(), "Data integrity compromised!"

print('File received and verified successfully.')
connection.close()