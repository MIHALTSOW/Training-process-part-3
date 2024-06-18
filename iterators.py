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
