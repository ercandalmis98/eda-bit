string = input("String:")
noOftimes = int(input("How many changes:"))
lst = []
tmpNo = noOftimes
i = 0
while noOftimes>0:
    x = input("Enter the {}. exchange:".format(i+1)).split()
    lst.append(x)
    noOftimes -= 1
    i += 1
while tmpNo>0:
    rule = str.maketrans(lst[i-1][1],lst[i-1][0])
    string = string.translate(rule)
    tmpNo -= 1
    i -= 1
print(lst)
print(string)
