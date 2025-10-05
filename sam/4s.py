def calculate_average(*args):
   
    if len(args) == 0:
        return 0
    
   
    total_sum = sum(args)
   
    count = len(args)
    
    average = total_sum / count
    
   
    print(f"Полученные аргументы: {args}")
    print(f"Количество чисел: {count}")
    print(f"Сумма чисел: {total_sum}")
    print(f"Среднее арифметическое: {average:.2f}")
    
    return average

if __name__ == '__main__':

    result1 = calculate_average(10, 20, 30, 40, 50)
    print(f"Результат 1: {result1:.2f}\n")
    
    result2 = calculate_average(5, 15, 25)
    print(f"Результат 2: {result2:.2f}\n")
    
    result3 = calculate_average(2, 4, 6, 8, 10, 12, 14)
    print(f"Результат 3: {result3:.2f}")
