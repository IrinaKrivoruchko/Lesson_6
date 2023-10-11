# import random
# while True:
#     try:
#         NUM_SIZE = int(input("Enter size of list: "))
#         if NUM_SIZE > 0:
#             break
#         if NUM_SIZE <= 0:
#             print("You should to enter number more then 0")
#     except ValueError:
#         print("Enter only integer numbers please!")
#
# numbers = []
# for num in range(NUM_SIZE):
#     numbers.append(random.randint(1, 100))
#
# print(numbers)

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
# def counter_of_prime_numbers(num):
#     counter = 0
#     for number in num:
#         if number < 2:
#             continue
#
#         is_simple = True
#
#         for i in range(2, number):
#              if number % i == 0:
#                 is_simple = False
#                 break
#         if is_simple:
#             counter += 1
#
#     return counter
# print(f"The number of primes in a list: {counter_of_prime_numbers(numbers)}")

#4
# list_for_del = [1, 2, 3, 4, 5, 6, 7, 1, 4]
# def del_element_in_list(num):
#     counter_del = 0
#     for_del = 4
#     for x in num:
#         if x == for_del:
#             counter_del += 1
#
#     if counter_del != 0:
#         num.remove(for_del)
#
#     return counter_del
#
# if del_element_in_list(list_for_del) != 0:
#     print(f"Counter of deleted elements: {del_element_in_list(list_for_del)}")
# else:
#     print("Nothing found")

#5
first_list = [12, 3, 4, 5, 6, 8, 4, 3, 66, 1]
second_list = [1, 2, 3, 6, 4, 7, 8, 10, 55]
# second_list = [0, 0, 0]

def search_of_common(list1, list2):
    common = set(first_list).intersection(second_list)
    return common

if len(search_of_common(first_list, second_list)) != 0:
    print(f"Some common: {search_of_common(first_list, second_list)}")
else:
    print("Nothing found")