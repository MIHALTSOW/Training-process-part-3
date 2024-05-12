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


# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)


# from datetime import datetime
#
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
#
# print(datetime.fromtimestamp(seconds))
#
# print(dt.timestamp())


# from datetime import datetime
#
# times_of_purchases = [
#     datetime(2017, 10, 1, 12, 23, 25),
#     datetime(2017, 10, 1, 15, 26, 26),
#     datetime(2017, 10, 1, 15, 42, 57),
#     datetime(2017, 10, 1, 17, 49, 59),
#     datetime(2017, 10, 2, 6, 37, 10),
#     datetime(2017, 10, 2, 6, 42, 53),
#     datetime(2017, 10, 2, 8, 56, 45),
#     datetime(2017, 10, 2, 9, 18, 3),
#     datetime(2017, 10, 2, 12, 23, 48),
#     datetime(2017, 10, 2, 12, 45, 5),
#     datetime(2017, 10, 2, 12, 48, 8),
#     datetime(2017, 10, 2, 12, 10, 54),
#     datetime(2017, 10, 2, 19, 18, 10),
#     datetime(2017, 10, 2, 12, 31, 45),
#     datetime(2017, 10, 3, 20, 57, 10),
#     datetime(2017, 10, 4, 7, 4, 57),
#     datetime(2017, 10, 4, 7, 13, 31),
#     datetime(2017, 10, 4, 7, 13, 42),
#     datetime(2017, 10, 4, 7, 21, 54),
#     datetime(2017, 10, 4, 14, 22, 12),
#     datetime(2017, 10, 4, 14, 50),
#     datetime(2017, 10, 4, 15, 7, 27),
#     datetime(2017, 10, 4, 12, 44, 49),
#     datetime(2017, 10, 4, 12, 46, 41),
#     datetime(2017, 10, 4, 16, 32, 33),
#     datetime(2017, 10, 4, 16, 34, 44),
#     datetime(2017, 10, 4, 16, 46, 59),
#     datetime(2017, 10, 4, 12, 26, 6)
# ]
#
# more_than_12 = 0
# less_than_12 = 0
#
# for time in times_of_purchases:
#     if time.hour > 12:
#         more_than_12 += 1
#     elif time.hour < 12:
#         less_than_12 += 1
#
# if more_than_12 > less_than_12:
#     print('После полудня')
# else:
#     print('До полудня')

# second variant
# res = 0
# for i in times_of_purchases:
#     if i.hour >= 12:
#         res += 1
#     else:
#         res -= 1
#
# print(('После', 'До')[res < 0], 'полудня')


# from datetime import date, time, datetime
#
# dates = [
#     date(1793, 8, 23),
#     date(1410, 3, 11),
#     date(804, 11, 12),
#     date(632, 6, 4),
#     date(295, 1, 23),
#     date(327, 8, 24),
#     date(167, 4, 16),
#     date(229, 1, 24),
#     date(1239, 2, 5),
#     date(1957, 7, 14),
#     date(197, 8, 24),
#     date(479, 9, 6)
# ]
#
# times = [
#     time(7, 33, 27),
#     time(21, 2, 10),
#     time(17, 20, 47),
#     time(20, 8, 59),
#     time(12, 42, 56),
#     time(15, 9, 57),
#     time(17, 47, 9),
#     time(9, 40, 2),
#     time(11, 47, 1),
#     time(17, 27, 10),
#     time(17, 55, 40),
#     time(9, 14, 9)
# ]
#
# all_time_date = []
# for time, date in zip(times, dates):
#     date_and_time = all_time_date.append(datetime.combine(date, time))
#
# print(*sorted(all_time_date, key=lambda x: x.second), sep='\n')

# from datetime import datetime

# data = {
#     'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#     'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#     'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#     'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#     'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#     'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#     'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#     'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#     'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#     'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#     'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')
# }

# print(max(data, key=lambda x: datetime.strptime(data[x][1], '%d.%m.%Y %H:%M:%S') - datetime.strptime(data[x][0],
#                                                                                                      '%d.%m.%Y %H:%M:%S')))
# worktime = {}
# for key, value in data.items():
#     worktime[key] = (
#             datetime.strptime(value[1], '%d.%m.%Y %H:%M:%S') - datetime.strptime(value[0], '%d.%m.%Y %H:%M:%S'))
#
# print(max(worktime, key=worktime.get))


# doubtful, but okay

# from datetime import datetime, timedelta
#
#
# def is_available_date(booked_dates, date_for_booking):
#     def parse_date(date_str):
#         return datetime.strptime(date_str, '%d.%m.%Y')
#
#     def is_date_booked(date, booked_dates):
#         for booked_date in booked_dates:
#             if '-' in booked_date:
#                 start_date_str, end_date_str = booked_date.split('-')
#                 start_date = parse_date(start_date_str)
#                 end_date = parse_date(end_date_str)
#                 if start_date <= date <= end_date:
#                     return True
#             else:
#                 if date == parse_date(booked_date):
#                     return True
#         return False
#
#     if '-' in date_for_booking:
#         start_date_str, end_date_str = date_for_booking.split('-')
#         start_date = parse_date(start_date_str)
#         end_date = parse_date(end_date_str)
#         current_date = start_date
#         while current_date <= end_date:
#             if is_date_booked(current_date, booked_dates):
#                 return False
#             current_date += timedelta(days=1)
#     else:
#         if is_date_booked(parse_date(date_for_booking), booked_dates):
#             return False
#
#     return True
#
#
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))
#
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021-04.11.2021'
# print(is_available_date(dates, some_date))
#
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '06.11.2021'
# print(is_available_date(dates, some_date))


# from datetime import datetime, timedelta
#
# dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
#
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))


# from datetime import date, timedelta
#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days = (birthday - today).days
# print(days)


# my solution

# from datetime import timedelta, date, datetime
#
# date_str = input()
# date_input = datetime.strptime(date_str, '%d.%m.%Y').date()
#
#
# def print_date_after_before(date1):
#     date_before = date1 - timedelta(days=1)
#     date_after = date1 + timedelta(days=1)
#     date_before = date_before.strftime('%d.%m.%Y')
#     date_after = date_after.strftime('%d.%m.%Y')
#     print(date_before, date_after, sep='\n')
#
#
# print_date_after_before(date_input)


# teacher solution

# from datetime import datetime, timedelta
#
# pattern, td = '%d.%m.%Y', timedelta(days=1)
#
# dt = datetime.strptime(input(), pattern)
#
# print((dt - td).strftime(pattern))
# print((dt + td).strftime(pattern))


# my solution
# from datetime import timedelta
#
# input_time = input()
# hours, minutes, seconds = map(int, input_time.split(':'))
# delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
#
#
# def second_by_time(times):
#     total_seconds = times.total_seconds()
#     print(int(total_seconds))
#
#
# second_by_time(delta)

# teacher solution

# from datetime import timedelta
#
# h, m, s = map(int, input().split(':'))
#
# td = timedelta(hours=h, minutes=m, seconds=s)
#
# print(int(td.total_seconds()))

# my solution

# from datetime import timedelta, datetime
#
# h, m, s = map(int, input().split(':'))
# start_timer = timedelta(hours=h, minutes=m, seconds=s)
#
# length_timer = timedelta(seconds=int(input()))
#
#
# def timer(start, length):
#     total_time = start + length
#     total_seconds = total_time.total_seconds() % (24 * 3600)
#     total_time = timedelta(seconds=total_seconds)
#
#     # Convert timedelta to datetime for formatting
#     base_datetime = datetime(1, 1, 1)  # Base date for timedelta conversion
#     formatted_time = (base_datetime + total_time).time()
#     print(formatted_time.strftime("%H:%M:%S"))
#
#
# timer(start_timer, length_timer)


# teacher solution

# from datetime import timedelta, datetime
#
# pattern = '%H:%M:%S'
# dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))
#
# print(dt.strftime(pattern))


# from datetime import datetime
#
#
# def num_of_sundays(year):
#     count = 0
#     for month in range(1, 13):
#         for day in range(1, 32):
#             try:
#                 date_obj = datetime(year, month, day)
#                 if date_obj.weekday() == 6:
#                     count += 1
#             except ValueError:
#                 break
#     return count
#
#
# # Example usage
# year = 2022
# print(num_of_sundays(year))


# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# date_correct = datetime.strptime(input(), pattern)
#
#
# def write_10_tasks(start_date):
#     print(start_date.strftime(pattern), sep='\n')
#     for i in range(2, 11):
#         start_date += timedelta(days=i)
#         print(start_date.strftime(pattern), sep='\n')
#
#
# write_10_tasks(date_correct)


# my solution

# from datetime import datetime
#
#
# def days_between_dates(date1, date2):
#     pattern = '%d.%m.%Y'
#     date1 = datetime.strptime(date1, pattern)
#     date2 = datetime.strptime(date2, pattern)
#     delta = date2 - date1
#     return delta.days
#
#
# split_date = [i for i in input().split(' ')]
#
# total_date = []
# for i in range(len(split_date)):
#     try:
#         total_date.append(abs(days_between_dates(split_date[i], split_date[i + 1])))
#     except IndexError:
#         break
# print(total_date)

# teacher solution

# from datetime import datetime
#
# dates = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]
#
# diffs = [abs(dates[i] - dates[i - 1]).days for i in range(1, len(dates))]
#
# print(diffs)


# this code uncorrected
# def fill_up_missing_dates(dates):
#     date_list = []
#     pattern = '%d.%m.%Y'
#
#     mxDate, mnDate = max(dates), min(dates)
#     mxDate, mnDate = datetime.strptime(mxDate, pattern), datetime.strptime(mnDate, pattern)
#
#     delta = mxDate - mnDate
#     all_dates = [mnDate + timedelta(days=i) for i in range(delta.days + 1)]
#
#     for date in all_dates:
#         date_list.append(datetime.strftime(date, pattern))
#
#     return date_list

# let's try update this code

# from datetime import datetime, timedelta


# def fill_up_missing_dates(dates):
#     date_list = []
#
#     pattern = '%d.%m.%Y'
#     dates = sorted(dates, key=lambda x: datetime.strptime(x, pattern))
#
#     start_date = datetime.strptime(dates[0], pattern)
#     end_date = datetime.strptime(dates[-1], pattern)
#     delta = (end_date - start_date).days
#
#     for i in range(delta + 1):
#         date = start_date + timedelta(days=i)
#         date_list.append(datetime.strftime(date, pattern))
#
#     return date_list
#
#
# dates = ['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']
# print(len(fill_up_missing_dates(dates)))

# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
# print(fill_up_missing_dates(dates))


# dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
# print(fill_up_missing_dates(dates))


# from datetime import datetime, timedelta
#
# # Input start and end times
# start_time = datetime.strptime(input(), '%H:%M')
# end_time = datetime.strptime(input(), '%H:%M')
#
#
# def generate_schedule(start_time, end_time):
#     lesson_duration = timedelta(minutes=45)
#     break_time = timedelta(minutes=10)
#
#     current_time = start_time
#     while current_time + lesson_duration <= end_time:
#         print(f'{current_time.strftime("%H:%M")} - {(current_time + lesson_duration).strftime("%H:%M")}')
#         current_time += lesson_duration + break_time
#
#
# if end_time - start_time >= timedelta(minutes=45):
#     generate_schedule(start_time, end_time)


# my solution
# from datetime import date, time, datetime, timedelta
#
# data = [
#     ('07:14', '08:46'),
#     ('09:01', '09:37'),
#     ('10:00', '11:43'),
#     ('12:13', '13:49'),
#     ('15:00', '15:19'),
#     ('15:58', '17:24'),
#     ('17:57', '19:21'),
#     ('19:30', '19:59')
# ]
#
#
# def minutes_for_all_tasks(data):
#     all_minutes = []
#     pattern = '%H:%M'
#     for i in data:
#         start, end = datetime.strptime(i[0], pattern), datetime.strptime(i[1], pattern)
#         all_minutes.append((end - start).seconds // 60)
#     return print(sum(all_minutes))
#
#
# minutes_for_all_tasks(data)

# teacher solution

# from datetime import date, time, datetime, timedelta
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# seconds = 0
#
# for i in data:
#     start, end = [datetime.strptime(x, '%H:%M') for x in i]
#     seconds += (end - start).total_seconds()
#
# print(int(seconds // 60))


# most difficult task

# from datetime import datetime, timedelta
#
#
# def count_13th_weekday():
#     week = {
#         0: 0,
#         1: 0,
#         2: 0,
#         3: 0,
#         4: 0,
#         5: 0,
#         6: 0
#     }
#
#     start_count = datetime.strptime('01.01.0001', '%d.%m.%Y')
#     end_count = datetime.strptime('31.12.9999', '%d.%m.%Y')
#     delta = (end_count - start_count).days
#
#     for i in range(delta + 1):
#         date = start_count + timedelta(days=i)
#         if date.day == 13:
#             week[date.weekday()] += 1
#
#     print(*week.values(), sep='\n')
#
#
# count_13th_weekday()


# from datetime import datetime
#
# workingtime = {
#     'Monday': '9:00 - 21:00',
#     'Tuesday': '9:00 - 21:00',
#     'Wednesday': '9:00 - 21:00',
#     'Thursday': '9:00 - 21:00',
#     'Friday': '9:00 - 21:00',
#     'Saturday': '10:00 - 18:00',
#     'Sunday': '10:00 - 18:00'
# }
#
# date_str, time_str = input('Enter date and time in format dd.mm.yyyy HH:MM: ').split()
# date_time = datetime.strptime(date_str + ' ' + time_str, '%d.%m.%Y %H:%M')
# day_week = date_time.weekday()
#
# for key, value in workingtime.items():
#     if day_week == list(workingtime.keys()).index(key):
#         start = datetime.strptime(value.split(' - ')[0], '%H:%M').time()
#         end = datetime.strptime(value.split(' - ')[1], '%H:%M').time()
#         if start <= date_time.time() < end:
#             remaining_minutes = (end.hour - date_time.hour) * 60 + (end.minute - date_time.minute)
#             print(remaining_minutes)
#         else:
#             print('Магазин не работает')


# from datetime import datetime, timedelta
#
# num = 3
# num = int(input())

# input_date = ['Иван Петров 01.05.1995', 'Петр Сергеев 29.04.1995', 'Сергей Иванов 01.01.1996']

# input_date = ['Иван Петров 01.05.1995', 'Петр Сергеев 29.05.1995', 'Сергей Иванов 01.05.1995']

# input_date = [
#     'Анна Цивинская 12.08.2000',
#     'Сослан Найфонов 12.08.2000',
#     'Фатима Бекузарова 12.08.2000',
#     'Геор Гагиев 12.08.2000',
#     'Аслан Короев 12.08.2000',
#     'Владимир Чен 12.08.2000'
# ]

# input_date = [input() for _ in range(num)]
# print(input_date)

# dict_time = {}
#
# for i in input_date:
#     name, second_name, date = i.split()
#     date = datetime.strptime(date, '%d.%m.%Y')
#     dict_time[name + ' ' + second_name] = date
#
# mn_time_key = min(dict_time, key=dict_time.get)
# mn_time_value = dict_time[mn_time_key]
#
# if len(set(dict_time.values())) == len(dict_time.values()):
#     print(mn_time_value.strftime('%d.%m.%Y'), mn_time_key)
# else:
#     print(mn_time_value.strftime('%d.%m.%Y'), (len(dict_time.values()) - len(set(dict_time.values()))) + 1)

# from datetime import datetime

# input_date = [
#     'Иван Петров 01.05.1995',
#     'Петр Сергеев 29.04.1995',
#     'Сергей Романов 01.01.1996',
#     'Роман Григорьев 01.01.1996',
#     'Григорий Иванов 01.05.1995'
# ]

# input_date = [
#     'Иван Петров 14.10.1995',
#     'Петр Сергеев 29.04.1992',
#     'Сергей Романов 01.01.1994',
#     'Роман Григорьев 01.01.1994',
#     'Григорий Иванов 16.07.1995'
# ]

# input_date = [
#     'Иван Петров 04.05.1995',
#     'Петр Сергеев 04.05.1995',
#     'Сергей Романов 01.02.1993',
#     'Роман Григорьев 01.02.1993',
#     'Григорий Иванов 06.07.1999',
#     'Тимур Гуев 06.07.1999'
# ]

# dict_time = {}
#
# for i in input_date:
#     name, second_name, date = i.split()
#     date = datetime.strptime(date, '%d.%m.%Y')
#     dict_time[name + ' ' + second_name] = date
#
# mn_time_key = min(dict_time, key=dict_time.get)
# mn_time_value = dict_time[mn_time_key]
#
# born_more_employees = {}
#
# for key, value in dict_time.items():
#     born_more_employees[value] = born_more_employees.get(value, 0) + 1
#
# for key, value in sorted(born_more_employees.items()):
#     if value == max(born_more_employees.values()):
#         print(key.strftime('%d.%m.%Y'))


# import time
#
# start_time = time.monotonic()
#
# for i in range(5):
#     print(i)
#     time.sleep(0.5)
#
# end_time = time.monotonic()
#
# elapsed_time = end_time - start_time
# print(f"Program finished in {elapsed_time:.2f} seconds")


# import time
#
#
# def calculate_it(func, *args):
#     start_time = time.perf_counter()
#     result = func(*args)
#     end_time = time.perf_counter()
#     elapsed_time = end_time - start_time
#
#     return print((result, elapsed_time))
#
#
# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c
#
#
# calculate_it(add, 1, 2, 3)


# import time
#
#
# def add(a, b, c):
#     time.sleep(2)
#     return a + b + c
#
#
# def add1(a, b, c):
#     time.sleep(2)
#     return a + b + c
#
#
# def add2(a, b, c):
#     time.sleep(1)
#     return a + b + c
#
#
# func_list = [add, add1, add2]
#
#
# def get_the_fastest_func(funcs, *args):
#     time_list = {}
#     for func in funcs:
#         start_time = time.perf_counter()
#         func(*args)
#         end_time = time.perf_counter()
#         time_list[func.__name__] = end_time - start_time
#
#     return min(time_list, key=time_list.get)
#
#
# fastest_func_name = get_the_fastest_func(func_list, 1, 2, 3)
# print(f"The fastest function is {fastest_func_name}")


# from math import factorial
# import time
#
# start_time = time.perf_counter()
# factorial(10)
# end_time = time.perf_counter()
#
# print(f'modul math: {end_time - start_time}')
#
#
# def factorial_recurrent(n):
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)
#
#
# start_time = time.perf_counter()
# factorial_recurrent(10)
# end_time = time.perf_counter()
#
# print(f'recurrent: {end_time - start_time}')
#
#
# def factorial_classic(n):
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# start_time = time.perf_counter()
# factorial_classic(10)
# end_time = time.perf_counter()
#
# print(f'classic: {end_time - start_time}')


# import time
#
#
# def for_and_append():
#     iterations = 10_000_000
#     result = []
#     for i in range(iterations):
#         result.append(i + 1)
#     return result
#
#
# def list_comprehension():
#     iterations = 10_000_000
#     return [i + 1 for i in range(iterations)]
#
#
# start_time = time.perf_counter()
# for_and_append()
# end_time = time.perf_counter()
#
# print(f'append: {end_time - start_time}')
#
# start_time = time.perf_counter()
# list_comprehension()
# end_time = time.perf_counter()
#
# print(f'list: {end_time - start_time}')


# import time
#
# iterable = [i for i in range(10)]
#
#
# def for_and_append(iterable):
#     result = []
#     for elem in iterable:
#         result.append(elem)
#     return result
#
#
# def list_comprehension(iterable):
#     return [elem for elem in iterable]
#
#
# def list_function(iterable):
#     return list(iterable)
#
#
# def get_the_fastest_func(funcs, arg):
#     time_list = {}
#     for func in funcs:
#         start_time = time.perf_counter()
#         func(arg)
#         end_time = time.perf_counter()
#         time_list[func.__name__] = end_time - start_time
#
#     return min(time_list, key=time_list.get)
#
#
# func_list = [for_and_append, list_comprehension]
#
# for i in range(10):
#     print(get_the_fastest_func(func_list, iterable))
