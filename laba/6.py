def calculate_mean(data):
    """Вычисление среднего арифметического"""
    return sum(data) / len(data)

def process_data(**kwargs):
    """Обработка данных и вычисление средних значений"""
    for key, values in kwargs.items():
        mean_value = calculate_mean(values)
        print(f"{key}: {values} -> Среднее: {mean_value:.2f}")

if __name__ == '__main__':
    process_data(
        group_a=[85, 90, 78, 92, 88],
        group_b=[76, 82, 95, 79, 85],
        group_c=[90, 87, 83, 91, 89],
        group_d=[68, 75, 80, 72, 78]
    )
