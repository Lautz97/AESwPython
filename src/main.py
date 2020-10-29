from src import test, aes
import string


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
    inputPlain = test.randomString(test.promptStringLength("insert number of 16B block: ",16))
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


# endregion


print("AES - 128 Python implementation by Lauterio Davide")

testRndBlocks()


# inputPlain = utils.readInputsFromFile()

