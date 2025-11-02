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
