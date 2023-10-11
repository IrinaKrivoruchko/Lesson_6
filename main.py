import random
while True:
    try:
        NUM_SIZE = int(input("Enter size of list: "))
        if NUM_SIZE > 0:
            break
        if NUM_SIZE <= 0:
            print("You should to enter number more then 0")
    except ValueError:
        print("Enter only integer numbers please!")

numbers = []
for num in range(NUM_SIZE):
    numbers.append(random.randint(-100, 100))

print(numbers)

