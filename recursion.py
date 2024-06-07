# def traffic(n):
#     while n > 0:
#         print('Не парковаться')
#         n -= 1

# def traffic(n):
#     if n > 0:
#         print("Не парковаться")
#         traffic(n - 1)
#
#
# traffic(0)

# def digits_from_1_to_100(n=1):
#     if n <= 100:
#         print(n)
#         digits_from_1_to_100(n + 1)
#
#
# digits_from_1_to_100()


# def func(start, end):
#     if start <= end:
#         print(start)
#         func(start + 1, end)
#
# func(1, 100)


# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341,
#            437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331,
#            323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
#            984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777,
#            805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]


# def cycle(n, position=0):
#     print(f"Элемент {position}: {n[position]}")
#     if position < len(n):
#         cycle(n, position + 1)
#
#
# cycle(numbers)
#
#
# def cycle(n, position=0):
#     try:
#         print(f"Элемент {position}: {n[position]}")
#         cycle(n, position + 1)
#     except IndexError:
#         return

# def func(seq, start, end):
#     if start <= end:
#         print('Элемент {}: {}'.format(start, seq[start]))
#         func(seq, start + 1, end)
#
#
# func(numbers, 0, 99)

# def list_elements():
#     def output(n=0):
#         if n < len(numbers):
#             print(f'Элемент {n}: {numbers[n]}')
#             output(n + 1)
#
#     output()
#
#
# list_elements()

# def relative_difference(a, b):
#     for i in range(len(a)):
#         a1 = a[i]
#         b1 = b[i]
#         print(((a1 - b1) / a1) * 100)
#
#
# a = [1, 0.7, 1.1, 1.3, 0.6]
# b = [0.775, 0.531, 0.531, 0.531, 0.531]
#
# relative_difference(a, b)

# import sys
#
# nums = [int(digit) for digit in sys.stdin if int(digit) == 0 break]

#
# def reverse_nums(digits):
#     if len(digits) > 0:
#         print(digits[-1])
#         reverse_nums(digits[:-1])
#
#
# reverse_nums(nums)

# def recursion():
#     digit = int(input())
#     if digit != 0:
#         recursion()
#     print(digit)
#
# recursion()

# def triangle(h):
#     if h > 0:
#         print("*" * h)
#         triangle(h - 1)
#
#
# triangle(3)

# def hourglass(n=16, digit=1):
#     if n > 4:
#         print((str(digit) * n).center(16))
#         hourglass(n - 4, digit + 1)
#     print((str(digit) * n).center(16))
#
#
# hourglass()

# def print_digits(number):
#     number = str(number)
#     if len(number) > 0:
#         print(int(number[-1]))
#         if len(number) > 1:
#             print_digits(int(number[:-1]))
#
#
# print_digits(12345)
# print()
# print_digits(7)

# def print_digits(number):
#     number = str(number)
#     if len(number) > 0:
#         if len(number) > 1:
#             print_digits(int(number[:-1]))
#         print(int(number[-1]))
#
#
# print_digits(12345)
# print()
# print_digits(2077)

# def fib(n):
#     cache = {1: 1, 2: 1}
#
#     def fib_rec(n):
#         result = cache.get(n)
#         if result is None:
#             result = fib_rec(n - 2) + fib_rec(n - 1)
#             cache[n] = result
#         return result
#
#     return fib_rec(n)

# def cnt_digits(n):
#     if n == 0:
#         return 0
#     return 1 + cnt_digits(n // 10)
#
# print(cnt_digits(5))

# print(20 // 10)

# def sum_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_digits(n // 10)


# def number_of_frogs(year):
#     if year == 1:
#         return 77
#     return 3 * (number_of_frogs(year - 1) - 30)


# def range_sum(numbers, start, end):
#     if start == end:
#         return numbers[start]
#     return numbers[start] + range_sum(numbers, start + 1, end)


# def get_pow(a, n):
#     if n == 0:
#         return 1
#     return a * get_pow(a, n - 1)
#
#
# print(get_pow(5, 2))


# def get_fast_pow(a, n):
#     if n == 0:
#         return 1
#     if n % 2 == 0:
#         return get_fast_pow(a * a, n // 2)
#     return get_fast_pow(a, n - 1) * a

# def recursive_sum(a, b):
#     if b == 0:
#         return a
#     return recursive_sum(a + 1, b - 1)

# def is_power(number):
#     if number == 1:
#         return True
#     if number % 2 == 1:
#         return False
#     return is_power(number // 2)

# def is_palindrome(string):
#     if len(string) <= 1:
#         return True
#     if string[0] == string[-1]:
#         return is_palindrome(string[1:-1])
#     return False
#
# print(is_palindrome('stepik'))
# print(is_palindrome('level'))


# def to_binary(number):
#     if number == 0:
#         return 0
#     return number % 2 + 10 * to_binary(number // 2)


# from sys import getrecursionlimit
#
# limit = getrecursionlimit()
#
# print(limit)

# def recursive_sum(nested_lists):
#     if not nested_lists:
#         return 0
#     if isinstance(nested_lists[0], list):
#         return recursive_sum(nested_lists[0]) + recursive_sum(nested_lists[1:])
#     return nested_lists[0] + recursive_sum(nested_lists[1:])


# def linear(nested_lists):
#     result = []
#     for item in nested_lists:
#         if isinstance(item, list):
#             result.extend(linear(item))
#         else:
#             result.append(item)
#     return result
#
#
# my_list = [3, [4], [5, [6, [7, 8]]]]
#
# print(linear(my_list))

# def get_value(nested_dicts, key):
#     if isinstance(nested_dicts, dict):
#         if key in nested_dicts:
#             return nested_dicts[key]
#         for value in nested_dicts.values():
#             result = get_value(value, key)
#             if result is not None:
#                 return result
#
#
# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993},
#         'address': {'streetAddress': 'Часовая 25, кв. 127',
#                     'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'},
#                     'postalCode': '125315'}}
#
# print(get_value(data, 'cityName'))
