year = input('Рік високосний? (Так/Ні): ')


def get_hours():
    if year == 'Так':
        return 366 * 24

    else:
        return 365 * 24


def get_minutes(number):
    return number * 60


def get_seconds(number2):
    print(number2 * 60)


get_seconds(get_minutes(get_hours()))