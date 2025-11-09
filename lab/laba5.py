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
