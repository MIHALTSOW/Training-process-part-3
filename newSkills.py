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


# numbers = list(map(int, input().split(' ')))
#
#
# def more_one_input(numbers):
#     result = {}
#     for i in sorted(numbers):
#         result[i] = result.get(i, 0) + 1
#     for k, v in result.items():
#         if v > 1:
#             print(k, end=' ')
#
#
# more_one_input(numbers)

# ore we can use lambda

# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda x: nums.count(x) > 1, set(nums))))


# this is my try

# def group_sum(num):
#     result = {}
#     keys = []
#     valus = []
#
#     # for i in range(1, num + 1):
#     #     if len(str(i)) == 1:
#     #         keys.append(i)
#     #     else:
#     #         valus.append(str(i))
#     for i in range(1, num + 1):
#         valus.append(str(i))
#         keys.append(str(i))
#         # keys.append(str(i))
#
#     if len(valus) == 0:
#         return 1
#     #
#     for j in keys:
#         for k in valus:
#             if j == sum(map(int, k)):
#                 result[j] = result.get(j, []) + [k]
#     return result
#     # for x in result.values():
#     #     print(len(x))


# codeium help
# def group_sum(num):
#     result = {}
#
#     for i in range(1, num + 1):
#         digits_sum = sum(map(int, str(i)))
#         if digits_sum in result:
#             result[digits_sum].append(str(i))
#         else:
#             result[digits_sum] = [str(i)]
#
#     mx = max(result.values(), key=len)
#     return len(mx)
#
#
# print(group_sum(1337))

# solution from answers

# data = {}
#
# for i in range(1, int(input()) + 1):
#     sum_of_digits = sum(map(lambda d: int(d), str(i)))
#     data[sum_of_digits] = data.get(sum_of_digits, 0) + 1
#
# print(max(data.values()))

# only code, without function
# n = int(input())
# languages = [input() for i in range(n)]
# result = {}
# total = []
#
# mn_len = min(languages, key=len)
#
# for k, j in enumerate(languages):
#     result[k] = j
#
# for i in mn_len.split(', '):
#     cnt = 0
#     for j in sorted(result.values()):
#         if i in j:
#             cnt += 1
#             if cnt == len(result):
#                 total.append(i)
#
# print(*sorted(total), sep=', ')


# implemented through function (реализовал через функцию)
# n = int(input())
# languages = [input() for i in range(n)]
#
#
# def all_languages(n, languages):
#     result = {}
#     total = []
#
#     mn_len = min(languages, key=len)
#
#     for k, j in enumerate(languages):
#         result[k] = j
#
#     for i in mn_len.split(', '):
#         cnt = 0
#         for j in sorted(result.values()):
#             if i in j:
#                 cnt += 1
#                 if cnt == len(result):
#                     total.append(i)
#
#     if len(total) == 0:
#         print('Сериал снять не удастся')
#
#     return print(*sorted(total), sep=', ')
#
#
# all_languages(n, languages)

# more faster solution


# this is my try

# main_word = 'машина'
# # main_word = 'весть'
# # main_word = 'внук'
# # n = int(input())
# # all_words = [input() for _ in range(n)]
# all_words = ['сеть', 'машинист', 'дорога', 'урок', 'работа', 'аксиома', 'железо', 'ветеран']
# # all_words = ['месть', 'гость', 'лань']
# # all_words = ['брат', 'дом', 'ворон', 'сват', 'обед']
#
#
# def only_vowel(main_word):
#     words = 'аеёиоуыэюя'
#
#     count_vowel = len([i for i in main_word if i in words])
#
#     pos_match = []
#     pos_main = []
#
#     for i in all_words:
#         cnt = 0
#         for j in i:
#             if j in words:
#                 cnt += 1
#         if cnt == count_vowel:
#             pos_match.append(i)
#
#     cnt = 0
#     for i in main_word:
#         cnt += 1
#         if i in words:
#             pos_main.append(cnt)
#
#     for k in pos_match:
#         cnt = 0
#         pos_words = []
#         for j in k:
#             cnt += 1
#             if j in words:
#                 pos_words.append(cnt)
#         if pos_main == pos_words:
#             print(k)
#
#     # print(pos_match)
#     # print(pos_main)
#     # print(pos_words)
#
#
# only_vowel(main_word)

# how complete teacher

# vowels = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
# pattern = [i for i, c in enumerate(input()) if c in vowels]
#
# for _ in range(int(input())):
#     word = input()
#     if [i for i, c in enumerate(word) if c in vowels] == pattern:
#         print(word)


# n1 = int(input())
# all_emails = [input() for _ in range(n1)]
#
# n2 = int(input())
# new_emails = [input() for _ in range(n2)]


# i tried this
# n1 = 6
# all_emails = ['ivan-petrov@beegeek.bzz', 'petr-ivanov@beegeek.bzz', 'ivan-petrov1@beegeek.bzz',
#               'ivan-ivanov@beegeek.bzz', 'ivan-ivanov1@beegeek.bzz', 'ivan-ivanov2@beegeek.bzz']
#
# n2 = 3
# new_emails = ['ivan-ivanov', 'petr-petrov', 'ivan-ivanov']
#
#
# def add_new(all_emails, new_emails):
#     all_email_names = [i.split('@')[0] for i in all_emails]
#
#
#     cnt_dict = {}
#     # print(all_emails)
#
#     for i in new_emails:
#         if i not in all_email_names:
#             all_email_names.append(i)
#             new_email = f'{i}@beegeek.bzz'
#         else:
#             if i in cnt_dict:
#                 cnt_dict[i] += 1
#             else:
#                 cnt_dict[i] = 1
#                 new_email = f'{i}{cnt_dict[i]}@beegeek.bzz'
#
#     print(new_email)
#
#
# add_new(all_emails, new_emails)
