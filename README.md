Тема 10.
Отчет по теме № 10 подготовил(а):
Суслопарова Юлия
Пиэ-23-1

| Заданияе | Выполнено |
|-----------|-----------|
| 1         | +         |
| 2         | +         |
| 3         | +         |
| 4         | +         |
| 5         | +         |
|Лабораторные задания
|-----------|-----------|
| 1         | +         |
| 2         | +         |
| 3         | +         |
| 4         | +         |
| 5         | +         |



## Задание 1.Лаба 
```python
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))

```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ffa49019-8728-4ad1-bb47-02577ca6e3c7" />
## Вывод Задание выполенно

## Задание 2.Лаба 
```python
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]
        if age < 0 or age > 130:
            age = 'Недопустимый возраст'
        input_func(name, age)

    return output_func

@check
def personal_info(name, age):
    print(f"Name: {name} Age: {age}")

personal_info('Владимир', 38)
personal_info('Александр', -5)
personal_info('Петр', 138, 15, 48, 2)
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e4924dbb-8828-4307-ae7f-a42674465bce" />
## Вывод Задание выполенно

## Задание 3.Лаба 
```python
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информация обработана')

if __name__ == '__main__':
    data([1, 15, 'Hello', 'i', 'try', 'to', 'crash', 'your', 'site', 38, 45])
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/132edea4-3cf0-4694-a3a0-d8e3bc101a89" />
## Вывод Задание выполенно

## Задание 4.Лаба 
```python
class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException('Длина более 10 символов')
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '12345678900'
    check_name(name)
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/709e893b-11e9-4520-be44-4520e7fa3056" />
## Вывод Задание выполенно

## Задание 5.Лаба 
```python
class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')

@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c7c5dc43-8ddb-480b-b8c3-4648af2e1a0c" />
## Вывод Задание выполенно

## Задание 1.сам
```python
import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time() 
        result = func()           
        end_time = time.time()    
        execution_time = end_time - start_time
        print(f"\n\nВремя выполнения: {execution_time:.6f} секунд")
        return result
    return wrapper

@timer_decorator
def fibonacci():
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')
    
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

if __name__ == '__main__':
    fibonacci()
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b268abed-43aa-4495-9a55-6d855624c357" />
## Вывод Задание выполенно

## Задание 2.сам
```python
def add_two():
    try:
        user_input = input("Введите число для сложения с 2: ")
        number = float(user_input) 
        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")
        return result
    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")
      
if __name__ == "__main__":
    print("Тест 1: ")
    add_two()
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7f76ba92-0983-4481-b1c7-722806a96438" />
## Вывод Задание выполенно

## Задание 3.сам
```python

```
## Вывод Задание выполенно


## Задание 4.сам
```python
def star_decorator(func):
    def wrapper():
        print("⭐" * 20)
        func() 
        print("⭐" * 20)
    return wrapper

@star_decorator
def say_hello():
    print("Привет, мир!")

@star_decorator
def say_bye():
    print("До свидания!")

print("=== Запускаем украшенные функции ===")
say_hello()
say_bye()
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/728dcddd-7726-4b13-be10-f276f004c618" />
## Вывод Задание выполенно


## Задание 5.сам
```python

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
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3bb8b90b-71ee-4c28-8cb8-7a03e1982e41" />
## Вывод Задание выполенно

