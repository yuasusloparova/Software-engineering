num = int(input("Введите число от 0 до 10: "))
if not 0 <= num <= 10:
    print("Число не в диапазоне от 0 до 10")
else:
    if num <= 3:
        print("от 0 до 3 включительно")
    elif num <= 6:
        print("от 3 до 6")
    else:
        print("от 6 до 10 включительно")
