def addNumber(a,b):
    total=0
    total = a+b
    return total

print(addNumber(3,4))

def sumList(*num):
    total=0
    for i in num:
        total = total + i
    return total

print(sumList(1,2,3,4,5,6,7,8,9,10))