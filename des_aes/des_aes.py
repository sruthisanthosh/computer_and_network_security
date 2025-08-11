from Crypto.Cipher import DES,AES
from Crypto.Util.Padding import pad, unpad
import time, os

#--------------------------DES Encryption & Decryption------------------------------

def get_des_plaintext():
    with open('des_aes/des_plaintext.txt','rb') as file:
        text = file.read()
        return text

def des_encrypt(plaintext):
    print("Enterring DES Encryption")
    key_des = os.urandom(8)
    cipher=DES.new(key_des,DES.MODE_ECB)

    start_time_des = time.time()
    des_ciphertext=cipher.encrypt(pad(plaintext,DES.block_size))
    end_time_des =time.time()
    des_encrypt_time = end_time_des - start_time_des
    return des_ciphertext,key_des,des_encrypt_time

def des_decrypt(ciphertext,des_key):
    print("\nEnterring DES Decryption")
    decipher=DES.new(des_key,DES.MODE_ECB)

    start_time_des = time.time()
    des_decrypt_result=unpad(decipher.decrypt(ciphertext),DES.block_size)
    end_time_des =time.time()
    des_decrypt_time = end_time_des - start_time_des
    return des_decrypt_result,des_decrypt_time

def DES_crypt():
    des_plaintext = get_des_plaintext()
    print("The DES plaintext is:", des_plaintext)
    des_ciphertext,des_key,des_encrypt_time=des_encrypt(des_plaintext)
    print("The Encrypted DES ciphertext is:", des_ciphertext)
    #print("Time taken for DES encryption is:",des_encrypt_time)

    des_decrypt_result,des_decrypt_time=des_decrypt(des_ciphertext,des_key)
    print("The Decrypted DES plaintext is:", des_decrypt_result)
    #print("Time taken for DES decryption is:",des_decrypt_time)

    if des_decrypt_result==des_plaintext:
        print("\nThe DES Encryption and Decrytion is successful!")
        print("Total time for DES:",f"{(des_encrypt_time+des_decrypt_time):.16e}","\n")

#--------------------------AES Encryption & Decryption------------------------------
        
def get_aes_plaintext():
    with open('des_aes/aes_plaintext.txt','rb') as file:
        text = file.read()
        return text

def aes_encrypt(plaintext):
    print("Enterring AES Encryption")
    key_size=int(input("Select the key size for AES(16, 24, 32):"))
    key_aes = os.urandom(key_size)
    cipher=AES.new(key_aes,AES.MODE_ECB)
    
    start_time_aes = time.time()
    aes_ciphertext=cipher.encrypt(pad(plaintext,AES.block_size))
    end_time_aes =time.time()
    aes_encrypt_time = end_time_aes - start_time_aes
    return aes_ciphertext,key_aes,aes_encrypt_time

def aes_decrypt(ciphertext,key_aes):
    print("\nEnterring AES Decryption")
    decipher=AES.new(key_aes,AES.MODE_ECB)

    start_time_aes = time.time()
    aes_decrypt_result=unpad(decipher.decrypt(ciphertext),AES.block_size)
    end_time_aes =time.time()
    aes_decrypt_time = end_time_aes - start_time_aes
    return aes_decrypt_result,aes_decrypt_time

def AES_crypt():
    aes_plaintext = get_aes_plaintext()
    print("The AES plaintext is:", aes_plaintext)
    aes_ciphertext,key_aes,aes_encrypt_time=aes_encrypt(aes_plaintext)
    print("The Encrypted AES ciphertext is:", aes_ciphertext)
    #print("Time taken for AES encryption is:",aes_encrypt_time)

    aes_decrypt_result,aes_decrypt_time=aes_decrypt(aes_ciphertext,key_aes)
    print("The Decrypted AES plaintext is:", aes_decrypt_result)
    #print("Time taken for AES decryption is:",aes_decrypt_time)

    if aes_decrypt_result==aes_plaintext:
        print("\nThe AES Encryption and Decrytion is successful!")
        print("Total time for AES:",f"{(aes_encrypt_time+aes_decrypt_time):.16e}","\n")


#--------------------------Main function------------------------------

if __name__ == "__main__":

    #DES
    DES_crypt();
    print('__'*25,'\n')
    #AES
    AES_crypt();



    



