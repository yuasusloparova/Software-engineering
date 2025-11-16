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
