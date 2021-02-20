import os
from aesLibrary import AES
import sys
from hashlibrary import hashGeneration
if __name__ == '__main__':
    import sys
    write = lambda b: sys.stdout.buffer.write(b)
    read = lambda: sys.stdin.buffer.read()
    if len(sys.argv) != 4:
        print("----------- USAGE ------------------------")
        print("python main.py aes_mode file_path key")
    elif len(sys.argv) == 4:
        print(sys.argv[2])
        if sys.argv[1] == "cbc":
            print("CBC MODE AES IMPLEMENTATION")
            plain_file = open(""+sys.argv[2], "rb+")
            contentx = plain_file.read()
        elif sys.argv[1] == "ofb":
            print("OFB MODE AES IMPLEMENTATION")
            print(sys.argv[2])
            plain_file = open(sys.argv[2], "rb+")
            contentx = plain_file.read()
        print(type(sys.argv[3]))
        temp = sys.argv[3].encode('utf-16')
        aes_mode = AES(temp)
        iv = b'\x01' * 16



        BEFORE_HASH = hashGeneration(contentx).hex()

        #CALCULATE CBC HASHING
        print("BEFORE ENCODE HASH: ",BEFORE_HASH)
        print("FILE CONTENT : ",contentx)
        if sys.argv[1] == "cbc":
            ciphertext = aes_mode.encryptCBC(contentx, iv)
            plaintext = aes_mode.decryptCBC(ciphertext, iv)
        else:
            ciphertext = aes_mode.encryptOFB(contentx, iv)
            plaintext = aes_mode.decryptOFB(ciphertext, iv)
        plain_file.write(ciphertext)
        plain_file.write(sys.argv[3].encode())
        print("ciphertext_cbc:", ciphertext)
        print("plain text : ", plaintext)
        plain_file.close()
        #AFTER HASHING CBC FILE
        plain_file = open(sys.argv[2], "rb+")
        contentx = plain_file.read()
        AFTER_HASH = hashGeneration(contentx).hex()
        print()
        print("AFTER ENCODE HASH CBC FILE")
        if AFTER_HASH == BEFORE_HASH :
            print("BEFORE ENCODE HASH : ", BEFORE_HASH)
            print("AFTER ENCODE HASH  :", AFTER_HASH)
            print("cbc same files!!!")
        else:
            print("BEFORE ENCODE HASH: ", BEFORE_HASH)
            print("AFTER ENCODE HASH :", AFTER_HASH)
            print("hash changes , they are not same files")
        print()


