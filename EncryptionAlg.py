word = "apple"
def encrypt(word):
    lenOfword = len(word)
    newWord = ""
    index = 0
    while lenOfword>0:
        if word[lenOfword-1] == "a":
            newWord += "0"
        elif word[lenOfword-1] == "e":
            newWord += "1"
        elif word[lenOfword-1] == "i":
            newWord += "2"
        elif word[lenOfword-1] == "o":
            newWord += "3"
        elif word[lenOfword-1] == "u":
            newWord += "4"
        else:
            newWord += word[lenOfword-1]
        index += 1
        lenOfword -= 1
    newWord+="aca"
    return newWord
print(encrypt(word))
