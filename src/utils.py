import random
import string


# return a random string of n characters, just for debug
def randomString(n=16):
    return ''.join(random.choice(string.ascii_letters+string.whitespace+string.digits) for i in range(n))


# ask to user how many characters the random string must be, just for debug
def promptStringLength():
    r = input("length of the string?")
    return int(r)


# todo
def readInputsFromFile():
    # todo
    return ""


# get length of a sting in bytes
def utf8len(s):
    return len(s.encode('utf-8'))


# split a string 16 Bytes by 16 Bytes
def splitString(s=""):
    res = s
    res = [res[i:i + 16] for i in range(0, len(res), 16)]
    return res
