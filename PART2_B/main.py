from aesLibrary import AES
if __name__ == '__main__':

    #ASSIGN MODEEEEE
    aes_mode = AES(b'\x00' * 16)
    iv = b'\x01' * 16

    #CBC MODE AES IMPLEMENTATION------------------------------------------------------------------------------------
    print("CBC MODE AES IMPLEMENTATION")
    contentx = "Hello world"
    print("CBC MESSAGE : ",contentx)
    ciphertext_cbc = aes_mode.encryptCBC(contentx.encode(), iv)
    plaintext_cbc = aes_mode.decryptCBC(ciphertext_cbc, iv)
    print("cbc mode ciphertext_cbc:", ciphertext_cbc)
    print("cbc mode plain text : ", plaintext_cbc)
    print()

    # OFB MODE AES IMPLEMENTATION------------------------------------------------------------------------------------
    print("OFB MODE AES IMPLEMENTATION")
    content = "Hello world"
    print("OFB MESSAGE : ", content)
    #ofb encrypt decypt
    ciphertext_ofb = aes_mode.encryptOFB(content.encode(), iv)
    plaintext_ofb = aes_mode.decryptOFB(ciphertext_ofb, iv)

    print("ofb mode cipher text:", ciphertext_ofb)
    print("ofb mode plain text : ", plaintext_ofb)
    print()


