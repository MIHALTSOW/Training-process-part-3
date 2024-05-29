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


# from collections import namedtuple
#
# Party = namedtuple('Party', 'name date time')
#
# party = Party(name='Jack', date='01.01.2020', time='10:00')
#
# print(party[0])
# print(party.name)
# print(party[1])
# print(party.date)

# from collections import defaultdict
#
# info = defaultdict(int)
#
# info['name'] = 'Timur'
# info['age'] = 29
# info['job'] = 'Teacher'
#
# print(info['salary'])
# print(info)

# from collections import defaultdict
#
# info = defaultdict(int, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
#
# print(info['name'])
# print(info['salary'])
# print(info)

# from collections import defaultdict
#
# info1 = defaultdict(int, name='Timur', age=29, job='Teacher')
# info2 = defaultdict(int, [('name', 'Timur'), ('age', 29), ('job', 'Teacher')])
#
# print(info1)
# print(info2)

# from collections import defaultdict
# a = defaultdict.fromkeys(['name', 'surname', 'hobby'], None)
#
# print(type(a))


# from collections import defaultdict
#
# data = data = [
#     ('Books', 1343),
#     ('Books', 1166),
#     ('Merch', 616),
#     ('Courses', 966),
#     ('Merch', 1145),
#     ('Courses', 1061),
#     ('Books', 848),
#     ('Courses', 964),
#     ('Tutorials', 832),
#     ('Merch', 642),
#     ('Books', 815),
#     ('Tutorials', 1041),
#     ('Books', 1218),
#     ('Tutorials', 880),
#     ('Books', 1003),
#     ('Merch', 951),
#     ('Books', 920),
#     ('Merch', 729),
#     ('Tutorials', 977),
#     ('Books', 656)
# ]
#
# total_value = defaultdict(int)
#
# for i in data:
#     name, value = i
#     total_value[name] += value
#
# for key, value in sorted(total_value.items(), key=lambda x: x):
#     print(f"{key}: ${value}")

# from collections import defaultdict
#
# staff = [
#     ('Sales', 'Robert Barnes'),
#     ('Developing', 'Thomas Porter'),
#     ('Accounting', 'James Wilkins'),
#     ('Sales', 'Connie Reid'),
#     ('Accounting', 'Brenda Davis'),
#     ('Developing', 'Miguel Norris'),
#     ('Accounting', 'Linda Hudson'),
#     ('Developing', 'Deborah George'),
#     ('Developing', 'Nicole Watts'),
#     ('Marketing', 'Billy Lloyd'),
#     ('Sales', 'Charlotte Cox'),
#     ('Marketing', 'Bernice Ramos'),
#     ('Sales', 'Jose Taylor'),
#     ('Sales', 'Katie Warner'),
#     ('Accounting', 'Steven Diaz'),
#     ('Accounting', 'Kimberly Reynolds'),
#     ('Accounting', 'John Watts'),
#     ('Accounting', 'Dale Houston'),
#     ('Developing', 'Arlene Gibson'),
#     ('Marketing', 'Joyce Lawrence'),
#     ('Accounting', 'Rosemary Garcia'),
#     ('Marketing', 'Ralph Morgan'),
#     ('Marketing', 'Sam Davis'),
#     ('Marketing', 'Gail Hill'),
#     ('Accounting', 'Michelle Wright'),
#     ('Accounting', 'Casey Jenkins'),
#     ('Sales', 'Evelyn Martin'),
#     ('Accounting', 'Aaron Ferguson'),
#     ('Marketing', 'Andrew Clark'),
#     ('Marketing', 'John Gonzalez'),
#     ('Developing', 'Wilma Woods'),
#     ('Sales', 'Marie Cooper'),
#     ('Accounting', 'Kay Scott'),
#     ('Sales', 'Gladys Taylor'),
#     ('Accounting', 'Ann Bell'),
#     ('Accounting', 'Craig Wood'),
#     ('Accounting', 'Gloria Higgins'),
#     ('Marketing', 'Mario Reynolds'),
#     ('Marketing', 'Helen Taylor'),
#     ('Marketing', 'Mary King'),
#     ('Accounting', 'Jane Jackson'),
#     ('Marketing', 'Carol Peters'),
#     ('Sales', 'Alicia Mendoza'),
#     ('Accounting', 'Edna Cunningham'),
#     ('Developing', 'Joyce Rivera'),
#     ('Sales', 'Joseph Lee'),
#     ('Sales', 'John White'),
#     ('Marketing', 'Charles Bailey'),
#     ('Sales', 'Chester Fernandez'),
#     ('Sales', 'John Washington')
# ]
#
# cnt_office = defaultdict(int)
#
# for i in staff:
#     office, name = i
#     cnt_office[office] += 1
#
# for office, name in sorted(cnt_office.items(), key=lambda x: x):
#     print(f"{office}: {name}")


# from collections import defaultdict
#
# staff_broken = [
#     ('Developing', 'Miguel Norris'),
#     ('Sales', 'Connie Reid'),
#     ('Sales', 'Joseph Lee'),
#     ('Marketing', 'Carol Peters'),
#     ('Accounting', 'Linda Hudson'),
#     ('Accounting', 'Ann Bell'),
#     ('Marketing', 'Ralph Morgan'),
#     ('Accounting', 'Gloria Higgins'),
#     ('Developing', 'Wilma Woods'),
#     ('Developing', 'Wilma Woods'),
#     ('Marketing', 'Bernice Ramos'),
#     ('Marketing', 'Joyce Lawrence'),
#     ('Accounting', 'Craig Wood'),
#     ('Developing', 'Nicole Watts'),
#     ('Sales', 'Jose Taylor'),
#     ('Accounting', 'Linda Hudson'),
#     ('Accounting', 'Edna Cunningham'),
#     ('Sales', 'Jose Taylor'),
#     ('Marketing', 'Helen Taylor'),
#     ('Accounting', 'Kimberly Reynolds'),
#     ('Marketing', 'Mary King'),
#     ('Sales', 'Joseph Lee'),
#     ('Accounting', 'Gloria Higgins'),
#     ('Marketing', 'Andrew Clark'),
#     ('Accounting', 'John Watts'),
#     ('Accounting', 'Rosemary Garcia'),
#     ('Accounting', 'Steven Diaz'),
#     ('Marketing', 'Mary King'),
#     ('Sales', 'Gladys Taylor'),
#     ('Developing', 'Thomas Porter'),
#     ('Accounting', 'Brenda Davis'),
#     ('Sales', 'Connie Reid'),
#     ('Sales', 'Alicia Mendoza'),
#     ('Marketing', 'Mario Reynolds'),
#     ('Sales', 'John White'),
#     ('Developing', 'Joyce Rivera'),
#     ('Accounting', 'Steven Diaz'),
#     ('Developing', 'Arlene Gibson'),
#     ('Sales', 'Robert Barnes'),
#     ('Sales', 'Charlotte Cox'),
#     ('Accounting', 'Craig Wood'),
#     ('Marketing', 'Carol Peters'),
#     ('Marketing', 'Ralph Morgan'),
#     ('Accounting', 'Kay Scott'),
#     ('Sales', 'Evelyn Martin'),
#     ('Marketing', 'Billy Lloyd'),
#     ('Sales', 'Gladys Taylor'),
#     ('Developing', 'Deborah George'),
#     ('Sales', 'Charlotte Cox'),
#     ('Marketing', 'Sam Davis'),
#     ('Sales', 'John White'),
#     ('Sales', 'Marie Cooper'),
#     ('Marketing', 'John Gonzalez'),
#     ('Sales', 'John Washington'),
#     ('Sales', 'Chester Fernandez'),
#     ('Sales', 'Alicia Mendoza'),
#     ('Sales', 'Katie Warner'),
#     ('Accounting', 'Jane Jackson'),
#     ('Sales', 'Chester Fernandez'),
#     ('Marketing', 'Charles Bailey'),
#     ('Marketing', 'Gail Hill'),
#     ('Accounting', 'Casey Jenkins'),
#     ('Accounting', 'James Wilkins'),
#     ('Accounting', 'Casey Jenkins'),
#     ('Marketing', 'Mario Reynolds'),
#     ('Accounting', 'Aaron Ferguson'),
#     ('Accounting', 'Kimberly Reynolds'),
#     ('Sales', 'Robert Barnes'),
#     ('Accounting', 'Aaron Ferguson'),
#     ('Accounting', 'Jane Jackson'),
#     ('Developing', 'Deborah George'),
#     ('Accounting', 'Michelle Wright'),
#     ('Accounting', 'Dale Houston')
# ]

# my solution
# colleagues = defaultdict(set)
#
# for i in staff_broken:
#     office, name = i
#     colleagues[office].add(name)
#     # if (name,) not in colleagues:
#     #     colleagues[office] += (name,)
#
#
# for key, value in sorted(colleagues.items(), key=lambda x: x[0]):
#     print(key, sep='', end=': '), print(*sorted(value), sep=', ')

# teacher solution
# departments = defaultdict(set)
#
# for department, employee in staff_broken:
#     departments[department].add(employee)
#
# for department in sorted(departments):
#     staff = sorted(list(departments[department]))
#     print(f'{department}: {", ".join(staff)}')

# from collections import defaultdict
#
#
# def wins(pairs):
#     result = defaultdict(set)
#     for winner, loser in pairs:
#         result[winner].add(loser)
#     return result
#
#
# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))

# from collections import defaultdict
#
#
# def flip_dict(dict_of_lists):
#     fip_dict = defaultdict(list)
#     for key, value in dict_of_lists.items():
#         for i in value:
#             fip_dict[i].append(key)
#
#     return fip_dict
#
#
# print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

# from collections import defaultdict

# def best_sender(messages, senders):
#     result = defaultdict(int)
#     for message, sender in zip(messages, senders):
#         result[sender] += len(message)
#     max_value = max(result.values())
#     for k, v in result.items():
#         if v == max_value:
#             return k
# return [k for k, v in result.items() if v == max_value]


# messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
# senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
#
# print(best_sender(messages, senders))

