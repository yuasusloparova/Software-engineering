numbers = [2, 4, 6, 8, 10, 11, 12]
flag = False

for num in numbers:
    if num % 2 != 0:
        flag = True
        break

if flag:
    print("В массиве есть нечетное число")
else:
    print("В массиве все числа четные")
