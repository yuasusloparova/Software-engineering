Тема 9.
Отчет по теме № 9 подготовил(а):
Суслопарова Юлия
Пиэ-23-1

| Заданияе | Выполнено |
|-----------|-----------|
| 1         | +         |
| 2         | +         |
| 3         | -        |
| 4         | +         |
| 5         | +         |
|Лабораторные задания
|-----------|-----------|
| 1         | +         |



## Задание 1.Лаба 
```python

class Ivan:
    __shots__=['name']
    def __init__(self, name):
        if name == 'Иван':
            self.name = f"да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"

person1 = Ivan('Алексей')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2f5e6c3b-ea0b-45e5-9a95-8975dfb63e7f" />



## Задание 2.Лаба
```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

def composition(self):
    if self.ingredient:
        print(f"Мороженое с {self.ingredient}")
    else:
        print('Обычное мороженное')
icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composistion()
```
![2](laba2.png)


## Задание 3.Лаба 

```python
class MyClass:
    def __init__(self, value):
        self._value=value

    def set_value(self, value):
        self._value=value

    def get_value(self):
        return self._value
    
    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "свойство value")

obj = MyClass(42)
print(obj.get_value()) 
obj.set_value(45)       
print(obj.get_value())  
obj.set_value(100)    
print(obj.get_value())
```
![3](laba3.png)


## Задание 4.Лаба 
```python
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds ='weow'

dog= Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat=Cat()
print (f"Cat is {cat.className}, but they say {cat.sounds}")
```
![4](laba4.png)


## Задание 5.Лаба
```python
class Russian:
    @staticmethod 
    def greeting():
        print("привет")
class English:
    @staticmethod
    def greeting():
        print("hell0")
def greet(language):
    language.greeting()
ivan=Russian()
greet(ivan)
john=English()
greet(john)
```
![5](laba5.png)

## Самостоятельня 1
```python
class Tomato:
    states={0: 'отсутсвует',
            1: 'цветение', 
            2: 'зеленый',
            3: 'красный' }
    def __init__(self, index):
        self._index = index
        self._state = 0
    def grow(self):
        if self._state <3:
            self._state+=1
            print(f"Помидор {self._index} перешел в стадию: {self.states[self._state]}")
        else:
            print(f"Помидор {self._index} уже полностью созрел!")
    def is_ripe(self):
        return self._state == 3
class TomatoBush:

    def __init__(self, count):
        self.tomatoes = [Tomato(i) for i in range(count)]
    
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    
    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True
    
    def give_away_all(self):
        self.tomatoes = []
class Gardener:
    @staticmethod
    def knowledge_base():
        print("=== Справка по садоводству ===")
        print("1. Помидор проходит 4 стадии: отсутствует, цветение, зеленый, красный")
        print("2. Собирать урожай можно когда все помидоры красные")
        print("3. Садовник ухаживает за кустом с помощью метода work()")
        print("4. Для сбора урожая используйте метод harvest()")
    
    def __init__(self, name, plant):
       
        self.name = name          

        self.__plant = plant       
    
    def work(self):
       
        print(f"{self.name} ухаживает за растениями...")
        self.__plant.grow_all()
    
    def harvest(self):
       
        if self.__plant.all_are_ripe():
            print(f" {self.name} собирает урожай!")
            self.__plant.give_away_all()
            return True
        else:
            print(f"  {self.name}: Еще не все помидоры созрели!")
            return False



if __name__ == "__main__":
    
    Gardener.knowledge_base()
    
    print("\n" + "="*40 + "\n")
    
  
    bush = TomatoBush(2)
    gardener = Gardener("Вася", bush)
    
   
    print(f"Садовник: {gardener.name}")
    
  
    gardener.work()
    gardener.harvest() 
    
    
    gardener.work()
    gardener.harvest()  
    
   
    gardener.work()
    gardener.harvest() 

```
![6](sam.png)
