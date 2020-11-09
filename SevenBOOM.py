lst = [1,2,3,4,5,788]
def seven_boom(lst):
    result = False
    for i in range(len(lst)):
        if result is True:
            break
        tmp = lst[i]
        while tmp>0:
            if tmp%10 == 7:
                result = True
                break
            tmp = int(tmp / 10)
    if result is True:
        return "BOOM!"
    else:
        return "there is no 7 in the list" 
print(seven_boom(lst))