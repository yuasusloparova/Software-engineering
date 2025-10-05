def calculate_average(x, *args):
    total_sum = x + sum(args)
    count = 1 + len(args)
    average = total_sum / count
    
    print(f"Первый аргумент: {x}")
    print(f"Сумма остальных аргументов: {sum(args)}")
    print(f"Количество всех аргументов: {count}")
    print(f"Среднее арифметическое: {average}")
    
    return average

if __name__ == '__main__':
    result = calculate_average(10, 2, 4, 6, 8)
    print(f"\nИтоговый результат: {result}")
