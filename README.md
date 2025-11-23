 Тема 11.
Отчет по теме №11 подготовил(а):
Суслопарова Юлия
Пиэ-23-1

| Заданияе | Выполнено |
|-----------|-----------|
| 1         | +         |
| 2         | +         |
|Лабораторные задания
| 1         | +         |
| 2         | +         |
| 3         | +         |
| 4         | +         |
| 5         | +         |


## Задание 1.Лаба 
```python
numbers=[0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f06756c0-746f-4a16-8b77-fe45f51805a7" />



## Задание 2.Лаба 
```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count

counter = CountDown(5)
for i in counter:
    print(i)
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/409aaeca-70c0-4111-86ac-607d4d00cbc8" />



## Задание 3.Лаба 
```python
a = [i ** 2 for i in range(1, 5)]

print('a - ', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))
for i in a:
    print(i)
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/07169ef6-a255-44a6-9514-43669c640ebc" />



## Задание 4.Лаба 
```python
b = (i ** 2 for i in range(1, 5))
print(b)
print('first')
for i in b:
    print(i)
print('second')

for i in b:
    print(i)
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8e5d48b7-de7e-4fb9-91b9-3224af7d2adc" />



## Задание 5.Лаба 
```python
def countdown(count):
    while count >= 0:
        yield count
        count -= 1

counter = countdown(5)
for i in counter:
    print(i)
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8da34c9d-75f4-4add-9091-7b81dbd99575" />


## Задание 1 Самостоятельная
## Задание 2 Самостоятельная
```python
def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = 200

print("Вычисление чисел Фибоначчи...")
with open("fib.txt", "w", encoding="utf-8") as file:
    for i, num in enumerate(fib(n), 1):
        file.write(f"F({i}) = {num}\n")
        
        if i == n:
            print(f"200-е число Фибоначчи: {num}")
            print(f"Все {n} чисел записаны в файл 'fib.txt'")
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4dd7a57b-97d0-4f74-a02c-44c4bd15ac73" />

