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
