

from datetime import date


day = int(input("Введите день\n"))
mouth = int(input("Введите месяц\n"))
year = int(input("Введите год\n"))

def examination(year, mouth, day):
    try:
        date(year, mouth, day)
        return True
    except:
        return False


print(examination(year, mouth, day))


