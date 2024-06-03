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

# from collections import OrderedDict
#
# data = OrderedDict(
#     {'Name': 'Брусника',
#      'IsNetObject': 'да',
#      'OperatingCompany': 'Брусника',
#      'TypeObject': 'кафе',
#      'AdmArea': 'Центральный административный округ',
#      'District': 'район Арбат',
#      'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
#      'SeatsCount': '10'}
# )
#
# print(OrderedDict(reversed(data.items())))

# from collections import OrderedDict
#
# data = OrderedDict(
#  {'Name': 'Брусника',
#   'IsNetObject': 'да',
#   'OperatingCompany': 'Брусника',
#   'TypeObject': 'кафе',
#   'AdmArea': 'Центральный административный округ',
#   'District': 'район Арбат',
#   'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
#   'SeatsCount': '10'}
# )
#
# new_grades = OrderedDict()
#
# for rule in (False, True, False, True, False, True, False, True):
#     key, value = data.popitem(last=rule)
#     new_grades[key] = value
#
# print(OrderedDict(new_grades))

# from collections import Counter
#
# files = [
#     'emoji_smile.jpeg',
#     'city-of-the-sun.mp3',
#     'dhook_hw.json',
#     'sample.xml',
#     'teamspeak3.exe',
#     'project_module3.py',
#     'math_lesson3.mp4',
#     'old_memories.mp4',
#     'spiritfarer.exe',
#     'backups.json',
#     'python_for_beg1.mp4',
#     'emoji_angry.jpeg',
#     'exam_results.csv',
#     'project_main.py',
#     'classes.csv',
#     'plants.xml',
#     'cant-help-myself.mp3',
#     'microsoft_edge.exe',
#     'steam.exe',
#     'math_lesson4.mp4',
#     'city.jpeg',
#     'bad-disease.mp3',
#     'beauty.jpeg',
#     'hollow_knight_silksong.exe',
#     'whatsapp.exe',
#     'photoshop.exe',
#     'telegram.exe',
#     'yandex_browser.exe',
#     'math_lesson7.mp4',
#     'students.csv',
#     'emojis.zip',
#     '7z.zip',
#     'bones.mp3',
#     'python3.zip',
#     'dhook_lsns.json',
#     'carl_backups.json',
#     'forest.jpeg',
#     'python_for_pro8.mp4',
#     'yandexdisc.exe',
#     'but-you.mp3',
#     'project_module1.py',
#     'nothing.xml',
#     'flowers.jpeg',
#     'grades.csv',
#     'nvidia_gf.exe',
#     'small_txt.zip',
#     'project_module2.py',
#     'tab.csv',
#     'note.xml',
#     'sony_vegas11.exe',
#     'friends.jpeg',
#     'data.pkl'
# ]
#
# total = Counter([file.split('.')[1] for file in files])
#
# for i in sorted(total):
#     print(f"{i}: {total[i]}")

# from collections import Counter
#
#
# def count_occurences(word, words):
#     return Counter(words.lower().split()).get(word.lower(), 0)
#
#
# # word = 'python'
# # words = 'Python Conferences python training python events'
#
# word = 'Se'
# words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'
#
#
# print(count_occurences(word, words))


# from collections import Counter
#
# total_sales = Counter([i for i in input().split(',')])
#
# for sales, cnt in sorted(total_sales.items()):
#     print(f"{sales}: {cnt}")


# ascii_value = ord('р')
#
# print(ascii_value)

# from collections import Counter
#
#
# def ascii_value(word):
#     return sum(ord(i) for i in word if i != ' ')
#
#
# sales = [(i, ascii_value(i)) for i in input().split(',')]
#
# max_len = max(len(i[0]) for i in sales)
#
# total_sales = Counter(sales)
#
# for sales, cnt in sorted(total_sales.items()):
#     if len(sales[0]) == max_len:
#         print(f"{sales[0]}: {sales[1]} UC x {cnt} = {sales[1] * cnt} UC")
#     else:
#         average_len = max_len - len(sales[0])
#         print(sales[0] + ' ' * average_len + f": {sales[1]} UC x {cnt} = {sales[1] * cnt} UC")

# also we can use ljust() and rjust()


# my solution
# from collections import Counter
#
# with open('pythonzen.txt', encoding='utf-8') as txt_file:
#     text = txt_file.readlines()
#
#     all_words = []
#
#     for i in sorted(text):
#         new_text = ''.join(i.lower().split())
#         for j in new_text:
#             if j.isalpha():
#                 all_words.append(j)
#
#     total = Counter(all_words)
#
#     for i in sorted(total):
#         print(f"{i}: {total[i]}")


# teacher solution
# from collections import Counter
#
# with open('pythonzen.txt', encoding='utf-8') as file:
#     counter = Counter(c for c in file.read().lower() if c.isalpha())
#     [print(f'{k}: {counter[k]}') for k in sorted(counter)]


# from collections import Counter
#
# string_input = [i for i in input().lower().split()]
#
# print(Counter(string_input).most_common(1)[0][0])


# from collections import Counter
#
# string_input = [i for i in input().lower().split()]
#
# min_value = min(Counter(string_input).values())
#
# list_words = []
# for key, value in sorted(Counter(string_input).items()):
#     if value == min_value:
#         list_words.append(key)
#
# print(*list_words, sep=', ')


# from collections import Counter
#
# string_input = [i for i in input().lower().split()]
#
# most_common_word = []
#
# for key, value in sorted(Counter(string_input).items()):
#     if value == Counter(string_input).most_common(1)[0][1]:
#         most_common_word.append(key)
#
# if len(sorted(most_common_word)) > 1:
#     print(sorted(most_common_word)[-1])
# else:
#     print(*most_common_word)


# from collections import Counter, defaultdict
#
# string_input = [i.lower() for i in input().lower().split()]
#
# len_word_cnt = defaultdict(int)
#
# for key, value in Counter(string_input).items():
#     len_word_cnt[len(key)] += value
#
# for key, value in sorted(len_word_cnt.items(), key=lambda x: x[1]):
#     print(f"{key}: {value}")

# from collections import Counter
# import sys

# input_data = sys.stdin.read().split('\n')
#
# dic = {}
#
# for i in input_data:
#     key, value = i.split()
#     dic[key] = int(value)
#
# print(sorted(dic.items(), key=lambda x: x[1], reverse=True)[-2][0])


# from collections import Counter, namedtuple
# import csv
#
# Person = namedtuple('Person', 'username, email, dtime')
#
# with open('name_log.csv', encoding='utf-8') as file:
#     file_info = csv.reader(file)
#     next(file_info)
#
#     file_rename = Counter(i[1] for i in file_info)
#
#     for name, cnt in sorted(file_rename.items()):
#         print(f"{name}: {cnt}")


# from collections import Counter
#
# def scrabble(symbols, word):
#     symbol_in_word = Counter(word.lower())
#     repeat_symbols = Counter(symbols.lower())
#     if symbol_in_word - repeat_symbols == {}:
#         return True
#     else:
#         return False
#
#
# print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
# print(scrabble('begk', 'beegeek'))
# print(scrabble('beegeek', 'beegeek'))

# from collections import Counter
#
#
# def print_bar_chart(data, mark):
#     bar = Counter(data)
#     max_len = len(max(bar, key=lambda x: len(x)))
#
#     for i in sorted(bar, key=lambda x: bar[x], reverse=True):
#         if len(i) != max_len:
#             print(f"{i}{' ' * (max_len - len(i))} |{bar[i] * mark}")
#         else:
#             print(f"{i} |{bar[i] * mark}")


# print_bar_chart('beegeek', '+')

# languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
# print_bar_chart(languages, '#')

# my solution
# from collections import Counter, namedtuple, defaultdict
# import csv
# import json
#
# Vegetables = namedtuple('vegetables', 'name cntJanuary cntFebruary cntMarch')
#
# with open('quarter1.csv', encoding='utf-8') as first_file:
#     with open('quarter2.csv', encoding='utf-8') as second_file:
#         with open('quarter3.csv', encoding='utf-8') as third_file:
#             with open('quarter4.csv', encoding='utf-8') as fourth_file:
#                 first_file = csv.reader(first_file)
#                 second_file = csv.reader(second_file)
#                 third_file = csv.reader(third_file)
#                 fourth_file = csv.reader(fourth_file)
#
#                 next(first_file)
#                 next(second_file)
#                 next(third_file)
#                 next(fourth_file)
#
#                 first_file = list(first_file)
#                 second_file = list(second_file)
#                 third_file = list(third_file)
#                 fourth_file = list(fourth_file)
#
#                 quarter = first_file + second_file + third_file + fourth_file
#
# with open('prices.json', encoding='utf-8') as five_file:
#     json_file = json.load(five_file)
#
# dic_price = dict(json_file)
#
#
# sum_dic = defaultdict(int)
#
# for i in quarter:
#     sales = Vegetables(i[0], int(i[1]), int(i[2]), int(i[3]))
#     sum_cnt = sales.cntJanuary + sales.cntFebruary + sales.cntMarch
#     sum_dic[sales.name] += sum_cnt
#
# total_dict = {}
#
# for name, price in sum_dic.items():
#     if name in dic_price:
#         total_dict[name] = price * dic_price[name]
#     else:
#         total_dict[name] = price
#
# total = 0
# for key, value in total_dict.items():
#     total += value
#
# print(total)

# import json
#
# with open('zoo.json', encoding='utf-8') as file:
#     zoo_data = json.load(file)
#
# total_animals = sum(animal_count for animal_counts in zoo_data for animal_count in animal_counts.values())
#
# print(total_animals)


# import json
# from collections import ChainMap
#
# with open('zoo.json', encoding='utf-8') as js:
#     animals = ChainMap(*json.load(js))
#
# print(sum(animals.values()))

# from collections import ChainMap, Counter
#
# bread = {
#     'булочка с кунжутом': 15,
#     'обычная булочка': 10,
#     'ржаная булочка': 15
# }
#
# meat = {
#     'куриный бифштекс': 50,
#     'говяжий бифштекс': 70,
#     'рыбный бифштекс': 40
# }
#
# sauce = {
#     'сливочно-чесночный': 15,
#     'кетчуп': 10,
#     'горчица': 10,
#     'барбекю': 15,
#     'чили': 15
# }
#
# vegetables = {
#     'лук': 10,
#     'салат': 15,
#     'помидор': 15,
#     'огурцы': 10
# }
#
# toppings = {
#     'сыр': 25,
#     'яйцо': 15,
#     'бекон': 30
# }
#
# priceList = ChainMap(bread, meat, sauce, vegetables, toppings)
#
# total_sum = 0
# order = input().split(',')
# listOrder = Counter(order)
#
# lenSpace = (len(max(listOrder, key=listOrder.get)))
#
# for key, value in sorted(listOrder.items()):
#     if key in priceList:
#         print(f"{key}{' ' * (lenSpace - len(key))} x {value}")
#         total_sum += priceList[key] * value
#
# print('-' * (lenSpace + 6))
# print(f"Итог: {total_sum}р")
