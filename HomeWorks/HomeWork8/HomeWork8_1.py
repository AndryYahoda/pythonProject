# Task 1
# print('Поділ з залишком повертає залишок від ділення двох чисел.')
# Task 2
# print('Цілий поділ виконує ділення двох чисел і повертає цілу частину результату, відкидаючи дробову частину')
# Task 3
# import random
# number_of_symbols = int(input("Enter number of symbols for generation: "))
# i = 0
# result = []
# all_symbols = 'ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstvxyz1234567890'
# for i in range(number_of_symbols):
#     symbol = random.choice(all_symbols)
#     result.append(symbol)
# result_as_string = ''.join(result)
# print(result_as_string)
# Task 4
# import math
# input1 = float(input('Enter first number: '))
# print(math.fmod(input1, 2))
# if math.fmod(input1, 2) == 0:
#     print("This is paired number")
# else:
#     print("This is unpaired number")
# Task 5
# from datetime import datetime
# current_dt = datetime.now()
# print("Поточний час", current_dt)
# Task 6
# from datetime import datetime, timedelta, date
#
# name = input("Введіть ваше ім'я: ")
# dob_str = input("Введіть дату народження у форматі YYYY-MM-DD: ")
# dob = datetime.strptime(dob_str, "%Y-%m-%d")
# current_date = datetime.now()
#
# if current_date.month > dob.month or (current_date.month == dob.month and current_date.day > dob.day):
#     next_birthday_year = current_date.year + 1
# else:
#     next_birthday_year = current_date.year
#
# next_birthday = datetime(next_birthday_year, dob.month, dob.day)
# days_difference = (next_birthday - current_date).days
# print(f"Привіт, {name}! До вашого наступного дня народження залишилося {days_difference} днів.")

# Task 7
# import random
# first_names = ['Andrii', 'Bogdan', 'Ostap', 'Ivan', 'Petro']
# last_names = ['Sirko', 'Shtanko', 'Mogyla', 'Pes', 'Soroka']
# user_first_name = first_names[random.randint(0, len(first_names)-1)]
# user_last_name = last_names[random.randint(0, len(last_names)-1)]
# print(user_first_name + ' ' + user_last_name)
# Task 8
# from datetime import datetime, timedelta, date
#
# date1_str = input("Введіть дату у форматі YYYY-MM-DD: ")
# date2_str = input("Введіть дату у форматі YYYY-MM-DD: ")
# date1 = datetime.strptime(date1_str, "%Y-%m-%d")
# date2 = datetime.strptime(date2_str, "%Y-%m-%d")
# if date1 > date2:
#     print('Difference in seconds: ', (date1 - date2).total_seconds())
# elif date1 < date2:
#     print('Difference in seconds: ', (date2 - date1).total_seconds())
# else:
#     print('date1 equals date2')
# Task 9
# import sys
# print(sys.argv)
# Task 10
# import time
#
# timer = int(input('What is the starting time? '))
# for k in range(timer):
#     time.sleep(1)
#     print(timer)
#     timer -= 1
#     if timer == 0:
#         print('The end')
#         break


