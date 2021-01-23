userInput = int(input("Enter the Number: "))

factorial = 1

if userInput < 0:
    print("Invalid")
elif userInput == 0:
    print("0")
else:
    for i in range(1, userInput+1):
        factorial = factorial * i
    print(factorial)        