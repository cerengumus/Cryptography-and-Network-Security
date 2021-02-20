from aesLibrary import AES
if __name__ == '__main__':
    master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
    M = AES(master_key)
    M.change(master_key)
    plaintext = 0x3243f6a8885a308d313198a2e0370734
    print("master_key:", master_key)
    print("plain text:", plaintext)
    encrypted = M.encrypt(plaintext)
    print("encrypted",encrypted)
    ciphertext = 0x3925841d02dc09fbdc118597196a0b32
    print("cipher text:", ciphertext)
    decrypted = M.decrypt(ciphertext)
    print("decrypted", decrypted)
