 Тема 6.
Отчет по теме № 3 подготовил(а):
Суслопарова Юлия
Пиэ-23-1

| Заданияе | Выполнено |
|-----------|-----------|
| 1         | +         |
| 2         | +         |
| 3         | +        |
| 4         | +         |
| 5         | +         |
|Лабораторные задания
| 1         | +         |
| 2         | +         |
| 3         | +         |
| 4         | +         |
| 5         | +         |


## Задание 1.Лаба 
```python
class Car:
    def __init__(self, make, model): #конструктор класса, который принимает 2 параметра
        self.make = make
        self.model = model
my_car = Car("Toyota", "Corolla") #создаем экземпляр класса
```
![1](lab1.png)
## Результат Задание выполенено 

## Задание 2.Лаба 
```python
class Car: #объявляем класс
    def __init__(self, make, model): #конструктор класса ринимает 2 параметра
        self.make = make
        self.model = model
    def drive(self): #добавляем метод класса
        print(f"Driving the {self.make} {self.model}")
my_car = Car("Toyota", "Corolla") #создаем экземпляр класса
my_car.drive() #вызываем метод для созданного объекта
```
![2](lab2.png)
## Результат Задание выполенено 

## Задание 3.Лаба 
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def drive(self):
        print(f"Driving the {self.make} {self.model}")
class ElectricCar(Car): # Наследование от Car
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model) # вызываем конструктор родительского класса
        self.battery_capacity = battery_capacity # добавляем новый атрибут
    def charge(self): #создаем уникальный метод для класса ElectricCar
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")
my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive() # используем унаследованный метод
my_electric_car.charge() # используем собственный метод
```
![3](lab3.png)
## Результат Задание выполенено 

## Задание 4.Лаба 
```python
class Car:
    def __init__(self, make, model):
        self._make = make # защищенный атрибут
        self.__model = model # приватный атрибут

    def drive(self):
        print(f"Driving the {self._make} {self.__model}") # метод имеет доступ ко всем атрибутам

my_car = Car("Toyota", "Corolla")
print(my_car._make) # вызова защищенного атрибута
my_car.drive() # вызов метода
```
![4](lab4.png)
## Результат Задание выполенено 

## Задание 5.Лаба 
```python
class Shape: # общий класс
    def area(self):
        pass # абстрактный метод

class Rectangle(Shape): # Класс Прямоугольник, наследуется от Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height # реализация метода поиска площади для прямоугольника

class Circle(Shape): # класс Круг, наследуется от Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius # реализация метода поиска площади для круга

# создаем объекты
my_rectangle = Rectangle(5, 4)
my_circle = Circle(5)
# вызываем методы для поиска площади
print(my_rectangle.area())
print(my_circle.area())
```
![5](lab5.png)
## Результат Задание выполенено 


## Задание 1.
```python
class Cosmetika:
    def __init__(self, name):
        self.name = name

my_cosmetika = Cosmetika("помада")
my_cosmetika.my_name()

```
![1](sam1.png)
## Результат Задание выполенено 

## Задание 2.
```python
class Cosmetika:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def my_name(self):
        print(f"Я {self.name}")
    def my_color(self):
        print(f"у меня {self.color} ")
my_animal = Cosmetika("помада", 1)
my_animal.my_name()
my_animal.my_color()
```
![2](sam2.png)
## Результат Задание выполенено 

## Задание 3.
```python
class Cosmetika:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def my_name(self):
        print(f"Я {self.name}")

    def my_color(self):
        print(f"Цвет{self.color} ")

class DomesticCosmetika(Cosmetika):
    def __init__(self, name, color, owner):
        super().__init__(name, color)
        self.owner = owner

    def my_owner(self):
        print(f"Количество - {self.owner}")


my_Cosmetika = Cosmetika("помада", 1)
my_domestic = DomesticCosmetika("румяна", 3, "много")
my_Cosmetika.my_name()
my_Cosmetika.my_color()
my_domestic.my_name()
my_domestic.my_color()
my_domestic.my_owner()
```
![3](sam3.png)
## Результат Задание выполенено 

## Задание 4. 
```python
class Cosmetika:
    def __init__(self, name, color):
        self._name = name
        self._color = color
        self.__kolvo= "много"


    def my_name(self):
        print(f"Я {self._name}")

    def my_color(self):
        print(f"цвет {self._color} ")

    def get_kolvo(self):
        return self.__kolvo

    def set_kolvo(self, status):
        allowed_statuses = ["много", "мало"]
        if status in allowed_statuses:
            self.__kolvo = status
            print(f"Статус здоровья изменен на: {status}")
        else:
            print("Недопустимый статус здоровья")

class DomesticAnimal(Cosmetika):
    def __init__(self, name, color, owner):
        super().__init__(name, color)
        self.owner = owner

    def my_owner(self):
        print(f"Помада - {self.owner}")

my_Cosmetika = Cosmetika("Помада", 1)
my_domestic = DomesticAnimal("Ремяна", 3, "много")
my_Cosmetika.my_name()
my_Cosmetika.my_color()
print(f"Статус здоровья: {my_Cosmetika.get_kolvo()}")
my_Cosmetika.set_kolvo("количество")
my_domestic.my_name()
my_domestic.my_color()
my_domestic.my_owner()
print(f"Статус здоровья: {my_domestic.get_health_status()}")
```
![4](sam4.png)
## Результат Задание выполенено 

## Задание 5.
![5](sam5.png)
## Результат Задание выполенено 


