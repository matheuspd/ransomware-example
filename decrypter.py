import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Nome do arquivo criptografado
encrypted_file_name = "test.txt.ransomware"

# Chave de criptografia e IV
key = b'1234567890abcdef'  # Chave fixa de 16 bytes (128 bits)
iv = b'abcdef1234567890'   # IV fixo de 16 bytes (128 bits)

# Abrir o arquivo criptografado
file = open(encrypted_file_name, "rb")
encrypted_data = file.read()

# Descriptografar o arquivo
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_padded = cipher.decrypt(encrypted_data)
decrypted_data = unpad(decrypted_padded, AES.block_size)

# Restaurar o arquivo original
original_file_name = encrypted_file_name.replace(".ransomware", "")
original_file =  open(original_file_name, "wb")
original_file.write(decrypted_data)

# Remover o arquivo criptografado
os.remove(encrypted_file_name)
