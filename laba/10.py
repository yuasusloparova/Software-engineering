result = 0

def calculate_rectangle_area():
    global result
    width = float(input("Ширина прямоугольника: "))
    height = float(input("Высота прямоугольника: "))
    result = width * height

def calculate_triangle_area():
    global result
    base = float(input("Основание треугольника: "))
    height = float(input("Высота треугольника: "))
    result = 0.5 * base * height

if __name__ == '__main__':
    print("Выберите фигуру для расчета площади:")
    print("1 - Прямоугольник")
    print("2 - Треугольник")
    
    choice = input("Ваш выбор (1 или 2): ")
    
    if choice == '1':
        calculate_rectangle_area()
    elif choice == '2':
        calculate_triangle_area()
    else:
        print("Неверный выбор")
        result = 0
    
    print(f"Площадь фигуры: {result}")
