from src import test, aes
from time import perf_counter as pC


# region TEST FUNCTIONS


# do a single block test
def testRndSingleBlock():
    # generate a random key of 16 bytes
    generatedKey = test.randomString(16)
    print("the key used is: " + generatedKey)
    # generate a random string prompting the length
    inputPlain = test.randomString(16)
    # split the plain text in an array of 16Bytes each row
    inputPlainA = test.splitBlocks(inputPlain)
    # show some info
    print("the input is: " + inputPlain)
    print("the splitted input is: ", inputPlainA)
    print("the length of each row is: ", [test.utf8len(i) for i in inputPlainA])
    # encrypt and show result
    encrypted = aes.AES(generatedKey).singleBlockEncrypt(bytes(inputPlainA[0], encoding='utf-8'))
    print("encrypted plain text = ", encrypted)
    # decrypt and show the result
    decrypted = aes.AES(generatedKey).singleBlockDecrypt(encrypted)
    print("decrypted plain text = " + decrypted.decode('utf-8'))
    # confirm a correct decode
    if inputPlain == decrypted.decode('utf-8'):
        print("OK")
    else:
        print("something went wrong")


# test a given number of 16 bytes plainText
def testRndBlocks():
    # generate a random key of 16 bytes
    generatedKey = test.randomString(16)
    print("the key used is: " + generatedKey)
    # generate a random string prompting the length
    inputPlain = test.randomString(test.promptStringLength("insert number of 16B block: ", 16))
    # split the plain text in an array of 16Bytes each row
    inputPlainA = test.splitBlocks(inputPlain)
    # show some info
    print("the input is: " + inputPlain)
    print("the splitted input is: ", inputPlainA)
    print("the length of each row is: ", [test.utf8len(i) for i in inputPlainA])
    # encrypt and show result
    encryptedArray = aes.AES(generatedKey).encrypt(inputPlainA)
    print("encryptedArray plain text = ", encryptedArray)
    # decrypt and show the result
    decrypted = aes.AES(generatedKey).decrypt(encryptedArray)
    print("decrypted plain text = " + decrypted)
    # confirm a correct decode
    if inputPlain == decrypted:
        print("OK")
    else:
        print("something went wrong")


def testTiming(showOutput=False):
    dimensions = [1024, 102400, 10240000]
    # dimensions = [102400, 102400, 102400]
    for dim in dimensions:
        generatedKey = test.randomString(16)
        inputPlain = test.randomString(dim)
        inputPlainA = test.splitBlocks(inputPlain)

        t0 = pC()

        te0 = pC()
        encryptedArray = aes.AES(generatedKey).encrypt(inputPlainA)
        if showOutput:
            print("encryptedArray plain text = ", encryptedArray)
        te1 = pC() - te0

        td0 = pC()
        decrypted = aes.AES(generatedKey).decrypt(encryptedArray)
        if showOutput:
            print("decrypted plain text = " + decrypted)
        td1 = pC() - td0

        t1 = pC() - t0
        if inputPlain == decrypted:
            print("input length: ", dim)
            print("Total time elapsed: ", t1, " seconds")
            print("Encryption time: ", te1, " seconds")
            print("Decryption time: ", td1, " seconds")
        else:
            print("something went wrong")


# endregion


print("AES - 128 Python implementation by Lauterio Davide")

testTiming()

# input length:  1024
# Total time elapsed:  0.051485299999999956  seconds
# Encryption time:  0.02237230000000001  seconds
# Decryption time:  0.02910809999999997  seconds
# input length:  102400
# Total time elapsed:  4.7761286  seconds
# Encryption time:  2.0138437  seconds
# Decryption time:  2.7622816999999995  seconds
# input length:  10240000
# Total time elapsed:  467.3741961  seconds
# Encryption time:  195.2238076  seconds
# Decryption time:  272.1503844  seconds
