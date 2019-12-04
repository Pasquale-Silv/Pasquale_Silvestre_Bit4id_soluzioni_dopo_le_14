from Q1 import shift_left, shift_right, shift
import random

dictTransf = {}

def cypher_binary(str):
    encrypt = ''
    for ch in str:
        a = ord(ch) + 1
        encrypt += chr(a)
    encryptBinary = transformInBinary(encrypt)
    return encryptBinary


def transformInBinary(str2):
    global dictTransf
    encryptWord = ''
    for ch in str2:
        if ch in dictTransf:
            dictTransf[ch] += str(random.randint(0, 1))
        else:
            dictTransf[ch] = str(random.randint(0, 1))
    for letter in str2:
        for k, v in dictTransf.items():
            if letter == k:
                encryptWord += dictTransf[k]
    return encryptWord

def spaceBinary(wordBinary):
    binList = list(wordBinary)
    return " ".join(binList)

encrypt1 = cypher_binary("Ciao Pasquale")
print(encrypt1)
encrypt1 = shift(encrypt1, 'right', 2)
print(encrypt1)
spaceBinaryWord = spaceBinary(encrypt1)
print(spaceBinaryWord)
