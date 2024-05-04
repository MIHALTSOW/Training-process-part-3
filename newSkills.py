# Part 2.1
# def hide_card(card_number):
#     card_number = card_number.replace(' ', '')
#     hidden_number = ''
#     for idx, digit in enumerate(card_number):
#         if idx < 12:
#             hidden_number += '*'
#         else:
#             hidden_number += digit
#     return hidden_number
#
#
# print(hide_card(input()))
#
#
# # more comfortable solution
# def hide_card(card_number):
#     return '*' * 12 + card_number.replace(' ', '')[-4:]


# def same_parity(numbers):
#     total = []
#     if len(numbers) == 0:
#         return []
#     elif numbers[0] % 2 == 0:
#         for i in numbers:
#             if i % 2 == 0:
#                 total.append(i)
#     else:
#         for j in numbers:
#             if j % 2 != 0:
#                 total.append(j)
#     return total
#
#
# print(same_parity([-1, 1248234832443, 8]))

# more comfortable solution

# def same_parity(nums):
#     return [i for i in nums if i % 2 == nums[0] % 2]


# and more

# def same_parity(numbers):
#     return list(filter(lambda x: x % 2 == numbers[0] % 2))


# def is_valid(pin_code):
#     if 4 <= len(pin_code) <= 6 and all(i in '0123456789' and i != ' ' for i in pin_code):
#         return True
#     return False
#
#
# print(is_valid('89abc1'))

# more faster solution

# def is_valid(pin):
#     return pin.isdigit() and len(pin) in (4, 5, 6)


# def print_given(*args, **kwargs):
#     for i in args:
#         print(i, type(i))
#     for k, v in sorted(kwargs.items()):
#         print(k, v, type(v))
#
#
# print_given()


# def convert(string):
#     if len(list(filter(lambda x: x.isupper(), string))) > len(list(filter(lambda x: x.islower(), string))):
#         return string.upper()
#     if len(list(filter(lambda x: x.isupper(), string))) == len(list(filter(lambda x: x.islower(), string))):
#         return string.lower()
#     else:
#         return string.lower()
#
#
# print(convert('pi31415!'))


# more comfortable solution

# def convert(text):
#     lower_count = len(list(filter(str.islower, text)))
#     upper_count = len(list(filter(str.isupper, text)))
#     if lower_count >= upper_count:
#         return text.lower()
#     return text.upper()
#
#
# print(convert('BEEgeek'))


# def filter_anagrams(word, words):
#     dict_word = {}
#     for k in word:
#         dict_word[k] = dict_word.get(k, 0) + 1
#
#     result = []
#
#     for i in words:
#         dict_words = {}
#         for j in i:
#             dict_words[j] = dict_words.get(j, 0) + 1
#
#         if dict_word == dict_words:
#             result.append(i)
#
#     return result
#
#
# word = 'abba'
# anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
#
# print(filter_anagrams(word, anagrams))


# more-more-more comfortable solution

# def filter_anagrams(word, anagrams):
#     return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]
#
#
# word = 'abba'
# anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
#
# print(filter_anagrams(word, anagrams))


# def likes(names):
#     if len(names) == 0:
#         return 'Никто не оценил данную запись'
#     elif len(names) == 1:
#         return f'{names[0]} оценил(a) данную запись'
#     elif len(names) == 2:
#         return f'{names[0]} и {names[1]} оценили данную запись'
#     elif len(names) == 3:
#         return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
#     return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'
#
#
# print(likes(['Том']))


# def index_of_nearest(numbers, number):
#     if len(numbers) == 0:
#         return -1
#     else:
#         mn = [abs(i - number) for i in numbers]
#         return mn.index(min(mn))
#
#
# print(index_of_nearest([9, 5, 3, 2, 11], 4))


# another solution

# def index_of_nearest(nums, n):
#     if nums:
#         minimum = min(nums, key=lambda num: abs(num - n))
#         return nums.index(minimum)
#     return -1
#
#
# print(index_of_nearest([7, 5, 4, 4, 3], 4))


# def spell(*args):
#     fist_word_long_word = {}
#     for i in args:
#         fist_word_long_word[i[0].lower()] = max(fist_word_long_word.get(i[0].lower(), 0), len(i))
#     return fist_word_long_word
#
#
# print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

# d1 - first shop
# d2 - second shop
# d3 - distance between shops

# def minimum_distance(d1, d2, d3):
#     first_way = d1 + d3 + d2
#     second_way = d2 + d3 + d1
#     third_way = (d1 + d1) + (d2 + d2)
#     forth_way = d2 + d3 + d3 + d2
#     five_way = d1 + d3 + d3 + d1
#     return min(first_way, second_way, third_way, forth_way, five_way)
#
#
# print(minimum_distance(100, 33, 34))

# more faster solution

# d1, d2, d3 = [int(input()) for _ in range(3)]
#
# print(min(d1 + d2 + d3, 2 * (d1 + d2), 2 * (d1 + d3), 2 * (d2 + d3)))


# def find_word_language(word1, word2, word3):
#     alphabet = []
#     alphabet.append(word1)
#     alphabet.append(word2)
#     alphabet.append(word3)
#     if all(i in 'AaBCcEeHKMOoPpTXxy' for i in alphabet):
#         return 'en'
#     if all(i in 'АаВСсЕеНКМОоРрТХху' for i in alphabet):
#         return 'ru'
#     else:
#         return 'mix'
#
#
# print(find_word_language('a', 'B', 'c'))

# more fuster solution

# langs = ['ru', 'mix', 'mix', 'en']
# eng = 'AaBCcEeHKMOoPpTXxy'
# ind = sum(input() in eng for _ in range(3))
# print(langs[ind])

# and another one, more prefer solution

# letters = [input() for _ in range(3)]
# if all(map(lambda x: x in 'AaBCcEeHKMOoPpTXxy', letters)):
#     print('en')
# elif all(map(lambda x: x in 'АаВСсЕеНКМОоРрТХху', letters)):
#     print('ru')
# else:
#     print('mix')


# do counter
# cnt = 0
# push = input()
# while push == (''
#                ''):
#     cnt += 1
#     print(cnt)
#     push = input()


# n = list(map(int, input().split(' ')))
#
# def change_words(n=9, x=3, y=6, A=5, B=8):
#     all_digits = [i for i in range(1, n + 1)]
#     rev_xy = list(reversed(all_digits[x - 1:y]))
#     all_digits = all_digits[:x - 1] + rev_xy + all_digits[y:]
#     rev_ab = list(reversed(all_digits[A - 1:B]))
#     all_digits = all_digits[:A - 1] + rev_ab + all_digits[B:]
#     return all_digits
#
#
# print(*change_words(n[0], n[1], n[2], n[3], n[4]))

# or more faster solution
# n, x, y, a, b = [int(i) for i in input().split()]
# nums = list(range(1, n + 1))
#
# nums[x - 1:y] = reversed(nums[x - 1:y])
# nums[a - 1:b] = reversed(nums[a - 1:b])
#
# print(*nums)
