# list = ['червоний', 'помаранчевий', 'жовтий', 'зелений', 'блакитний', 'синій', 'фіолетовий']
# i = 0
# for color in list:
#     i += 1
#     print(f"{i}-ий колір {color}")
a = float(input('Введіть число a: '))
b = float(input('Введіть число b: '))


def get_summ(x, y):
    suma = x + y
    print('Сума двох чисел ', suma)


def get_diff(x, y):
    print('Різниця чисел ', x - y)


def get_mult(x, y):
    print('Добуток чисел ', x * y)


def get_divv(x, y):
    if y == 0:
        print('Ділення на нуль')
    else:
        print('Частка двох чисел ', x / y)


get_summ(a, b)
get_diff(a, b)
get_mult(a, b)
get_divv(a, b)
