from datetime import datetime, timedelta

def calculate_future_date():
    today = datetime.today()
    print(f"Сегодня: {today.strftime('%d.%m.%Y')}")
    print(f"День недели: {today.strftime('%A')}")
    
    try:
        days = int(input("Введите количество дней: "))
        future_date = today + timedelta(days=days)
        
        print(f"Через {days} дней будет: {future_date.strftime('%d.%m.%Y')}")
        print(f"День недели: {future_date.strftime('%A')}")
        
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == '__main__':
    calculate_future_date()
