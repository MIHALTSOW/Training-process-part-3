# Time and date theory

# my_date = date(1999, 11, 18)
# my_date = date(day=18, month=11, year=1999)
#
# print(my_date)
# print(type(my_date))

# print('Year =', my_date.year)
# print('Month =', my_date.month)
# print('Day =', my_date.day)

# creation_date = date.today()
# print(creation_date)

# date1 = date.fromordinal(366)
# date2 = date(1999, 12, 26)
#
# print(date1)
# print(date2.toordinal())

# my_time = time(11, 20, 54, 1234)
# print(my_time)
# print(type(my_time))


# time1 = time(11, 20, 54, 1234)
# time2 = time(11, 20, 54)
# time3 = time(11, 20)
# time4 = time(11)
# time5 = time()
# time6 = time(minute=23, second=56)
#
# print(time1, time2, time3, time4, time5, sep='\n')
# print(time6)


# my_time = time(11, 20, 54, 1234)
#
# print('Hour =', my_time.hour)
# print('Minute =', my_time.minute)
# print('Second =', my_time.second)
# print('Microsecond =', my_time.microsecond)


# date1 = date(2022, 10, 15)
# date2 = date(1999, 12, 26)
#
# time1 = time(13, 10, 5)
# time2 = time(21, 32, 59)
#
# print(date1 < date2)
# print(time1 < time2)


# my_date = date(2021, 12, 31)
# my_time = time(11, 20, 54)
#
# print(my_date)
# print(my_time)
#
# print(str(my_date))
# print(str(my_time))
#
# print(repr(my_date))
# print(repr(my_time))


# my_set = {date(2021, 12, 31), date(2019, 3, 19), date(2022, 5, 25)}
#
# my_dict = {
#     date(2021, 12, 31): 'New year',
#     date(2030, 10, 6): 'Birthday'
# }
#
# print(my_set)
# print(my_dict)


# dates = [
#     date(2021, 12, 31),
#     date(2025, 3, 19),
#     date(2017, 5, 25)
# ]
#
# print(min(dates))
# print(max(dates))
# print(sorted(dates))


# date1 = date(1992, 10, 6)
# date2 = date1.replace(year=1995)
# date3 = date1.replace(month=12, day=17)
#
# print(date1)
# print(date2)
# print(date3)


# time1 = time(17, 10, 6)
# time2 = time1.replace(hour=21)
# time3 = time1.replace(minute=48, second=59)
#
# print(time1)
# print(time2)
# print(time3)


# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
#          date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
#          date(1666, 6, 6), date(1968, 5, 26)]

# def quarter(date):
#     if date.month <= 3:
#         return 'Q1'
#     elif date.month <= 6:
#         return 'Q2'
#     elif date.month <= 9:
#         return 'Q3'
#     else:
#         return 'Q4'

# def quarter(date):
#     quarter_num = (date.month - 1) // 3 + 1
#     return f'Q{quarter_num}'
#
#
# for i in dates:
#     print(f'{i.year}-{quarter(i)}')

# from datetime import date
#
#
# def get_min_max(dates):
#     if len(dates) == 0:
#         print(())
#     else:
#         mx = max(dates)
#         mn = min(dates)
#         print(tuple((mn, mx)))
#
# # dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
# # dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# # get_min_max(dates)

# my variant
#
#
# def get_date_range(date1, date2):
#     delta = date2 - date1
#     if delta.days == 0:
#         return [date1]
#
#     return [date1 + timedelta(days=i) for i in range(delta.days + 1)]
#
#
# date1 = date(2021, 10, 1)
# date2 = date(2021, 10, 5)
#
# print(*get_date_range(date1, date2), sep='\n')
#
#
# # teacher variant

# def get_date_range(start, end):
#     return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

# a = date(1999, 11, 18)
# b = a.toordinal()
#
# print(b)
#
# i = 730076
# print(date.fromordinal(i))


# from datetime import date, timedelta
#
#
# def saturdays_between_two_dates(date1, date2):
#     list_date = [date1, date2]
#     mx, mn = max(list_date), min(list_date)
#     current_date = mn
#     saturdays = 0
#     while current_date <= mx:
#         if current_date.weekday() == 5:
#             saturdays += 1
#         current_date += timedelta(days=1)
#     return saturdays
#
#
# date1 = date(2010, 6, 13)
# date2 = date(2011, 7, 14)
#
# print(saturdays_between_two_dates(date1, date2))


# information from 3.2

# from datetime import date, time

# my_date = date(2021, 8, 10)
# my_time = time(7, 18, 34)
#
# print(my_date)
# print(my_time)
#
# print(my_date.strftime('%d/%m/%y'))
# print(my_date.strftime('%a %d, %B %Y'))
# print(my_time.strftime('%H.%M.%S'))


# given_date = date(2021, 7, 17)
#
# print(given_date.strftime('%A %d %B %Y'))
# print(given_date.strftime('%Y/%m/%d'))
# print(given_date.strftime('%d.%m.%Y (%A, %B)'))
# print(given_date.strftime('Day of year: %j, week number: %U'))


# given_time = time(14, 4, 29)
#
# print(given_time.strftime('Hours: %H, minutes: %M, seconds: %S'))
# print(given_time.strftime('%H:%M:%S'))
# print(given_time.strftime('%I:%M:%S %p'))


# import locale
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#
# my_date = date(2021, 8, 10)
# print(my_date.strftime('%A %d, %B %Y'))


# from datetime import time
#
# alarm = time(7, 30, 25)
#
# print('Hours:', alarm.strftime('%H'))
# print('Minutes:', alarm.strftime('%M'))
# print('Seconds:', alarm.strftime('%S'))


# from datetime import date
#
# birthday = date(1999, 11, 18)
#
# print('Month name:', birthday.strftime('%B'))
# print('Day of week:', birthday.strftime('%A'))
# print('Year:', birthday.strftime('%Y'))
# print('Month:', birthday.strftime('%m'))
# print('Day:', birthday.strftime('%d'))


# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))
# print(andrew.strftime('%B (%Y)'))
# print(andrew.strftime('%Y-%j'))


# from datetime import date, time
#
# day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
# hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС').split(':')
#
# my_date = date(int(year), int(month), int(day))
# my_time = time(int(hour), int(minute), int(second))
#
# print(my_date)
# print(my_time)


# from datetime import date
#
# date1, date2 = date.fromisoformat(input()), date.fromisoformat(input())
#
#
# def min_max_dates(date_first, date_second):
#     if date_first < date_second:
#         print(date1.strftime('%d-%m (%Y)'))
#     else:
#         print(date2.strftime('%d-%m (%Y)'))
#
#
# min_max_dates(date1, date2)


# from datetime import date
#
# all_dates = [date.fromisoformat(input()) for _ in range(int(input()))]

# def output_ground_dates(dates):
#     sort_dates = sorted(dates)
#     for i in sort_dates:
#         print(i.strftime('%d/%m/%Y'))
#
#
# output_ground_dates(all_dates)


# from datetime import date

# def print_good_dates(all_dates):
#     sort_dates = sorted(all_dates)
#     for i in sort_dates:
#         if i.year == 1992 and int(i.month) + int(i.day) == 29:
#             print(i.strftime('%B %d, %Y'))


# maybe more compfortable solution
# def print_good_dates(all_dates):
#     for d in sorted(filter(lambda x: x.year == 1992 and x.month + x.day == 29, all_dates)):
#         print(d.strftime('%B %d, %Y'))
#
#
# dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
# print_good_dates(dates)
#
# dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
# print_good_dates(dates)

# from datetime import date

# this version not work good, don't use it

# def is_correct(day, month, year):
#     if month == 2 and day >= 29:
#         return False
#     return 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2999
#
# this version is good

# def is_valid_date(day, month, year):
#     try:
#         date(year, month, day)
#         return True
#     except ValueError:
#         return False
#
# print(is_correct(31, 12, 2021))
# print(is_correct(31, 13, 2021))
# print(is_correct(31, 2, 2021))

# more interesting solution (not recommend)

# def is_correct(day, month, year):
#     try:
#         date(year, month, day)
#         return True
#     except:
#         return False


# from datetime import date
#
#
# def is_valid_date(day, month, year):
#     try:
#         date(year, month, day)
#         return True
#     except ValueError:
#         return False
#
#
# def validate_dates():
#     cnt = 0
#     while True:
#         user_input = input()
#         if user_input == 'end':
#             break
#         parts = user_input.split('.')
#         if len(parts) != 3:
#             print('Некорректная')
#             continue
#         day, month, year = map(int, parts)
#         if is_valid_date(day, month, year):
#             print('Корректная')
#             cnt += 1
#         else:
#             print('Некорректная')
#     print(cnt)
#
#
# validate_dates()
