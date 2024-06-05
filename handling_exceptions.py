# def swapcase_vowels(string):
#     vowels = 'aeiouy'
#     swapped_string = ''
#
#     for char in string:
#         if char in vowels:
#             swapped_string += char.upper()
#         else:
#             swapped_string += char
#
#     return swapped_string
#
#
# print(swapcase_vowels('hello world'))


# a = int(input())
# b = int(input())
#
# numbers = []
#
# for i in range(a, b + 1):
#     if int(i) % 7 == 0:
#         numbers.append(i)
#
# print(numbers)

# def get_max_index(numbers):
#     max_value = max(numbers)
#
#     for index, value in enumerate(numbers):
#         if value == max_value:
#             return index
#
#
# print(get_max_index([1, 2, 3, 4, 5, 10, 7, 8, 9, 10]))


# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
#               {'Likes': 13, 'Comments': 2, 'Shares': 1},
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
#               {'Comments': 4, 'Shares': 2},
#               {'Photos': 8, 'Comments': 1, 'Shares': 1},
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
#
# for post in blog_posts:
#     try:
#         total_likes += post['Likes']
#     except:
#         post['Likes'] = -1
#
# print(total_likes)

# my solution
# import sys
#
# input_person = [i for i in sys.stdin.read().split('\n') if i != '']
#
# cnt_sum = 0
# cnt_notDigit = 0
#
# for i in input_person:
#     if i.isdigit():
#         i = int(i)
#         cnt_sum += i
#     elif i.replace('.', '', 1).isdigit():
#         i = float(i)
#         cnt_sum += i
#     else:
#         cnt_notDigit += 1
#
# print(cnt_sum, cnt_notDigit, sep='\n')

# other solution
# import sys
#
# s, counter = 0, 0
#
# for line in sys.stdin:
#     try:
#         s += int(line)
#     except ValueError:
#         try:
#             s += float(line)
#         except ValueError:
#             counter += 1
#
# print(s, counter, sep='\n')

# n = input()
#
# month = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }
#
# try:
#     print(month[int(n)])
# except ValueError:
#     print("Введено некорректное значение")
# except KeyError:
#     print("Введено число из недопустимого диапазона")


# def add_to_list_in_dict(data, key, element):
#     if key in data:
#         data[key].append(element)
#     else:
#         data[key] = [element]
#     return data
#
#
# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'b', 7)
#
# print(data)

# try:
#     with open(input(), 'r', encoding='utf-8') as file:
#         for line in file:
#             print(line)
# except:
#     print('Файл не найден')

# def get_weekday(number):
#     if not isinstance(number, int):
#         raise TypeError('Аргумент не является целым числом')
#     if number not in range(1, 8):
#         raise ValueError('Аргумент не принадлежит требуемому диапазону')
#
# print(get_weekday(6))


# def is_good_password(string):
#     flag = False
#     if len(string) >= 9 and any(char.isdigit() for char in string) and any(char.isupper() for char in string) and any(
#             char.islower() for char in string):
#         flag = True
#     return flag
#
#
# print(is_good_password('41157082'))
# print(is_good_password('мойпарольсамыйлучший'))
# print(is_good_password('МойПарольСамыйЛучший111'))


# class LengthError(Exception):
#     pass
#
#
# class LetterError(Exception):
#     pass
#
#
# class DigitError(Exception):
#     pass
#
#
# def is_good_password(string):
#     try:
#         if len(string) < 9:
#             raise LengthError
#         if not any(char.islower() for char in string) or not any(char.isupper() for char in string):
#             raise LetterError
#         if not any(char.isdigit() for char in string):
#             raise DigitError
#         return True
#     except LengthError as e:
#         raise
#     except LetterError as e:
#         raise e
#     except DigitError as e:
#         raise e
#
#
# print(is_good_password('41157082'))
# print(is_good_password('мойпарольсамыйлучший'))
# print(is_good_password('МойПарольСамыйЛучший111'))


