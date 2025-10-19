def personal_info(name, age, company = 'unnamed'):
    print(f'Имя: {name}, Возраст: {age}, Компания: {company}')
one = ('Тема',20,'Табачка')
two = ('Артемий',25)
personal_info(*one)
personal_info(*two)
