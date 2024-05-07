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
