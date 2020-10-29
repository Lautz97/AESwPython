import random
import string


# return a random string of n characters, just for debug
def randomString(n=16):
    return ''.join(random.choice(string.ascii_letters+string.whitespace+string.digits) for i in range(n))


# ask to user how many characters the random string must be, just for debug
def promptStringLength():
    r = input("length of the string?")
    # todo validate input r
    return int(r)


# todo
def readInputsFromFile():
    # todo
    return ""


# get length of a sting in bytes
def utf8len(s): return len(s.encode('utf-8'))


# split a string 16 Bytes by 16 Bytes
# padding stuff stolen from git for wrong sized plain text
def splitBlocks(message, blockSize=16):
    assert len(message) % blockSize == 0
    return [message[i:i + 16] for i in range(0, len(message), blockSize)]

































