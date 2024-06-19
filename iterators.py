# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88,
#            -11, 16, -22]
#
# it = iter(reversed(numbers))
#
# print(next(it))


# def filterfalse(predicate, iterable):
#     if predicate is None:
#         predicate = bool
#     return filter(lambda x: not predicate(x), iterable)
#
#
# objects = [0, 1, True, False, 17, []]
# print(*filterfalse(None, objects))


# def simple_sequence():
#     num = 1
#     while True:
#         for _ in range(num):
#             yield num
#         num += 1


# generator = simple_sequence()
#
# print(next(generator))
# print(next(generator))

# generator = simple_sequence()
# numbers = [next(generator) for _ in range(10)]
#
# print(*numbers)


# def alternating_sequence(count: int = None) -> list[int]:
#     num = 1
#     current_count = 0
#     while count is None or current_count < count:
#         yield num
#         current_count += 1
#         if num > 0:
#             num = -num - 1
#         else:
#             num = abs(num) + 1
#
# generator = alternating_sequence()
#
# print(next(generator))
# print(next(generator))


# def primes(left, right):
#     for num in range(left, right + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 yield num
#
#
# generator = primes(1, 15)
#
# print(*generator)

# def reverse(sequence):
#     for i in range(len(sequence) - 1, -1, -1):
#         yield sequence[i]
#
#
# print(*reverse([1, 2, 3, 4, 5]))

# from datetime import date, timedelta
#
#
# def dates(start: date, count: int = None):
#     current = start
#     if count is None:
#         try:
#             while True:
#                 yield current
#                 current = current + timedelta(days=1)
#         except OverflowError:
#             print(f"ошибка OverflowError: {current}")
#     else:
#         for _ in range(count):
#             yield current
#             current += timedelta(days=1)
#
#
# # TEST_1:
# generator = dates(date(2022, 3, 8))
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # TEST_2:
# generator = dates(date(2022, 3, 8), 5)
#
# print(*generator)
#

# # TEST_5:
# generator = dates(date(2049, 1, 7))
#
# for _ in range(10_000):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


# def card_deck(suit: str):
#     suits = ["пик", "треф", "бубен", "червей"]
#     values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
#     suit_index = suits.index(suit)
#     for value in values:
#         for s in suits:
#             if s != suit:
#                 yield f"{value} {s}"
#         if suits[-1] != suit:
#             yield f"{value} {suits[suit_index]}"
#
#
# generator = card_deck('пик')
#
# print(next(generator))
# print(next(generator))
# print(next(generator))

# def matrix_by_elem(matrix):
#     for row in matrix:
#         yield from row
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(*matrix_by_elem(matrix))

# def palindromes():
#     for i in range(1, 10000000):
#         try:
#             if str(i) == str(i)[::-1]:
#                 yield i
#         except StopIteration:
#             break

# from itertools import count
#
#
# def palindromes():
#     yield from (i for i in count(1) if str(i) == str(i)[::-1])

# def palindromes():
#     count = 1
#     while True:
#         if str(count) == str(count)[::-1]:
#             yield count
#         count += 1


# generator = palindromes()
#
# print(next(generator))
# print(next(generator))
# print(next(generator))

# generator = palindromes()
# numbers = [next(generator) for _ in range(30)]
#
# print(*numbers)

# generator = palindromes()
#
# for _ in range(10_000):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# def flatten(nested_list):
#     for item in nested_list:
#         if isinstance(item, list):
#             yield from flatten(item)
#         else:
#             yield item
#
#
# generator = flatten([[1, 2], [[3]], [[4], 5]])
#
# print(*generator)

# def cubes_of_odds(iterable):
#     return (number ** 3 for number in iterable if number % 2)
#
#
# print(type(cubes_of_odds([1, 2, 3, 4, 5])))

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True


# def is_prime(number: int) -> bool:
#     return number != 1 and all(number % i != 0 for i in range(2, number))


# print(is_prime(1))
# print(is_prime(8))
# print(is_prime(7))


# def count_iterable(iterable):
# count = 0
# for _ in iterable:
#     count += 1
# return count
# return sum(1 for _ in iterable)

# print(count_iterable([1, 2, 3, 4, 5]))

# def all_together(*args):
#     # for arg in args:
#     #     yield from arg
#     return (item for arg in args for item in arg)
#
# objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
#
# print(*all_together(*objects))


# def interleave(*iterables):
#     # for i in zip(*iterables):
#     #     yield from i
#     return (item for i in zip(*iterables) for item in i)


# print(*interleave('bee', '123'))


# from collections import namedtuple

# Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

# persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
#            Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
#            Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
#            Person('Genevieve Asse', 'French', 'female', 1949, 0),
#            Person('Irene Adler', 'Swedish', 'female', 2005, 0),
#            Person('Sergio Asti', 'Italian', 'male', 1926, 0),
#            Person('Olof Backman', 'Swedish', 'male', 1999, 0),
#            Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
#            Person('Dana Atchley', 'American', 'female', 1941, 2000),
#            Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
#            Person('Shura_Stone', 'Russian', 'male', 2000, 0),
#            Person('Jon Bale', 'Swedish', 'male', 2000, 0)]

# alive = (person for person in persons if person.death == 0)
# fromSwedish = (person for person in alive if person.nationality == 'Swedish')
# male = (person for person in fromSwedish if person.sex == 'male')
# most_young = max(male, key=lambda person: person.birth).name

# print(most_young)


# def parse_ranges(s):
#     for part in s.split(','):
#         if '-' in part:
#             start, end = part.split('-')
#             yield from range(int(start), int(end) + 1)
#         else:
#             yield int(part)
#
#
# print(*parse_ranges('1-2,4-4,8-10'))

# def filter_names(names, ignore_char, max_names):
#     start_ignore_char = (name for name in names if name[0].upper() != ignore_char.upper())
#     not_digits = (name for name in start_ignore_char if all(char.isalpha() for char in name))
#
#     if max_names > len(names):
#         return list(not_digits)
#     else:
#         return not_digits


# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
#
# print(*filter_names(data, 'D', 3))

# import csv
#
# with open('data.csv', encoding='utf-8') as file:
#
#     header = next(file)
#     file_info = csv.reader(file)
#
#     sum_only_a = sum(int(row[1]) for row in file_info if row[2] == 'a')
#
#     print(sum_only_a)

# from datetime import datetime, timedelta
#
#
# def years_days(year):
#     start_date = datetime(year, 1, 1)
#     end_date = datetime(year + 1, 1, 1)
#     while start_date < end_date:
#         yield start_date.strftime('%Y-%m-%d')
#         start_date += timedelta(days=1)
#
#
# dates = years_days(2022)
#
# print(next(dates))
# print(next(dates))
# print(next(dates))
# print(next(dates))

# def unique(iterable):
#     seen = set()
#     for item in iterable:
#         if item not in seen:
#             yield item
#             seen.add(item)

# def unique(iterable):
#     yield from (dict.fromkeys(numbers))
#
#
# numbers = [1, 2, 2, 3, 4, 5, 5, 5]
#
# print(*unique(numbers))

#
# def stop_on(iterable, value):
#     for item in iterable:
#         if item == value:
#             break
#         yield item
#
#
# numbers = [1, 2, 3, 4, 5]
#
# print(*stop_on(numbers, 4))

# def with_previous(iterable):
#     prev = None
#     for item in iterable:
#         yield item, prev
#         prev = item
#
# numbers = [1, 2, 3, 4, 5]
#
# print(*with_previous(numbers))

# def pairwise(iterable):
#     prev = None
#     for item in iterable:
#         if prev is not None:
#             yield prev, item
#         prev = item
#     yield prev, None
#
# numbers = [1, 2, 3, 4, 5]
#
# print(*pairwise(numbers))
#
# # Sample Output 1:
# # (1, 2) (2, 3) (3, 4) (4, 5) (5, None)

# def around(iterable):
#     prev = None
#     for item in iterable:
#         if prev is not None:
#             yield prev, item
#         prev = item
#     yield prev, None
#
#
# numbers = [1, 2, 3, 4, 5]
#
# print(*around(numbers))

# def is_iterable(obj):
#     try:
#         iter(obj)
#         return True
#     except TypeError:
#         return False
#
#
# print(is_iterable(18731))

# def is_iterator(obj):
#     try:
#         next(obj)
#         return True
#     except StopIteration:
#         return False
#
#
# print(is_iterator([1, 2, 3, 4, 5]))
#
# beegeek = map(str.upper, 'beegeek')
#
# print(is_iterator(beegeek))

# from itertools import count


# def tabulate(func):
#     count = 1
#     while True:
#         yield func(count)
#         count += 1

# def tabulate(func):
#     for i in count(1):
#         yield func(i)
#
#
# func = lambda x: x
# values = tabulate(func)
#
# print(next(values))
# print(next(values))


# def factorials(n):
#     for i in count(1):
#         yield i
#         if i == n:
#             break

# KILL THE PC
# from itertools import accumulate, count
#
#
# def factorials(n):
#     return accumulate(count(1), lambda x, y: x * y, initial=1)
#
#
# numbers = factorials(6)
#
# print(*numbers)

# from itertools import count, accumulate
#
#
# def factorials(n):
#     return accumulate([i for i in range(1, n + 1)], lambda x, y: x * y)
#
#
# numbers = factorials(6)
#
# print(*numbers)
# from itertools import cycle
# from string import ascii_uppercase
#
#
# def alnum_sequence():
#     letters = ascii_uppercase
#     digits = (digit for digit in range(1, 27))
#     words = (word for word in letters)
#     for digit, word in cycle(zip(digits, words)):
#         yield f"{digit}"
#         yield f"{word}"
#
#
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(55)))
#
#
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(100)))

# from itertools import dropwhile
#
#
# def drop_while_negative(iterable):
#     return dropwhile(lambda x: x < 0, iterable)
#
#
# numbers = [-3, -2, -1, 0, 1, 2, 3]
#
# print(*drop_while_negative(numbers))

# from itertools import takewhile, dropwhile
#
#
# def drop_this(iterable, obj):
#     return dropwhile(lambda x: x == obj, iterable)
#
#
# numbers = [0, 0, 0, 1, 2, 3]
#
# print(*drop_this(numbers, 0))

# from itertools import islice
#
#
# def take(iterable, n):
#     return islice(iterable, n)
#
#
# print(*take(range(10), 5))
#
# iterator = iter('beegeek')
#
# print(*take(iterator, 22))

# from itertools import islice
#
#
# def take_nth(iterable, n):
#     return next(islice(iterable, n - 1, n), None)
#
#
# numbers = [11, 22, 33, 44, 55]
#
# print(take_nth(numbers, 3))
#
# iterator = iter('beegeek')
#
# print(take_nth(iterator, 4))
#
# iterator = iter('beegeek')
#
# print(take_nth(iterator, 10))

# from itertools import accumulate, chain
#
#
# def sum_of_digits(iterable):
#     str_digits = chain.from_iterable(map(str, iterable))
#     return sum(int(digit) for digit in str_digits)
#
#
# print(sum_of_digits([13, 20, 41, 2, 2, 5]))


# def is_rising(iterable):
#     prev = None
#     for item in iterable:
#         if prev is not None and prev >= item:
#             return False
#         prev = item
#     return True
#
# print(is_rising([1, 2, 3, 4, 5]))
#
# iterator = iter([1, 1, 1, 2, 3, 4])
#
# print(is_rising(iterator))
#
# iterator = iter(list(range(100, 200)))
#
# print(is_rising(iterator))

# def max_pair(iterable):
#     max_sum = float('-inf')
#     for i in range(1, len(iterable)):
#         max_sum = max(max_sum, iterable[i-1] + iterable[i])
#     return max_sum
#
#
# print(max_pair([1, 8, 2, 4, 3]))
# iterator = iter([1, 2, 3, 4, 5])
#
# print(max_pair(iterator))
# iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
#
# print(max_pair(iterator))

# from collections import namedtuple
# from itertools import groupby
#
# Person = namedtuple('Person', ['name', 'age', 'height'])
#
# persons = [
#     Person('Tim', 63, 193),
#     Person('Eva', 47, 158),
#     Person('Mark', 71, 172),
#     Person('Alex', 45, 193),
#     Person('Jeff', 63, 193),
#     Person('Ryan', 41, 184),
#     Person('Ariana', 28, 158),
#     Person('Liam', 69, 193)
# ]
#
#
# persons.sort(key=lambda x: x.height)
#
# for height, group in groupby(persons, key=lambda x: x.height):
#     names = ', '.join(sorted(person.name for person in group))
#     print(f"{height}: {names}")

# from collections import namedtuple
# from itertools import groupby
#
#
# Student = namedtuple('Student', ['surname', 'name', 'grade'])
#
# students = [
#     Student('Гагиев', 'Александр', 10),
#     Student('Дедегкаев', 'Илья', 11),
#     Student('Кодзаев', 'Георгий', 10),
#     Student('Набокова', 'Алиса', 11),
#     Student('Кораев', 'Артур', 10),
#     Student('Шилин', 'Александр', 11),
#     Student('Уртаева', 'Илина', 11),
#     Student('Салбиев', 'Максим', 10),
#     Student('Капустин', 'Илья', 11),
#     Student('Гудцев', 'Таймураз', 11),
#     Student('Перчиков', 'Максим', 10),
#     Student('Чен', 'Илья', 11),
#     Student('Елькина', 'Мария', 11),
#     Student('Макоев', 'Руслан', 11),
#     Student('Албегов', 'Хетаг', 11),
#     Student('Щербак', 'Илья', 10),
#     Student('Идрисов', 'Баграт', 11),
#     Student('Гапбаев', 'Герман', 10),
#     Student('Цивинская', 'Анна', 10),
#     Student('Туткевич', 'Юрий', 11),
#     Student('Мусиков', 'Андраник', 11),
#     Student('Гадзиев', 'Георгий', 11),
#     Student('Белов', 'Юрий', 11),
#     Student('Акоева', 'Диана', 11),
#     Student('Денисов', 'Илья', 11),
#     Student('Букулова', 'Диана', 10),
#     Student('Акоева', 'Лера', 11)
# ]
#
#
# sorted_students_name = max(groupby(sorted(students, key=lambda x: x.name), key=lambda x: x.name), key=lambda x: len(list(x[1])))
#
# print(sorted_students_name[0])
#

# from collections import defaultdict
#
#
# def group_words(iterable):
#     dict_words = defaultdict(list)
#
#     for i in iterable:
#         dict_words[len(i)].append(i)
#
#     for key, value in sorted(dict_words.items()):
#         yield f"{key} -> {value}"
#
#
# word = ['hi', 'never', 'here', 'my', 'blue']
#
# for lens, group in group_words(word):
#     print(lens, *group)

# from itertools import groupby
#
# words = input().split()
#
# groups = {}
# sorted_words = sorted(words, key=len)
# for length, group in groupby(sorted_words, key=len):
#     groups[length] = sorted(list(group))
#
# for length, words in sorted(groups.items()):
#     words_list = ', '.join(words)
#     print(f"{length} -> {words_list}")

# from itertools import permutations

# string = input()
# unique_permutations = set(permutations(string))
#
# for perm in sorted(unique_permutations):
#     print(''.join(perm))
#
# for tpl in sorted(set(permutations(input()))):
#     print(''.join(tpl))

