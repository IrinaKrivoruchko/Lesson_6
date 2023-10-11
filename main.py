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
    numbers.append(random.randint(1, 100))

print(numbers)

#1
# def multiplication_list(num) -> int:
#     res_multi = 1
#     for i in num:
#         res_multi *= i
#     return res_multi
#
# print(f"Result of multiplication: {multiplication_list(numbers)}")

#2
# def find_min(num_min) -> int:
#     return min(num_min)
#
# print(f"Minimum in the list: {find_min(numbers)}")

#3
def counter_of_prime_numbers(num):
    counter = 0
    for number in num:
        if number < 2:
            continue

        is_simple = True

        for i in range(2, number):
             if number % i == 0:
                is_simple = False
                break
        if is_simple:
            counter += 1

    return counter
print(f"The number of primes in a list: {counter_of_prime_numbers(numbers)}")