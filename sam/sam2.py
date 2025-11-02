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
