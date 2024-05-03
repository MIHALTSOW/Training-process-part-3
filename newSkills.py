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
