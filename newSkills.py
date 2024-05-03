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
