
class TooYoungError(Exception):
    pass

def check_age_for_driving(age):
    if age < 18:
        raise TooYoungError("Тебе еще рано водить машину!")
    else:
        print("Можно водить машину!")

def check_age_for_alcohol(age):
    if age < 21:
        raise TooYoungError("Тебе еще рано пить алкоголь!")
    else:
        print("Можно покупать алкоголь!")

print("=== Проверка возраста для вождения ===")
try:
    check_age_for_driving(16) 
except TooYoungError as e:
    print(f"Ошибка: {e}")

try:
    check_age_for_driving(20) 
except TooYoungError as e:
    print(f"Ошибка: {e}")

print("\n=== Проверка возраста для алкоголя ===")
try:
    check_age_for_alcohol(19) 
except TooYoungError as e:
    print(f"Ошибка: {e}")

try:
    check_age_for_alcohol(25) 
except TooYoungError as e:
    print(f"Ошибка: {e}")
