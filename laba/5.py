def process_kwargs(**kwargs):
    print("Первый способ вывода:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    print("\nВторой способ вывода:")
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    process_kwargs(
        students=["Анна", "Борис", "Виктор"],
        grades=[85, 92, 78],
        subjects=["Математика", "Физика", "Информатика"]
    )
