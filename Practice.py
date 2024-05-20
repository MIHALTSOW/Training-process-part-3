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
