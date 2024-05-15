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
