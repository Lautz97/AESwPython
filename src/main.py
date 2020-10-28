import src.utils as utils


# initialize the S-Box and the inverted S-Box
# initSBox() -> lookup table

print("AES - 128")
# generate a random string prompting the length
inputPlain = utils.randomString(utils.promptStringLength())
# inputPlain = utils.readInputsFromFile()
# split the plain text in an array of 16Bytes each row
inputPlainA = utils.splitString(inputPlain)


# must get a key


print("the input is: ", inputPlain)
print("the splitted input is: ", inputPlainA)
print("the length of each row is: ", [utils.utf8len(i) for i in inputPlainA])

# initialize the state matrix from a row of the splitted plain text array
# initState(plain16BytesString)

# key transformation
# keyT = doKeyTransformation(key)

# key addition
# doKeyWhitening(state, keyT)

# compute Byte Substitution / Confusion
# doConfusion(state, sBox)

# compute the Diffusion Layer in separate functions
# doShiftRows(state)
# doMixColumns(state)

# add Decryption stuff
# todo

