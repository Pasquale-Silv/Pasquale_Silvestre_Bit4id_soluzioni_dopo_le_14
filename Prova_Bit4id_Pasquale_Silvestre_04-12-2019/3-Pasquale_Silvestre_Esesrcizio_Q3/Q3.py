import re

clearFile = 'plain_text.txt'
sensitiveWords = 'sensitive_glossary.txt'

with open(sensitiveWords, mode='r') as file1:
    sensitiveWordsList = file1.readlines()

sensitiveWordsList = [word.strip() for word in sensitiveWordsList]
print(sensitiveWordsList)
del sensitiveWordsList[-1]
print(sensitiveWordsList)

with open(clearFile, 'r') as file2:
    new_text = file2.read()
    print(new_text)
    for sensitive_word in sensitiveWordsList:
        regex = sensitive_word
        new_text = re.sub(r"\s" + regex + r".{0,3}\s", " ", new_text)

print(new_text)

with open(clearFile, 'r') as file2_again:
    for element in sensitiveWords:
        regex = element
        fileText = file2_again.read()
        new_terms = re.findall(regex, fileText)

print(new_terms)