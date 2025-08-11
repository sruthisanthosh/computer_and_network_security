import pyDes
#from Crypto.Util.Padding import pad, unpad
import os

def brute_force_decrypt(ciphertext_bytes):
    print("Brute Force Decrypt")
    count =1
    while(count<3):
        des_key = os.urandom(8)
        print(des_key)
        #decipher=DES.new(des_key,DES.MODE_ECB)
        #des_decrypt_result=unpad(decipher.decrypt(ciphertext),DES.block_size)
        # Create a DES object
        des = pyDes.des(des_key, pyDes.ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)  
        # Decrypt the data
        decrypted_data = des.decrypt(ciphertext_bytes)
        # Convert bytes to string
        decrypted_string = decrypted_data.decode('utf-8').rstrip('\0')  # Remove padding
        print("The Decrypted DES plaintext is:", decrypted_string)
        count = count + 1

if __name__ == "__main__":
    ciphertext = "ce126d2ddf2d1e64"
    #ciphertext_bytes = bytes.fromhex(ciphertext)
    #print(ciphertext_bytes)
    brute_force_decrypt(ciphertext)

 
