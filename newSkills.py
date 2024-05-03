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


