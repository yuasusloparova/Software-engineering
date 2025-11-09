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
    

