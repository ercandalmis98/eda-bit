def atbash(txt):
    alphabetUpper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetLower ="abcdefghijklmnopqrstuvwxyz" 
    index = 0 
    no = len(txt)
    newTxt = ""
    while no>0:
        if txt[index].isupper():
            newTxt += alphabetUpper[abs(int(alphabetUpper.find(txt[index])) - 25)]
        elif txt[index].islower():
            newTxt += alphabetLower[abs(int(alphabetLower.find(txt[index])) - 25)]
        else:
            newTxt += txt[index]
        index += 1
        no -= 1
    return newTxt 
print(atbash("Erc56an"))
