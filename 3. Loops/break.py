listNumber = [1,2,3,4,5,6,7,8,9,10]

userInput = int(input("Enter the user input: "))

for i in listNumber:
    if i == userInput:
        print("Match Found!")
        break;
else:
    print("No Match Found!")

print("Hey! I am out of the for loop.")

for l in "Hello":
    if l == 'l':
        break
    print("Value is ", l)

