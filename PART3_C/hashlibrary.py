hashing= [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

def hashGeneration(MSG: bytearray) -> bytearray:
    if isinstance(MSG, str):
        MSG = bytearray(MSG, 'ascii')
    elif isinstance(MSG, bytes):
        MSG = bytearray(MSG)
    elif not isinstance(MSG, bytearray):
        raise TypeError
    length = len(MSG) * 8
    MSG.append(0x80)
    while (len(MSG) * 8 + 64) % 512 != 0:
        MSG.append(0x00)
    MSG += length.to_bytes(8, 'big')
    assert (len(MSG) * 8) % 512 == 0, "cannot be fwegn!"
    blocks = []
    for i in range(0, len(MSG), 64):
        blocks.append(MSG[i:i+64])
    hex0 = 0x6a09e667
    hex1 = 0xbb67ae85
    hex2 = 0x3c6ef372
    hex3 = 0xa54ff53a
    hex5 = 0x9b05688c
    hex4 = 0x510e527f
    hex6 = 0x1f83d9ab
    hex7 = 0x5be0cd19
    for MSG_block in blocks:
        MSG_schedule = []
        for t in range(0, 64):
            if t <= 15:
                MSG_schedule.append(bytes(MSG_block[t*4:(t*4)+4]))
            else:
                sec1 = sigma1(int.from_bytes(MSG_schedule[t-2], 'big'))
                sec2 = int.from_bytes(MSG_schedule[t-7], 'big')
                sec3 = sigma0(int.from_bytes(MSG_schedule[t-15], 'big'))
                sec4 = int.from_bytes(MSG_schedule[t-16], 'big')
                #print("sec1",sec1)
                #print("sec2", sec2)
                #print("sec3", sec3)
                #print("sec4", sec4)
                schedule = ((sec1 + sec2 + sec3 + sec4) % 2**32).to_bytes(4, 'big')
                MSG_schedule.append(schedule)

        assert len(MSG_schedule) == 64
        a = hex0
        b = hex1
        c = hex2
        d = hex3
        e = hex4
        f = hex5
        g = hex6
        h = hex7
        for t in range(64):
            t1 = ((h + capsigma1(e) + ch(e, f, g) + hashing[t] +
                   int.from_bytes(MSG_schedule[t], 'big')) % 2**32)

            t2 = (capsigma0(a) + majiner(a, b, c)) % 2**32

            h = g
            g = f
            f = e
            e = (d + t1) % 2**32
            d = c
            c = b
            b = a
            a = (t1 + t2) % 2**32
        hex0 = (hex0 + a) % 2**32
        hex1 = (hex1 + b) % 2**32
        hex2 = (hex2 + c) % 2**32
        hex3 = (hex3 + d) % 2**32
        hex4 = (hex4 + e) % 2**32
        hex5 = (hex5 + f) % 2**32
        hex6 = (hex6 + g) % 2**32
        hex7 = (hex7 + h) % 2**32

    return ((hex0).to_bytes(4, 'big') + (hex1).to_bytes(4, 'big') +
            (hex2).to_bytes(4, 'big') + (hex3).to_bytes(4, 'big') +
            (hex4).to_bytes(4, 'big') + (hex5).to_bytes(4, 'big') +
            (hex6).to_bytes(4, 'big') + (hex7).to_bytes(4, 'big'))
def ch(x_coordinate: int, y_coordinate: int, z_coordinate: int):
    new = (x_coordinate & y_coordinate) ^ (~x_coordinate & z_coordinate)
    return new

def majiner(x_coordinate: int, y_coordinate: int, z_coordinate: int):
    new = (x_coordinate & y_coordinate) ^ (x_coordinate & z_coordinate) ^ (y_coordinate & z_coordinate)
    return new

def rotate(number: int, shift: int, size: int = 32):
    new = (number >> shift) | (number << size - shift)
    return new

def sigma0(number: int):
    number = (rotate(number, 7) ^ rotate(number, 18) ^ (number >> 3))
    #print(number)
    return number

def sigma1(number: int):
    number = (rotate(number, 17) ^ rotate(number, 19) ^ (number >> 10))
    return number

def capsigma0(num: int):
    num = (rotate(num, 2) ^ rotate(num, 13) ^ rotate(num, 22))
    return num

def capsigma1(num: int):
    num = (rotate(num, 6) ^ rotate(num, 11) ^ rotate(num, 25))
    return num

