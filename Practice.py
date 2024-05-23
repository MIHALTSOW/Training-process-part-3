# cut end string
# data = [line[:-2] for line in sys.stdin]
#
# for i in data:
#     print(i[::-1])

# my soulution
# data = [line[:-1] if line[-1] == '\n' else line for line in sys.stdin]
#
# for i in data:
#     print(i[::-1])

# teacher solution
# import sys
#
# for line in sys.stdin:
#     print(line.strip()[::-1])


# my soulution

# import sys
# from datetime import date
#
# dates = [date(*map(int, dt.split('-'))) for dt in sys.stdin]
#
# mx_date = max(dates)
# mn_date = min(dates)
# difference_date = (mx_date - mn_date).days
#
# print(difference_date)

# teacher solution
# import sys
# from datetime import datetime
#
# data = [datetime.fromisoformat(line.strip()) for line in sys.stdin]
# print((max(data) - min(data)).days)


# my soulution
# import sys
#
# cnt = 0
# for i in sys.stdin:
#     cnt += 1
#     last_digit = i.strip()
#
# if cnt % 2 != 0 and int(last_digit) % 2 == 0 or cnt % 2 == 0 and int(last_digit) % 2 != 0:
#     print('Анри')
# else:
#     print('Дима')

# teacher solution
# import sys
#
# s = tuple(int(i.strip()) for i in sys.stdin.readlines())
# print(('Дима', 'Анри')[(len(s) - 1) % 2 == s[-1] % 2])

# import sys
#
# length_students = [int(line.strip()) for line in sys.stdin]
#
# if len(length_students) == 0:
#     print("нет учеников")
# else:
#     print(f"Рост самого низкого ученика: {min(length_students)}")
#     print(f"Рост самого высокого ученика: {max(length_students)}")
#     print(f"Средний рост: {sum(length_students) / len(length_students)}")

# import sys
#
# cnt = 0
# for string in sys.stdin:
#     new_str = string.strip()
#     if new_str[0] == '#':
#         cnt += 1
#
# print(cnt)

# import sys
#
# without_comment = []
#
# for string in sys.stdin:
#     new_str = string.strip()
#     if len(new_str) == 0:
#         without_comment.append('\n')
#     elif new_str[0] != '#':
#         without_comment.append(string)
#
# print(''.join(without_comment))


# my soulution
# import sys
#
# # news = [new.strip() for new in sys.stdin]
#
# news = [
#     'На рейсах Поражения второй пилот будет исполнять обязанности бортпроводника / Авиация / 0.3',
#     'Огурец исключит из своих рядов членов, не проголосовавших за Единую Арстоцку на выборах / Политика / 0.8',
#     'Орбистанские точки общепита будут закрыты для вакцинированных граждан / Общество / 0.7',
#     'Джорджи Костава получил членский билет Независимого Кобрастана / Политика / 0.0',
#     'В Колечии повысят призывной возраст до 40 лет / Политика / 1.0',
#     'Всем гражданам Антегрии въезд в Арстоцку запрещен / Политика / 0.8',
#     'Политика'
# ]
#
# key_name = news[-1]  # Политика
#
# only_need = {}
# dict_news = {}
# key_list = []
# value_list_original = []
# value_list_type = []
#
# news = [i for i in news if i != key_name]
#
# for string_key in news:
#     for key in string_key.split(' / '):
#         key_list.append(key)
#         break
#
# for string_value in news:
#     cnt = 0
#     for value in string_value.split(' / '):
#         cnt += 1
#         if cnt == 3:
#             value_list_original.append(float(value))
#             break
#
# for string_value in news:
#     cnt = 0
#     for value in string_value.split(' / '):
#         cnt += 1
#         if cnt == 2:
#             value_list_type.append(value)
#             break
#
# for i, j, k in zip(key_list, value_list_original, value_list_type):
#     dict_news[i] = [j, k]
#
# for key, value in dict_news.items():
#     if value[1] == key_name:
#         only_need[key] = value[0]
#
# only_need_sorted_value = sorted(only_need.items(), key=lambda x: (x[1], x[0]))
#
# for key, value in only_need_sorted_value:
#     print(key)

# teacher solution he can split this shit
# import sys
#
# events, priority_tag = {}, None
#
# for line in sys.stdin:
#     line = line.strip().split(' / ')
#     if len(line) > 1:
#         event, tag, score = line
#         events.setdefault(tag, []).append((score, event))
#     else:
#         priority_tag = line[0]
#
# for _, event in sorted(events[priority_tag]):
#     print(event)


# import sys
# from datetime import datetime
#
# cnt = 0
# dict_date = {datetime.strptime(date.strip(), '%d.%m.%Y'): value for value, date in enumerate(sys.stdin.readlines()) if (cnt := cnt + 1)}
#
# sort_ASC = sorted(dict_date.items(), key=lambda x: x[0])
# sort_DESC = sorted(dict_date.items(), key=lambda x: x[0], reverse=True)
#
# if len(dict_date) != cnt:
#     print('MIX')
# elif list(dict_date.items()) == list(sort_ASC):
#     print('ASC')
# elif list(dict_date.items()) == list(sort_DESC):
#     print('DESC')
# else:
#     print('MIX')

#
# with open('sales.csv', 'r', encoding='utf-8') as csv_file:
#     rows = csv.reader(csv_file, delimiter=';', quotechar='"')
#     cnt = 0
#     for row in rows:
#         cnt += 1
#         if cnt >= 2 and int(row[1]) > int(row[2]):
#             print(row[0])

# interesting variant
# with open('sales.csv', 'r', encoding='utf-8') as csv_file:
#     rows = csv.reader(csv_file, delimiter=';', quotechar='"')
#     next(rows)  # skip the header row
#     for row in rows:
#         if int(row[1]) > int(row[2]):
#             print(row[0])

# You can use neme from title
# name / old_price / new_price

# first variant
# import csv
#
# with open('salary_data.csv', 'r', encoding='utf-8') as csv_file:
#     rows = csv.DictReader(csv_file, delimiter=';')
#     dict_companies = {row['company_name']: int(row['salary']) for row in rows}
#
# company_avgs = {}
# for company, salary in dict_companies.items():
#     if company not in company_avgs:
#         company_avgs[company] = [salary, 1]
#     else:
#         company_avgs[company][0] += salary
#         company_avgs[company][1] += 1
#
# for company in company_avgs:
#     company_avgs[company] = company_avgs[company][0] / company_avgs[company][1]
#
# sorted_dict_companies = sorted(company_avgs.items(), key=lambda x: (x[1], x[0]))
#
# for company, _ in sorted_dict_companies:
#     print(company)

# second variant
# import csv
#
# with open('salary_data.csv', 'r', encoding='utf-8') as csv_file:
#     rows = csv.reader(csv_file, delimiter=';')
#     next(rows)
#     data = {}
#     for row in rows:
#         company_name, salary = row
#         if company_name in data:
#             data[company_name].append(int(salary))
#         else:
#             data[company_name] = [int(salary)]
#
# company_avgs = {company: sum(salaries) / len(salaries) for company, salaries in data.items()}
# sorted_companies = sorted(company_avgs.items(), key=lambda x: (x[1], x[0]))
#
# for company, _ in sorted_companies:
#     print(company)


# import csv
#
# sorting_order = int(input())
#
# with open('deniro.csv', 'r', encoding='utf-8') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     words_list = []
#     for row in rows:
#         row[0] = str(row[0])
#         row[1] = int(row[1])
#         row[2] = int(row[2])
#         row = [row[0], row[1], row[2]]
#         words_list.append(row)
#
# if sorting_order == 1:
#     words_list.sort(key=lambda x: x[0])
# elif sorting_order == 2:
#     words_list.sort(key=lambda x: x[1])
# elif sorting_order == 3:
#     words_list.sort(key=lambda x: x[2])
#
# for row in words_list:
#     print(f"{row[0]},{row[1]},{row[2]}")

# text = '''movie,year,rating
# Machete,2010,72
# Marvin's Room,1996,80
# Raging Bull,1980,97
# This Boy's Life,1993,75
# Silver Linings Playbook,2012,92
# Taxi Driver,1976,99
# Jackie Brown,1997,87
# Shark Tale,2004,35
# Bang the Drum Slowly,1973,88
# Analyze That,2002,27
# Meet the Parents,2000,84
# Wag the Dog,1997,85
# The Big Wedding,2013,7
# Night and the City,1992,67
# Backdraft,1991,71
# The Untouchables,1987,80
# Cop Land,1997,72
# Thunderheart,1992,87
# Being Flynn,2012,51
# We're No Angels,1989,47
# Limitless,2011,70
# The Bag Man,2014,9
# The Good Shepherd,2006,54
# Jacknife,1989,64
# Righteous Kill,2008,19
# Mad Dog and Glory,1993,78
# Brazil,1985,98
# Mary Shelley's Frankenstein,1994,39
# Stone,2010,50
# Killer Elite,2011,25
# A Bronx Tale,1993,96
# Falling in Love,1984,60
# The Adventures of Rocky & Bullwinkle,2000,43
# Red Lights,2012,29
# The Score,2001,73
# New Year's Eve,2011,7
# Ronin,1998,68
# Midnight Run,1988,96
# Last Vegas,2013,46
# Born to Win,1971,40
# Angel Heart,1987,78
# City by the Sea,2002,48
# Cape Fear,1991,76
# Everybody's Fine,2009,46
# Goodfellas,1990,96
# 15 Minutes,2001,33
# Mistress,1991,69
# Hide and Seek,2005,13
# The Intern,2015,61
# Awakenings,1990,88
# Joy,2015,60
# Mean Streets,1973,98
# The Deer Hunter,1978,93
# Great Expectations,1998,38
# True Confessions,1981,75
# The Mission,1986,65
# Killing Season,2013,11
# The King of Comedy,1983,90
# New York,1977,67
# Rent,2005,46
# Once Upon a Time in America,1984,89
# Meet the Fockers,2004,38
# Bloody Mama,1970,17
# The Last Tycoon,1976,41
# Grudge Match,2013,29
# Analyze This,1999,69
# The Bridge of San Luis Rey,2005,4
# Guilty by Suspicion,1991,65
# What Just Happened?,2008,51
# Heat,1995,86
# Godsend,2003,4
# Captain Shakespeare,2007,76
# Flawless,1999,43
# Stanley & Iris,1990,29
# Arthur and the Invisibles,2007,21
# Greetings,1968,86
# Little Fockers,2010,10
# Sleepers,1996,74
# Dirty Grandpa,2016,11
# Dear America: Letters Home From Vietnam,1987,100
# Casino,1995,80
# The Fan,1996,38
# Heist,2015,26
# Men of Honor,2000,41'''
#
# with open('deniro.csv', 'w') as file:
#     file.write(text)


# combine csv columns (my solution)
# def csv_columns(file_name):
#     data = {}
#     with open(file_name, 'r', encoding='utf-8') as csv_file:
#         reader = csv.reader(csv_file, delimiter=',')
#         header = next(reader)
#
#         for row in reader:
#             for i, value in enumerate(row):
#                 print(i, value)
#                 column_name = header[i]
#                 if column_name in data:
#                     data[column_name].append(value)
#                 else:
#                     data[column_name] = [value]
#
#         return data
#
#
# print(csv_columns('deniro.csv'))

# import csv
#
# with open('data.csv', 'r', encoding='utf-8') as csv_file:
#     reader = csv.DictReader(csv_file, delimiter=',')
#
#     domain_count = {}
#     for row in reader:
#         email = row['email']
#         domain = email.split('@')[1]
#         if domain in domain_count:
#             domain_count[domain] += 1
#         else:
#             domain_count[domain] = 1
#
# sort_domain_count = sorted(domain_count.items(), key=lambda x: (x[1], x[0]))
# # print('domain' + ',' + 'count')
#
# # for domain, count in sort_domain_count:
# # print(f"{domain},{count}")
#
# with open('domain_usage.csv', 'w', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['domain', 'count'])
#     for domain, count in sort_domain_count:
#         writer.writerow([domain, count])


# import csv
#
# with open('wifi.csv', 'r', encoding='utf-8') as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#
#     district_number_of_access_points = {}
#
#     for row in reader:
#         district = row[1]
#         try:
#             number_of_access_points = int(row[3])
#         except ValueError:
#             continue
#
#         if district in district_number_of_access_points:
#             district_number_of_access_points[district] += number_of_access_points
#         else:
#             district_number_of_access_points[district] = number_of_access_points

# less comfortable variant sort

# sorted_district_number_of_access_points = sorted(district_number_of_access_points.items(), key=lambda x: x[0])
# sorted_district_number_of_access_points_second = sorted(sorted_district_number_of_access_points, key=lambda x: x[1],
#                                                         reverse=True)
#
# for district, number in sorted_district_number_of_access_points_second:
#     print(f'{district}: {number}')

# more comfortable variant sort

# for district, number in sorted(district_number_of_access_points.items(), key=lambda x: (-x[1], x[0])):
#     print(f'{district}: {number}')

# import csv
#
# with open('titanic.csv', 'r', encoding='utf-8') as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     next(reader)
#
#     less_18_alive_man_woman = {}
#     for row in reader:
#         alive, name, sex, age = row
#         try:
#             float_age = float(age)
#         except ValueError:
#             try:
#                 int_age = int(age)
#             except ValueError:
#                 print(f"Invalid age value for {name}: {age}")
#             else:
#                 if int_age < 18 and int(alive) == 1:
#                     less_18_alive_man_woman[name] = sex
#         else:
#             if float_age < 18 and int(alive) == 1:
#                 less_18_alive_man_woman[name] = sex
#
#     sorted_male_female = sorted(less_18_alive_man_woman.items(), key=lambda x: x[1], reverse=True)
#
#     for name, sex in sorted_male_female:
#         print(name)


# import csv
#
# fresh_entries = {}
#
# with open('name_log.csv', 'r', encoding='utf-8') as csv_file:
#     reader = csv.reader(csv_file)
#     header = next(reader)
#
#     for row in reader:
#         username, email, dtime = row
#         if email in fresh_entries:
#             if dtime > fresh_entries[email][1]:
#                 fresh_entries[email] = (username, dtime)
#         else:
#             fresh_entries[email] = (username, dtime)
#
# sorted_entries = sorted(fresh_entries.items(), key=lambda x: x[0])
#
# with open('new_name_log.csv', 'w', newline='', encoding='utf-8') as new_file:
#     writer = csv.writer(new_file)
#     writer.writerow(header)
#     for email, (username, dtime) in sorted_entries:
#         writer.writerow([username, email, dtime])

# import json
#
# lines = {
#     True: 97,
#     2: "I've been running for a reason",
#     "3": ("I", "could", "never", "retain"),
#     4: ["Sweet", "lips", "like", "pink", "lemonade"],
#     5.0: "When he's feeling generous he's gonna give me a taste",
#     "six": "10"
# }
#
# lines_json = json.dumps(lines)
#
# lines = json.loads(lines_json)
#
# for key, velue in lines.items():
#     print(f"{key} - {type(key)} / {velue} - {type(velue)}")


# import json
#
# countries = {
#     'Monaco': 'Monaco',
#     'Iceland': 'Reykjavik',
#     'Kenya': 'Nairobi',
#     'Kazakhstan': 'Nur-Sultan',
#     'Mali': 'Bamako',
#     'Colombia': 'Bogota',
#     'Finland': 'Helsinki',
#     'Costa Rica': 'San Jose',
#     'Cuba': 'Havana',
#     'France': 'Paris',
#     'Gabon': 'Libreville',
#     'Liberia': 'Monrovia',
#     'Angola': 'Luanda',
#     'India': 'New Delhi',
#     'Canada': 'Ottawa',
#     'Australia': 'Canberra'
# }
#
# line_json = json.dumps(countries, indent=3, sort_keys=True, separators=(',', ' - '))
#
# print(line_json)


# import json
#
# words = {
#     frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#     "travel": "trævl",
#     ("hello", "world"): ("həˈləʊ", "wɜːld"),
#     "moonlight": "muːn.laɪt",
#     "sunshine": "ˈsʌn.ʃaɪn",
#     ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#     "adventure": "ədˈventʃər",
#     "beautiful": "ˈbjuːtɪfl",
#     frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#     "bicycle": "baisikl",
#     ("pilot", "fly"): ("pailət", "flai")
# }
#
# line_json = json.dumps(words, skipkeys=True, ensure_ascii=False)
# print(line_json)


# import json
#
# club1 = {
#     "name": "FC Byern Munchen",
#     "country": "Germany",
#     "founded": 1900,
#     "trainer": "Julian Nagelsmann",
#     "goalkeeper": "M. Neuer",
#     "league_position": 1
# }
#
# club2 = {
#     "name": "FC Barcelona",
#     "country": "Spain",
#     "founded": 1899,
#     "trainer": "Xavier Creus",
#     "goalkeeper": "M. Ter Stegen",
#     "league_position": 7
# }
#
# club3 = {
#     "name": "FC Manchester United",
#     "country": "England",
#     "founded": 1878,
#     "trainer": "Michael Carrick",
#     "goalkeeper": "D. De Gea",
#     "league_position": 8
# }
#
# with open('data.json', 'w', encoding='utf-8') as json_file:
#     json.dump([club1, club2, club3], json_file, indent=3)


# import json
#
# specs = {
#     'Модель': 'AMD Ryzen 5 5600G',
#     'Год релиза': 2021,
#     'Сокет': 'AM4',
#     'Техпроцесс': '7 нм',
#     'Ядро': 'Cezanne',
#     'Объем кэша L2': '3 МБ',
#     'Объем кэша L3': '16 МБ',
#     'Базовая частота': '3900 МГц'
# }
#
# specs_json = json.dumps(specs, ensure_ascii=False, indent=3)
#
# print(specs_json)


# import json
#
#
# def is_correct_json(string):
#     try:
#         json.loads(string)
#     except json.JSONDecodeError:
#         return False
#     else:
#         return True
#
#
# print(is_correct_json('number = 17'))

# my solution
# import sys
# import json
#
# input_data = sys.stdin.read().strip()
#
# dict_json = json.loads(input_data)
#
# for key, value in dict_json.items():
#     if isinstance(value, list):
#         value = ', '.join(str(val) for val in value)
#     print(f"{key}: {value}")


# import json
#
# # Открываем файл data.json и читаем данные
# with open('data.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
# # Создаем список для измененных данных
# updated_data = []
#
# # Обрабатываем каждый объект из исходного списка
# for obj in data:
#     # print(type(obj))
#     if isinstance(obj, str):
#         updated_data.append(obj + '!')
#     elif isinstance(obj, (int, float)):
#         if obj is True:
#             updated_data.append('false')
#         elif obj is False:
#             updated_data.append('true')
#         else:
#             updated_data.append(obj + 1)
#     elif isinstance(obj, list):
#         updated_data.append(obj * 2)
#     elif isinstance(obj, dict):
#         obj['newkey'] = None
#         updated_data.append(obj)
#     elif obj is None:
#         continue
#
# with open('updated_data.json', 'w', encoding='utf-8') as file:
#     json.dump(updated_data, file, ensure_ascii=False, indent=4)

# import json
#
# with open('data1.json', 'r', encoding='utf-8') as json_file:
#     first_file = json.load(json_file)
#
# with open('data2.json', 'r', encoding='utf-8') as json_file:
#     second_file = json.load(json_file)
#
# first_dict = {}
#
# for key_first, value_first in first_file.items():
#     first_dict[key_first] = value_first
#
# for key_second, value_second in second_file.items():
#     first_dict[key_second] = value_second
#
# with open('data_merge.json', 'w', encoding='utf-8') as json_file:
#     json.dump(first_dict, json_file, ensure_ascii=False, indent=4)

# other variant
# import json
#
# with open('data1.json', 'r', encoding='utf-8') as f1, open('data2.json', 'r', encoding='utf-8') as f2:
#     json1, json2 = json.load(f1), json.load(f2)
#     itog = json1 | json2
#     with open('data_merge.json', 'w', encoding='utf-8') as f3:
#         json.dump(itog, f3, ensure_ascii=False, indent=4)

# import json
#
# with open('people.json', 'r', encoding='utf-8') as json_file:
#     file_info = json.load(json_file)
#
# cnt_dict = {}

# final_cnt = {
#     'age': None,
#     'country': None,
#     'phone': None,
#     'family_status': None,
#     'email': None,
#     'name': None,
#     'children': None,
#     'university': None
# }

# find all keys for max value
# for item in file_info:
#     cnt = 0
#     for key in item:
#         cnt += 1
#         cnt_dict[key] = cnt
# print(cnt_dict)

# for item in file_info:
#     if len(item) != 8:
#         for key, value in final_cnt.items():
#             if key not in item:
#                 item[key] = None
#
# with open('updated_people.json', 'w', encoding='utf-8') as json_file:
#     json.dump(file_info, json_file, ensure_ascii=False, indent=4)

# print(len(item))

# teacher solution

# import json
#
# with open('people.json', encoding='uft-8') as js:
#     content = json.load(js)
#
# keys = set()
# for data in content:
#     keys |= data.keys()
#
# for data in content:
#     data |= dict.fromkeys(keys - data.keys())
#
# with open('updated_people.json', 'w') as js:
#     json.dump(content, js, indent=3)

# import json
#
# with open('countries.json', 'r', encoding='utf-8') as json_file:
#     content = json.load(json_file)
#
#     dict_religion_country = {}
#
#     for data in content:
#         if data['religion'] in dict_religion_country:
#             dict_religion_country[data['religion']].append(data['country'])
#         else:
#             dict_religion_country[data['religion']] = [data['country']]
#
# with open('religion.json', 'w', encoding='utf-8') as json_file:
#     json.dump(dict_religion_country, json_file, indent=3)
#
# # or we can use setdefault()
#
# import json
#
# with open('countries.json', 'r', encoding='utf-8') as json_file:
#     content = json.load(json_file)
#
#     dict_religion_country = {}
#
#     for data in content:
#         dict_religion_country.setdefault(data['religion'], []).append(data['country'])
#
# with open('religion.json', 'w', encoding='utf-8') as json_file:
#     json.dump(dict_religion_country, json_file, indent=3)

# import json
# import csv
#
# addresses = {}
#
# with open('playgrounds.csv', 'r', encoding='utf-8') as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     header = next(reader)
#
#     for row in reader:
#         object_name, adm_area, district, address = row
#         if adm_area not in addresses:
#             addresses[adm_area] = {}
#
#         if district not in addresses[adm_area]:
#             addresses[adm_area][district] = []
#
#         addresses[adm_area][district].append(address)
#
# with open('addresses.json', 'w', encoding='utf-8') as json_file:
#     json.dump(addresses, json_file, ensure_ascii=False, indent=3)

# import json
# import csv
#
# with open('students.json', 'r', encoding='utf-8') as json_file:
#     content = json.load(json_file)
#
#     more_18_progress_more_75 = {}
#
#     for row in content:
#         name, city, age, progress, phone = row['name'], row['city'], row['age'], row['progress'], row['phone']
#         if progress >= 75 and age >= 18:
#             more_18_progress_more_75[name] = phone
#
# more_18_progress_more_75_sort = sorted(more_18_progress_more_75.items(), key=lambda x: x[0])
#
# with open('data.csv', 'w', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(['name', 'phone'])
#     for name, phone in more_18_progress_more_75_sort:
#         writer.writerow([name, phone])


# my try, but it is not wor
# import json
# import datetime
#
# with open('pools.json', 'r', encoding='utf-8') as json_file:
#     content = json.load(json_file)
#
#     working_hours = {}
#
#     for row in content:
#         import pytz
#
#         tz_info = pytz.FixedOffset(-60)
#         pool_time = datetime.datetime.strptime(row['WorkingHoursSummer']['Понедельник'][:-6], '%H:%M').time().replace(
#             tzinfo=tz_info)
#         if datetime.time(10, 0) <= pool_time <= datetime.time(12, 0) and row['DimensionsSummer']['Length'] == max(
#                 row['DimensionsSummer']['Length'], row['DimensionsSummer']['Width']):
#             working_hours[row['DimensionsSummer']['Length'], 'x', row['DimensionsSummer']['Width']] = row['Address']
#
# print(working_hours)

# import json
# from datetime import datetime
#
# # Чтение данных из файла pools.json
# with open('pools.json', 'r', encoding='utf-8') as file:
#     pools_data = json.load(file)
#
#
# # Функция для проверки, подходит ли бассейн по времени
# def is_pool_open_at_time(pool, time):
#     open_time = datetime.strptime(pool['WorkingHoursSummer']['Понедельник'].split('-')[0], '%H:%M').time()
#     close_time = datetime.strptime(pool['WorkingHoursSummer']['Понедельник'].split('-')[1], '%H:%M').time()
#     return open_time <= time <= close_time
#
#
# # Находим подходящий бассейн
# suitable_pool = None
# max_length = 0
# max_width = 0
#
# for pool in pools_data:
#     if is_pool_open_at_time(pool, datetime.strptime('10:00', '%H:%M').time()):
#         if pool['DimensionsSummer']['Length'] > max_length or (
#                 pool['DimensionsSummer']['Length'] == max_length and pool['DimensionsSummer']['Width'] > max_width):
#             max_length = pool['DimensionsSummer']['Length']
#             max_width = pool['DimensionsSummer']['Width']
#             suitable_pool = pool
#
# # Выводим размеры и адрес подходящего бассейна
# if suitable_pool:
#     print(f"{max_length}x{max_width}")
#     print(suitable_pool['Address'])


# import json
#
# with open('food_services.json', 'r', encoding='utf-8') as json_file:
#     content = json.load(json_file)
#
#     max_cafe_district = {}
#     max_cafe_in_network = {}
#
#     for row in content:
#         district = row['District']
#         name_company = row['OperatingCompany']
#
#         if district in max_cafe_district:
#             max_cafe_district[district] += 1
#         else:
#             max_cafe_district[district] = 1
#
#         if name_company and row['IsNetObject'] == 'да':
#             if name_company in max_cafe_in_network:
#                 max_cafe_in_network[name_company] += 1
#             else:
#                 max_cafe_in_network[name_company] = 1
#
#     max_district = max(max_cafe_district.items(), key=lambda x: x[1])
#     max_network = max(max_cafe_in_network.items(), key=lambda x: x[1])
#
#     print(f"{max_district[0]}: {max_district[1]}")
#     print(f"{max_network[0]}: {max_network[1]}")

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     zip_file.printdir()


# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)
#     print(info[6].compress_size)
#     print(info[6].filename)
#     print(info[6].date_time)

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[0].is_dir())
#     print(info[6].is_dir())

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(*info, sep='\n')

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     last_file = zip_file.getinfo(info[-4])
#     print(last_file.file_size)
#     print(last_file.compress_size)
#     print(last_file.filename)
#     print(last_file.date_time)

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read())

# my solution
# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.namelist()
#
#     cnt = 0
#     for i in info:
#         if i[-1] != '/':
#             cnt += 1
#
# print(cnt)

# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#
#     file_count = 0
#     for item in info:
#         if not item.is_dir():    # проверяем папка или нет
#             file_count += 1
#
# print(file_count)

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#
#     cnt_file = 0
#     cnt_compress = 0
#     for i in info:
#         cnt_file += i.file_size
#         cnt_compress += i.compress_size
#
# print(f"Объем исходных файлов: {cnt_file} байт(а)")
# print(f"Объем сжатых файлов: {cnt_compress} байт(а)")

# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#
#     compression_ratio = {i: (i.compress_size / i.file_size) * 100 for i in info if i.file_size != 0}
#     min_file = min(compression_ratio, key=compression_ratio.get)
#     print(min_file.filename.split('/')[-1])

# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#
#     date = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
#
#     dates_more_now_date = []
#
#     for i in info:
#         date_time_str = ' '.join(map(str, i.date_time))
#         now_date = datetime.strptime(date_time_str, '%Y %m %d %H %M %S')
#
#         if now_date > date:
#             dates_more_now_date.append(i.filename)
#
#     sort_dates_more_now_date = sorted(dates_more_now_date, key=lambda x: x.split('/')[-1])
#
#     for i in sort_dates_more_now_date:
#         if i.split('/')[-1] != '':
#             print(i.split('/')[-1])

# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     print(len(info))
#
#     sort_info = sorted(info, key=lambda x: x.filename.split('/')[-1])
#
#     cnt = 0
#     for i in sort_info:
#         cnt += 1
#         if i.filename.split('/')[-1] != '':
#             print(i.filename.split('/')[-1])
#
#             date = datetime(*i.date_time).strftime('%Y-%m-%d %H:%M:%S')
#             print(f"  Дата модификации файла: {date}")
#
#             print(f"  Размер исходного файла: {i.file_size} байт(а)")
#             print(f"  Размер сжатого файла: {i.compress_size} байт(а)")
#             if cnt != 25:
#                 print()

# from zipfile import ZipFile
#
# file_names = [
#     'how to prove.pdf', 'fipi_demo_2022.pdf',
#     'Hollow Knight Silksong.exe',
#     'code.jpeg', 'stepik.png', 'readme.txt',
#     'shopping_list.txt',
#     'Alexandra Savior – Crying All the Time.mp3',
#     'homework.py', 'test.py'
# ]
#
# with ZipFile('files.zip', 'w') as zip_file:
#     for file_name in file_names:
#         zip_file.write(file_name)

# from zipfile import ZipFile
# import os.path
#
# file_names = [
#     'how to prove.pdf',
#     'fipi_demo_2022.pdf',
#     'Hollow Knight Silksong.exe',
#     'code.jpeg',
#     'stepik.png',
#     'readme.txt',
#     'shopping_list.txt',
#     'Alexandra Savior – Crying All the Time.mp3',
#     'homework.py', 'test.py'
# ]
#
# with ZipFile('files.zip', 'w') as zip_file:
#     for file_name in file_names:
#         if os.path.getsize(file_name) <= 100:
#             zip_file.write(file_name)

# import zipfile
#
#
# def extract_this(zip_name, *args):
#     with zipfile.ZipFile(zip_name) as zip_file:
#         if not args:
#             zip_file.extractall()
#         else:
#             for arg in args:
#                 zip_file.extract(arg)

# import pickle
# import sys
#
# # Считываем название pickle файла
# pickle_file = input().strip()
#
# # Загружаем функцию из pickle файла
# with open(pickle_file, 'rb') as file:
#     loaded_func = pickle.load(file)
#
# # Считываем аргументы для функции из потокового ввода
# args = [line.strip() for line in sys.stdin]
#
# # Вызываем загруженную функцию с аргументами
# result = loaded_func(*args)
#
# # Выводим результат
# print(result)

# import pickle
#
#
# def filter_dump(filename, objects, typename):
#     filtered_objects = [obj for obj in objects if isinstance(obj, typename)]
#     with open(filename, 'wb') as file:
#         pickle.dump(filtered_objects, file)

# import pickle
#
# # Считываем название pickle файла и целое число
# pickle_file = input().strip()
# checksum = int(input().strip())
#
# # Загружаем объект из pickle файла
# with open(pickle_file, 'rb') as file:
#     data = pickle.load(file)
#
# # Вычисляем контрольную сумму в соответствии с правилами
# if isinstance(data, dict):
#     keys_sum = sum(key for key in data.keys() if isinstance(key, int))
#     if keys_sum == checksum:
#         print("Контрольные суммы совпадают")
#     else:
#         print("Контрольные суммы не совпадают")
# elif isinstance(data, list):
#     int_elements = [elem for elem in data if isinstance(elem, int)]
#     if len(int_elements) >= 2:
#         min_elem = min(int_elements)
#         max_elem = max(int_elements)
#         checksum_calc = min_elem * max_elem
#     else:
#         checksum_calc = 0
#     if checksum_calc == checksum:
#         print("Контрольные суммы совпадают")
#     else:
#         print("Контрольные суммы не совпадают")
# else:
#     print("Объект в pickle файле не является словарем или списком с целочисленными элементами")
