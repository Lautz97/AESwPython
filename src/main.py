from src import test, aes
import string


print("AES - 128")
# generate a random string prompting the length
inputPlain = test.randomString(test.promptStringLength())
# inputPlain = utils.readInputsFromFile()
# split the plain text in an array of 16Bytes each row
inputPlainA = test.splitBlocks(inputPlain)

generatedKey = test.randomString(16)


print("the key is: " + generatedKey)

print("the input is: " + inputPlain)
print("the splitted input is: ", inputPlainA)
print("the length of each row is: ", [test.utf8len(i) for i in inputPlainA])


encrypted = aes.AES(bytes(generatedKey, encoding='utf-8')).singleBlockEncrypt(bytes(inputPlainA[0], encoding='utf-8'))
print("encrypted plain text = ", encrypted)

decrypted = aes.AES(bytes(generatedKey, encoding='utf-8')).singleBlockDecrypt(encrypted)
print("decrypted plain text = " + decrypted.decode('utf-8'))
