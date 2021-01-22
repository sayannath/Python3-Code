import random

print(random.choice(range(100)))
print(random.choice([1,2,3,4,5,6]))

print(random.randrange(1,100, 1))

listNumber = [1,2,3,4,5,6]
random.shuffle(listNumber)
print(listNumber)

print(random.random())

random.seed(10)
print(random.random())
