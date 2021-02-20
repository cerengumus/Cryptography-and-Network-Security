import os
from aesLibrary import AES
from hashlibrary import hashGeneration


if __name__ == '__main__':
    #FILE OPENSSSSSS
    plain_file_cbc = open(r"plain_file_cbc", "rb+")
    plain_file_ofb = open(r"plain_file_ofb", "rb+")

    #ASSIGN MODEEEEE
    aes_mode = AES(b'\x00' * 16)
    iv = b'\x01' * 16

    #CBC MODE AES IMPLEMENTATION------------------------------------------------------------------------------------
    print("CBC MODE AES IMPLEMENTATION")
    contentx = plain_file_cbc.read()
    CBC_BEFORE_HASH = hashGeneration(contentx).hex()

    #CALCULATE CBC HASHING
    print("BEFORE ENCODE HASH CBC FILE: ",CBC_BEFORE_HASH)
    print("CBC FILE CONTENT : ",contentx)
    ciphertext_cbc = aes_mode.encryptCBC(contentx, iv)
    plaintext_cbc = aes_mode.decryptCBC(ciphertext_cbc, iv)
    plain_file_cbc.write(ciphertext_cbc)
    print("cbc mode ciphertext_cbc:", ciphertext_cbc)
    print("cbc mode plain text : ", plaintext_cbc)
    plain_file_cbc.close()
    #AFTER HASHING CBC FILE
    plain_file_cbc = open(r"plain_file_cbc", "rb+")
    contentx = plain_file_cbc.read()
    CBC_AFTER_HASH = hashGeneration(contentx).hex()
    print()
    print("AFTER ENCODE HASH CBC FILE")
    if CBC_AFTER_HASH == CBC_BEFORE_HASH :
        print("BEFORE ENCODE HASH CBC FILE: ", CBC_BEFORE_HASH)
        print("AFTER ENCODE HASH CBC FILE :", CBC_AFTER_HASH)
        print("cbc same files!!!")
    else:
        print("BEFORE ENCODE HASH CBC FILE: ", CBC_BEFORE_HASH)
        print("AFTER ENCODE HASH CBC FILE :", CBC_AFTER_HASH)
        print("hash changes , they are not same files")
        print("Data integrity changed")
    print()

    # OFB MODE AES IMPLEMENTATION------------------------------------------------------------------------------------
    print("OFB MODE AES IMPLEMENTATION")
    content = plain_file_ofb.read()
    print("OFB FILE CONTENT : ", content)
    # CALCULATE OFB HASHING BEFORE
    OFB_BEFORE_HASH = hashGeneration(contentx).hex()
    print("BEFORE ENCODE HASH OFB FILE : ", OFB_BEFORE_HASH)
    #ofb encrypt decypt
    ciphertext_ofb = aes_mode.encryptOFB(content, iv)
    plaintext_ofb = aes_mode.decryptOFB(ciphertext_ofb, iv)
    temp = ciphertext_ofb
    plain_file_ofb.write(temp)
    print("ofb mode cipher text:", ciphertext_ofb)
    print("ofb mode plain text : ", plaintext_ofb)
    print()
    plain_file_ofb.close()
    # CALCULATE OFB HASHING AFTER
    print("CALCULATE OFB HASHING AFTER")
    plain_file_ofb = open(r"plain_file_ofb", "rb+")
    content = plain_file_ofb.read()
    print("OFB FILE CONTENT : ", content)
    OFB_AFTER_HASH = hashGeneration(content).hex()
    if OFB_AFTER_HASH == OFB_BEFORE_HASH:
        print("BEFORE ENCODE HASH OFB FILE: ", OFB_BEFORE_HASH)
        print("AFTER ENCODE HASH OFB FILE : ", OFB_AFTER_HASH)
        print("ofb same files!!!")
    else:
        print("BEFORE ENCODE HASH OFB FILE: ", OFB_BEFORE_HASH)
        print("AFTER ENCODE HASH OFB FILE : ", OFB_AFTER_HASH)
        print("hash changes , they are not same files")
        print("Data integrity changed")
    print()

