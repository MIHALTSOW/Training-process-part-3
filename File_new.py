# from re import split
# from sys import stdin
#
# input_number = stdin.read().split('\n')
#
# for number in input_number:
#     country_code, city_code, phone_number = split(r"[- ]", number)
#     print(f"Код страны: {country_code}, Код города: {city_code}, Номер: {phone_number}")


# from re import search
# from sys import stdin
#
# input_login = stdin.read().split('\n')
#
# for login in input_login:
#     if search(r"\b^\_\d{1,}[a-zA-Z]{0,}\_?\b", login):
#         print(True)
#     else:
#         print(False)

# from re import search
# from sys import stdin
#
# words = stdin.read().split('\n')
#
# for word in words:
#     if search(r"\b(\w+)\1\b", word):
#         print(word)


# from re import search, IGNORECASE
#
# letter = input()
#
# if search(r"^(Добрый день|Здравствуйте|Доброе утро|Добрый вечер)", letter, flags=IGNORECASE):
#     print(True)
# else:
#     print(False)


# article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!
#
# Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
# В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...
#
# На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
# Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью.
#
# Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.
# Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!
#
# Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...
#
# Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''
#
# from re import IGNORECASE, search
#
# start_Stepik = 0
# end_three_nots = 0
#
# for word in article.split('\n'):
#     if search(r"^Stepik", word, flags=IGNORECASE):
#         start_Stepik += 1
#
# for word in article.split('\n'):
#     if search(r"\.\.\.$|\!$", word):
#         end_three_nots += 1
#
# print(start_Stepik)
# print(end_three_nots)

from re import findall

string = input()
word_input = input()

for word in string:
    needed_word = findall(r"word_input", word)

print(needed_word)
