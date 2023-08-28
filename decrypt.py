def generateLFSR(key: bytes):
    key = key * 2
    state = [0x12000032, 0x2527ac91, 0x888c1214]

    for i in range(4):
        state[0] = key[i] | (state[0] << 8)
        state[1] = key[4+i] | (state[1] << 8)
        state[2] = key[8+i] | (state[2] << 8)

    state[0] &= 0xffffffff
    state[1] &= 0xffffffff
    state[2] &= 0xffffffff

    return state


def xorByte(byte, state):
    flag1 = 1
    flag2 = 0
    res = 0
    for _ in range(8):
        aa = state[0] >> 1
        if state[0] & 1:
            state[0] = aa ^ 0xC0000031
            bb = state[1] >> 1
            flag1 = state[1] & 1
            if flag1:
                state[1] = ((bb | 0xC0000000) ^ 0x20000010)
            else:
                state[1] = bb & 0x3FFFFFFF
        else:
            state[0] = aa
            c = state[2] >> 1
            flag2 = state[2] & 1
            if flag2:
                state[2] = ((c | 0xF0000000) ^ 0x8000001)
            else:
                state[2] = c & 0xFFFFFFF

        res = (flag1 ^ flag2) | (res << 1)
    return res ^ byte


def xorData(data):
    dat = list(data)
    s = generateLFSR(b"a271730728cbe141e47fd9d677e9006d")
    for i in range(0, 128):
        dat[i] = xorByte(dat[i], s)
    return bytes(dat)
