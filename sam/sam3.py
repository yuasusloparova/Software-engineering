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
