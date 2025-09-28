string = "программирование"
value = input('Введите символ для поиска: ')
found = False

for char in string:
    if char == value:
        print(f"Символ '{value}' найден в строке")
        found = True
        break
else:
    print(f"Символ '{value}' не найден в строке")
