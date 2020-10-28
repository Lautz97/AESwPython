from src.utils import s_box, inv_s_box


# region -----------------------Byte Substitution-----------------------


# use S boxes to perform the byte sub layer in the encryption
def sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = s_box[s[i][j]]


# use S boxes to perform the byte sub layer in the decryption
def inv_sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = inv_s_box[s[i][j]]

# endregion

