# teacher solution

# from string import ascii_letters
#
# translator = str.maketrans(ascii_letters, input() * 2)
#
# print(input().translate(translator))

# my solution

# new = input() * 2
# old = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# translation_table = str.maketrans(old, new)
# original_string = input()
#
# print(original_string.translate(translation_table))


# from collections import namedtuple
#
# Fruit = namedtuple('Fruit', 'name color vitamins')
#
# juse = Fruit('apple', 'red', ['calories', 'sugar'])
#
# print(juse)
#
# print(type(juse))


# from collections import namedtuple
#
# Game = namedtuple('Game', 'name developer publisher')
#
# ExtendedGame = namedtuple('ExtendedGame', Game._fields + ('release_date', 'price'))
#
# print(ExtendedGame)

# import pickle
# from collections import namedtuple
#
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
#
# with open('data.pkl', 'rb') as file:
#     data = pickle.load(file)
#     print(len(data))
#
#     cnt = 0
#     for name, family, sex, color in data:
#         cnt += 1
#         print(f"name: {name}")
#         print(f"family: {family}")
#         print(f"sex: {sex}")
#         print(f"color: {color}")
#         if cnt != 13:
#             print()

# second solution
# for animal in data:
#     animal_dict = animal._asdict()
#     for key, value in animal_dict.items():
#         print(f"{key}: {value}")
#     print()


# my solution
# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [
#     User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#     User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#     User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#     User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#     User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#     User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#     User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#     User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#     User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#     User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#     User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#     User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#     User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#     User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#     User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')
# ]
#
# sort_user_name = sorted(users, key=lambda user: user.email)
#
# gold = [user for user in sort_user_name if user.plan == 'Gold']
# silver = [user for user in sort_user_name if user.plan == 'Silver']
# bronze = [user for user in sort_user_name if user.plan == 'Bronze']
# basic = [user for user in sort_user_name if user.plan == 'Basic']
#
# for name, surname, email, plan in gold:
#     print(f"{name} {surname}")
#     print(f"  Email: {email}")
#     print(f"  Plan: {plan}")
#     print()
#
# for name, surname, email, plan in silver:
#     print(f"{name} {surname}")
#     print(f"  Email: {email}")
#     print(f"  Plan: {plan}")
#     print()
#
# for name, surname, email, plan in bronze:
#     print(f"{name} {surname}")
#     print(f"  Email: {email}")
#     print(f"  Plan: {plan}")
#     print()
#
# cnt = 0
# for name, surname, email, plan in basic:
#     cnt += 1
#     print(f"{name} {surname}")
#     print(f"  Email: {email}")
#     print(f"  Plan: {plan}")
#     if cnt != 4:
#         print()
#
# teacher solution
# for user in sorted(users, key=lambda user: (["Gold", "Silver", "Bronze", "Basic"].index(user.plan), user.email)):
#     print(f"{user.name} {user.surname}")
#     print(f"  Email: {user.email}")
#     print(f"  Plan: {user.plan}")
#     print()


# # my solution
# import csv
# from collections import namedtuple
# from datetime import datetime
#
# # meeting = namedtuple('meeting', ['surname', 'name', 'date', 'time'])
#
# with open('meetings.csv', 'r', encoding='utf-8') as file:
#     file_info = csv.reader(file, delimiter=',')
#     headline = next(file_info)
#     dict_meet = {}
#
#     for row in file_info:
#         surname, name, date, time = row
#         date = datetime.strptime(date, '%d.%m.%Y').date()
#         time = datetime.strptime(time, '%H:%M').time()
#         datetime_object = datetime.strptime(f"{date} {time}", '%Y-%m-%d %H:%M:%S')
#         dict_meet[(surname, name)] = datetime_object
#
# sort_dict_meet_values = sorted(dict_meet.items(), key=lambda x: x[1])
#
# for key, value in sort_dict_meet_values:
#     print(f"{key[0]} {key[1]}")

# import csv
# from collections import namedtuple
# from datetime import datetime
#
# with open('meetings.csv', encoding='utf-8') as fi:
#     rows = csv.DictReader(fi)
#     Friends = namedtuple('Friends', rows.fieldnames)
#     meetings = [Friends(**row) for row in rows]
#
# meetings.sort(key=lambda item: datetime.strptime(f"{item.meeting_date} {item.meeting_time}", "%d.%m.%Y %H:%M"))
# for meeting in meetings:
#     print(meeting.surname, meeting.name)
