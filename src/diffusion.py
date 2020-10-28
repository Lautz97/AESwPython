# region -----------------------shift rows-----------------------


# given the s state matrix shift rows for encryption in the shift rows layer
def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


# given the s state matrix shift rows for decryption in the shift rows layer
def inv_shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]


# endregion


# region -----------------------mix columns-----------------------


# found on github
def xTime(a): return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])


# as in section 4.1.2 in The Design of Rijndael resource pag 69 of 253
def mix_single_column(a):
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xTime(a[0] ^ a[1])
    a[1] ^= t ^ xTime(a[1] ^ a[2])
    a[2] ^= t ^ xTime(a[2] ^ a[3])
    a[3] ^= t ^ xTime(a[3] ^ u)


# as in section 4.1.3 in The Design of Rijndael resource pag 70/71 of 253
def inv_mix_columns(s):
    for i in range(4):
        u = xTime(xTime(s[i][0] ^ s[i][2]))
        v = xTime(xTime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)


# endregion


