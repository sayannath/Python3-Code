userInput = int(input("Enter the Number: "))

if userInput > 1:
    for i in range(2, userInput):
        if userInput % i == 0:
            print("Not a Prime Number!")
            break
        else:
            print("It is a prime Number!")
            break
else:
    print("Not a Prime Number!")      